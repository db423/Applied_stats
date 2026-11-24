# %%
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import chi2
import matplotlib.pyplot as plt

# %%
rng = np.random.default_rng(seed=42)
def simulate_trial(n_per_arm, rng):
    x_i = np.repeat([0, 1], n_per_arm)
    z_i = rng.binomial(n=1, p=0.5, size=2 * n_per_arm)
    n_i = np.log(7/13) + np.log(1.6)*x_i + np.log(39/7)*z_i
    p_i = 1 / (1+np.exp(-n_i))
    Y_i = rng.binomial(1, p_i)
    return x_i, z_i, Y_i


    

# %%
x,z,y = simulate_trial(100, rng)
df = pd.DataFrame({"x":x , "z":z, "y":y})
df.groupby(["x", "z"])["y"].mean()

# %%
fit_full = smf.glm("y ~ z + x", data=df, family=sm.families.Binomial()).fit()
fit_full.summary()

# %%
fit_null = smf.glm("y ~ z", data=df, family=sm.families.Binomial()).fit()
lrt_stat = fit_null.deviance - fit_full.deviance
p_val = chi2.sf(lrt_stat, df = 1)
reject_h0 = p_val < 0.05

print(f"LRT stat: {lrt_stat:.4f}, p-value: {p_val:.4f}, Reject H0: {reject_h0}")

# %%
rng2 = np.random.default_rng(42)
def one_trial(n_per_arm, rng):
    x, z, y = simulate_trial(n_per_arm, rng)
    df = df = pd.DataFrame({"x":x , "z":z, "y":y})
    fit_full_adjusted = smf.glm("y ~ z + x", data=df, family=sm.families.Binomial()).fit()
    fit_null_adjusted = smf.glm("y ~ z", data=df, family=sm.families.Binomial()).fit()
    fit_full_unadjusted = smf.glm("y ~ x", data=df, family=sm.families.Binomial()).fit()
    fit_null_unadjusted = smf.glm("y ~ 1", data=df, family=sm.families.Binomial()).fit()
    lrt_stat_adjusted = fit_null_adjusted.deviance - fit_full_adjusted.deviance
    lrt_stat_unadjusted = fit_null_unadjusted.deviance - fit_full_unadjusted.deviance
    reject_adj = lrt_stat_adjusted > chi2.ppf(0.95, df = 1)
    reject_unadj = lrt_stat_unadjusted > chi2.ppf(0.95, df = 1)
    return (reject_adj, reject_unadj)


    

# %%
one_trial(200, rng2)

# %%
rng = np.random.default_rng(42)
M = 200
n_grid = np.arange(50, 451, 25)

rows = []
for n in n_grid:
    # Shape: (M, 2) array of True/False
    trials = np.array([one_trial(n, rng) for _ in range(M)])
    power_adj, power_unadj = trials.mean(axis=0)
    
    se_adj = np.sqrt(power_adj * (1 - power_adj) / M)
    se_unadj = np.sqrt(power_unadj * (1 - power_unadj) / M)
    
    rows.append({
        "n_per_arm": n,
        "n_total": 2 * n,
        "power_adj": power_adj,
        "se_adj": se_adj,
        "power_unadj": power_unadj,
        "se_unadj": se_unadj,
    })

results_df = pd.DataFrame(rows)
print(results_df)

# %%

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.plot(results_df["n_per_arm"], results_df["power_adj"], marker="o", label="Adjusted LRT (y ~ z + x)")
ax.axhline(0.80, color="red", linestyle="--", label="80% Target Power")

ax.set_xlabel("Sample Size per Arm (n)")
ax.set_ylabel("Estimated Power")
ax.set_title("Initial Power Curve vs. Sample Size")
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.show()

# %%


fig, ax = plt.subplots(figsize=(7, 4.5))


ax.plot(results_df["n_per_arm"], results_df["power_adj"], "o-", label="Adjusted (response ~ profile + treatment)")
ax.fill_between(
    results_df["n_per_arm"],
    results_df["power_adj"] - 1.96 * results_df["se_adj"],
    results_df["power_adj"] + 1.96 * results_df["se_adj"],
    alpha=0.2,
)


ax.plot(results_df["n_per_arm"], results_df["power_unadj"], "s--", label="Unadjusted (response ~ treatment)")
ax.fill_between(
    results_df["n_per_arm"],
    results_df["power_unadj"] - 1.96 * results_df["se_unadj"],
    results_df["power_unadj"] + 1.96 * results_df["se_unadj"],
    alpha=0.2,
)

ax.axhline(0.80, color="gray", linestyle=":", label="80% Target Power")
ax.set_xlabel("Sample Size per Arm (n)")
ax.set_ylabel("Estimated Power")
ax.legend()
plt.tight_layout()
plt.show()

# %%
rng = np.random.default_rng(42)
large_n = 200000
x1, z1, y1 = simulate_trial(large_n, rng)
df2 = pd.DataFrame({'x':x1, 'z':z1, 'y':y1})

fit_1 = smf.glm("y ~ z + x", data=df2, family=sm.families.Binomial()).fit()
fit_2 = smf.glm("y ~ x", data=df2, family=sm.families.Binomial()).fit()

print("Adjusted Beta_1 : " + str(fit_1.params['x']))
print("Unadjusted Beta_1 : " + str(fit_2.params['x']))

# %%



