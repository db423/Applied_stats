# Antithrombotic therapy for migraine in patients with patent foramen ovale: A randomized clinical trial

Dataset DOI: [10.5061/dryad.2rbnzs84m](https://doi.org/10.5061/dryad.2rbnzs84m)

## Description of the data and file structure

This dataset was generated from a multicenter, randomized clinical trial evaluating the efficacy and safety of antithrombotic therapies for migraine in patients with patent foramen ovale (PFO).

The dataset includes two subject-level datasets (i.e., ADSL and ADACRM), along with detailed variable definitions and key statistical programs. Analysis-ready data are provided in Microsoft Excel format, and the statistical programs used to generate tables, listings, and figures (TLFs) are provided as SAS scripts.

The datasets capture participant demographics, baseline clinical characteristics, treatment allocation, headache diary–derived outcomes (including migraine days and migraine attacks), and safety outcomes. A comprehensive variable dictionary is included to facilitate interpretation of all variables.

These materials are provided to support transparency and reproducibility of the results reported in the study.

### Files and variables

### File structure

The dataset is organized into three main components:

1. **code.zip**\
   Contains all statistical analysis programs written in SAS.
   * **Macros/**
     * `allfmt.sas`: Defines variable formats used across datasets and analyses.
   * SAS macro code:
     * `M_CT_BW_NO.sas`: Analysis for baseline continuous variables and secondary continuous variables;
     * `M_CG_BW_R_ALL_.sas`, `M_CG_BW_R_ALL.sas`: Analysis for baseline categorical variables and safety outcomes;
     * `T_CT_BW_CI.sas`,`T_CG_BW_R2_diff.sas`:Analysis for secondary endpoints (between-group differences);
     * `M_CG_BW_R_ALL_NT.sas`,`T_CG_CI_CMH_CRD.sas`: Analysis for primary endpoint (descriptive analysis,  between-group differences and comparisons) and secondary categorical variables;
     * `T_CG_CI_CMH_CRD_WP.sas`: subgroup analysis;
     * `blank.sas`: A nested macro.
   * `TLF.sas`: Key code used to generate Tables, Listings, and Figures (TLFs).
2. **data.zip**\
   Contains two datasets in Excel format for analysis:
   * `adsl.xls`: dataset for analysis population determination;
   * `adacrm.xls`: dataset for analysis of baseline characteristics, primary endpoint, secondary endpoints and safety outcomes.
3. **Variable dictionary.xls**\
   Provides detailed definitions for all variables included in the datasets, including variable names, labels, variable coding, and derivation rules.

---

### Dataset description

`adsl.xls` is a participant-level dataset containing treatment group assignment and protocol deviation information. Each row represents one participant.

`adacrm.xls` is the key analysis dataset, including analysis population flag variable, baseline variables, migraine diary–derived variables, MSQ scores, safety outcomes, derived endpoints, and subgroup variables. Each row represents one participant.

---

## Variables

`subjid` indicates the random number.

`group` indicates treatment group, coded as 1=Aspirin, 2=Clopidogrel, 3=Rivaroxaban, and 4=Metoprolol.

`pdtype` indicates the type of protocol deviation.

`fasfl` indicates inclusion in the full analysis set (FAS), coded as 1=Yes and 2=No.

`pprotfl` indicates inclusion in the per-protocol set (PPS), coded as 1=Yes and 2=No.

`age round` indicates rounded age in years.

`sex` indicates gender, coded as 1=Male and 2=Female.

`bmi cat` indicates body mass index category.

`comy` indicates duration of migraine in years.

`migzz_v1` indicates migraine with aura, coded as 1=Yes and 2=No.

`ech_v1` indicates transthoracic echocardiography (TTE), coded as 1=Yes and 2=No.

`xztee_v1` indicates transesophageal echocardiography (TEE), coded as 1=Yes and 2=No.

`xztee1a_v1` indicates contrast transthoracic echocardiography (cTTE), coded as 1=Yes and 2=No.

`xztee1b_v1` indicates contrast transesophageal echocardiography (cTEE), coded as 1=Yes and 2=No.

`xztee1c_v1` indicates contrast transcranial Doppler (cTCD), coded as 1=Yes and 2=No.

`ech29_v1` indicates right-to-left shunt (RLS) grade, coded as 0=Grade 0, 1=Grade 1, 2=Grade 2, and 3=Grade 3.

`migpl1_v1` indicates the number of migraine days per month at baseline.

`migpl3_v1` indicates the number of migraine attacks per month at baseline.

`msqr_v1` indicates the role restrictive (RR) domain of the Migraine-Specific Quality of Life Questionnaire (MSQ) at baseline.

`msqp_v1` indicates the role preventive (RP) domain of MSQ at baseline.

`msqe_v1` indicates the emotional function (EF) domain of MSQ at baseline.

`mi` indicates history of myocardial infarction, coded as 1=Yes and 2=No.

`ang` indicates angina, coded as 1=Yes and 2=No.

`smoke` indicates smoking status, coded as 1=Yes and 2=No.

`hyp` indicates hypertension, coded as 1=Yes and 2=No.

`dia` indicates diabetes mellitus, coded as 1=Yes and 2=No.

`hype` indicates hyperlipidemia, coded as 1=Yes and 2=No.

`snore` indicates snoring, coded as 1=Yes and 2=No.

`palp` indicates palpitations, coded as 1=Yes and 2=No.

`jsxt` indicates psychiatric disorders, coded as 1=Yes and 2=No.

`tws` indicates history of head trauma, coded as 1=Yes and 2=No.

`pill` indicates contraceptive drug use, coded as 1=Yes and 2=No.

`cein` indicates cerebral infarction, coded as 1=Yes and 2=No.

`tia` indicates transient ischemic attack, coded as 1=Yes and 2=No.

`wzjb` indicates peripheral vascular disease, coded as 1=Yes and 2=No.

`rein` indicates respiratory insufficiency, coded as 1=Yes and 2=No.

`nyha` indicates NYHA class I heart function, coded as 1=Yes and 2=No.

`atfi` indicates atrial fibrillation, coded as 1=Yes and 2=No.

`arrhy` indicates other arrhythmias, coded as 1=Yes and 2=No.

`jwpci` indicates previous percutaneous coronary intervention, coded as 1=Yes and 2=No.

`jwcabg` indicates previous coronary artery bypass grafting, coded as 1=Yes and 2=No.

`jwtt` indicates previous migraine preventive treatment, coded as 1=Yes and 2=No.

`jxyy` indicates acute medication use, coded as 1=Yes and 2=No.

`migpl3_v1a` indicates monthly migraine attacks at baseline and is derived from `migpl3_v1`.

`migpl1_v1a` indicates monthly migraine days at baseline and is derived from `migpl1_v1`.

`pl3_v3`, `pl3_v4`, and `pl3_v5` indicate monthly migraine attacks at weeks 4, 8, and 12.

`pl1_v3`, `pl1_v4`, and `pl1_v5` indicate monthly migraine days at weeks 4, 8, and 12.

`msqr_v1a`, `msqp_v1a`, and `msqe_v1a` indicate baseline MSQ domain scores derived from original variables.

`pl7_v3–pl7_v5`, `pl8_v3–pl8_v5`, and `pl9_v3–pl9_v5` indicate MSQ domain scores at follow-up visits.

`msqt1v`, `msqt3v`, `msqt4v`, and `msqt5v` indicate total MSQ scores at baseline and follow-up visits.

`ae` indicates any adverse event, coded as 1=Yes and 2=No.

`impae` indicates adverse events related to investigational medicinal products (IMPs), coded as 1=Yes and 2=No.

`sae` indicates any serious adverse event, coded as 1=Yes and 2=No.

`impsae` indicates serious adverse events related to IMPs, coded as 1=Yes and 2=No.

`bleed` indicates any bleeding event, coded as 1=Yes and 2=No.

`hemor` indicates major bleeding, coded as 1=Yes and 2=No.

`rrydl` indicates the primary endpoint-respondse rate, coded as 1=Yes and 2=No, defined as a ≥50% reduction in monthly migraine days or attacks at 12 weeks compared with baseline.

`rrydllo` indicates response rate using LOCF imputation.

`rdlt` indicates response rate based on migraine days only, coded as 1=Yes and 2=No.

`rdltlo` indicates response rate based on migraine days only using LOCF imputation.

`avdm` and `avcm` indicate absolute reductions in migraine days and attacks.

`avdmr` and `avcmr` indicate percentage reductions in migraine days and attacks.

`coce` indicates complete cessation of migraine, coded as 1=Yes and 2=No.

`chrr`, `chrp`, and `chef` indicate changes in MSQ domain scores.

`chmsq` indicates change in total MSQ score.

`pttyx` indicates migraine frequency subgroup, coded as 1=<15 days/month and 2=≥15 days/month.

`ageyz` indicates age subgroup, coded as 1=≥38.5 years and 2=<38.5 years.

---

## Missing data

Missing values are represented by blank cells. In addition, indicator variables (e.g., `migpl31v`, `pl33v`, `msqr1v`) identify missingness  at specific time points, coded as 1=Yes and 2=No.

---

## Code/software

The datasets are provided in Microsoft Excel (.xls) format and can be opened using Microsoft Excel, LibreOffice Calc, OpenOffice Calc, or other compatible software.

Statistical analysis code is provided as SAS programs (.sas). Analyses were originally conducted using SAS software.

Recommended software:

* SAS version 9.4 or later for reproducing analyses
* Microsoft Excel or equivalent for viewing datasets
* Any text editor for reviewing SAS code

### Workflow

1. Open datasets in `data.zip`.
2. Refer to `Variable dictionary.xls` for variable definitions.
3. Load macro and format files from `code.zip/Macros/`.
4. Run `TLF.sas` to generate tables, listings, and figures.
5. Individual scripts may also be run separately for specific analyses.

No proprietary software is required to view the datasets; however, SAS is required to reproduce the analyses.

---

## Access information

Other publicly accessible locations of the data: None.

The data are exclusively available through the Dryad Digital Repository associated with this study.

Data source: The data were generated prospectively as part of a multicenter randomized clinical trial conducted by the study investigators.


## Human subjects data

All participants provided written informed consent prior to enrollment, which included consent for the use of their data for research purposes and for sharing of de-identified data in the public domain.

Prior to data sharing, all datasets were fully de-identified to protect participant privacy. Direct identifiers (including names, contact information, identification numbers, and exact addresses) were removed. Indirect identifiers were minimized or generalized where necessary, including dates and site-level information, to reduce the risk of re-identification. Each participant was assigned a unique study identification number with no linkage to personal identifiers.

The shared dataset contains no information that could reasonably be used to identify individual participants.