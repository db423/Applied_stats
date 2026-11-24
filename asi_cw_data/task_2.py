# %%
import pandas as pd
import numpy as np
from pathlib import Path
from urllib.request import urlretrieve
from scipy import stats
from IPython.display import display
import statsmodels.api as sm
import statsmodels.formula.api as smf

# %%
%pip install "xlrd>=2.0.1"

# %%
for fn in ["Variable_dictionary.xls", "data/adsl.xls", "data/adacrm.xls"]:
    print(fn, pd.ExcelFile(fn).sheet_names)


vd = pd.read_excel("Variable_dictionary.xls", sheet_name="Dictionary")
adsl = pd.read_excel("data/adsl.xls", sheet_name="Sheet")
adacrm = pd.read_excel("data/adacrm.xls", sheet_name="Sheet")

print("IDs identical:", (adsl["subjid"] == adacrm["subjid"]).all())
print("Groups identical:", (adsl["group"] == adacrm["group"]).all())
print("\nRandomised per arm:\n", adacrm["group"].value_counts().sort_index())


# %%
baseline_cols = ["age_round", "sex", "migzz_v1", "ech29_v1", "migpl1_v1", "migpl3_v1"]
print(adacrm.groupby("group")[baseline_cols].mean().round(2))

print("\nProtocol deviations by group:")
print(pd.crosstab(adsl["group"], adsl["pdtype"], dropna=False))

# %%

df = pd.merge(
    adsl[["subjid", "group", "pdtype"]],
    adacrm[["subjid", "fasfl", "pprotfl", "rrydl", "rrydllo"]],
    on="subjid",
)
sub = df[df["group"].isin([1, 4])].copy()


print("FAS inclusion by protocol deviation:")
print(pd.crosstab([sub["group"], sub["fasfl"]], sub["pdtype"].fillna("None")))


fas_sub = sub[sub["fasfl"] == 1]
print("\nMissing week-12 outcome within FAS == 1:")
print(pd.crosstab([fas_sub["group"], fas_sub["rrydl"].isna()], fas_sub["pdtype"].fillna("None")))

# %%
for g, name in [(1, "Aspirin"), (4, "Metoprolol")]:
    arm = sub[sub["group"] == g]
    n_rand = len(arm)
    n_fas = (arm["fasfl"] == 1).sum()
    n_obs = ((arm["fasfl"] == 1) & (arm["rrydl"].notna())).sum()
    n_resp = ((arm["fasfl"] == 1) & (arm["rrydl"] == 1)).sum()
    print(f"{name}: Randomised={n_rand}, FAS={n_fas}, Observed Wk12={n_obs}, Responders={n_resp} ({n_resp / n_obs:.2%})")

# %%
ana = sub[(sub["fasfl"] == 1) & (sub["rrydl"].notna())].copy()

# Recode 1=Yes -> 1, 2=No -> 0 explicitly (safer than (rrydl == 1).astype(int), which turns NaN into 0)
ana["response"] = ana["rrydl"].map({1: 1, 2: 0})


ana["aspirin"] = (ana["group"] == 1).astype(int)


print(ana.groupby("aspirin")["response"].agg(n_obs="count", responders="sum", prop="mean"))

# %%
fit = smf.glm("response ~ aspirin", data=ana, family=sm.families.Binomial()).fit()
fit.summary()

# %%
b0 = fit.params["Intercept"]
b1 = fit.params["aspirin"]
se_b1 = fit.bse["aspirin"]

or_est = np.exp(b1)
or_low, or_high = np.exp([b1 - 1.96 * se_b1, b1 + 1.96 * se_b1])
print(f"Odds Ratio: {or_est:.3f} (95% CI: {or_low:.3f} to {or_high:.3f})")

# %%
p0 = 1 / (1 + np.exp(-b0))
p1 = 1 / (1 + np.exp(-(b0 + b1)))
diff = p1 - p0

n0 = (ana["aspirin"] == 0).sum()
n1 = (ana["aspirin"] == 1).sum()
se_diff = np.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)

diff_100 = 100 * diff
ci_low_100 = 100 * (diff - 1.96 * se_diff)
ci_high_100 = 100 * (diff + 1.96 * se_diff)
print(f"Difference per 100 treated: {diff_100:.2f} (95% CI: {ci_low_100:.2f} to {ci_high_100:.2f})")


# %%

fas_df = adacrm[(adacrm["group"].isin([1, 4])) & (adacrm["fasfl"] == 1)].copy()
fas_df["aspirin"] = (fas_df["group"] == 1).astype(int)


fas_df["resp_locf"] = fas_df["rrydllo"].map({1: 1, 2: 0})
fit_locf = smf.glm("resp_locf ~ aspirin", data=fas_df, family=sm.families.Binomial()).fit()
or_locf = np.exp(fit_locf.params["aspirin"])
ci_locf = np.exp([
    fit_locf.params["aspirin"] - 1.96 * fit_locf.bse["aspirin"],
    fit_locf.params["aspirin"] + 1.96 * fit_locf.bse["aspirin"],
])
print(f"LOCF Sensitivity OR: {or_locf:.3f} (95% CI: {ci_locf[0]:.3f} to {ci_locf[1]:.3f})")


ana_cov = fas_df[fas_df["rrydl"].notna()].copy()
ana_cov["response"] = ana_cov["rrydl"].map({1: 1, 2: 0})
fit_adj = smf.glm(
    "response ~ aspirin + migpl1_v1 + migzz_v1 + ech29_v1",
    data=ana_cov,
    family=sm.families.Binomial(),
).fit()
or_adj = np.exp(fit_adj.params["aspirin"])
ci_adj = np.exp([
    fit_adj.params["aspirin"] - 1.96 * fit_adj.bse["aspirin"],
    fit_adj.params["aspirin"] + 1.96 * fit_adj.bse["aspirin"],
])
print(f"Baseline-Adjusted Conditional OR: {or_adj:.3f} (95% CI: {ci_adj[0]:.3f} to {ci_adj[1]:.3f})")


safety_cols = ["ae", "sae", "bleed", "hemor"]
safety_rates = fas_df.groupby("group")[safety_cols].apply(lambda g: (g == 1).mean() * 100).round(2)
print("\nSafety event rates (% of FAS, 1=Aspirin, 4=Metoprolol):")
print(safety_rates)


