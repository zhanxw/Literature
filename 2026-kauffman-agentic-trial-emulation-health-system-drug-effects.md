# Paper Summary

**Title:** Agentic Trial Emulation to Learn Health System-specific Drug Effects At Scale

### Authors
Justin Kauffman, Lisa Duan, Samuel Gelman, Eyal Klang, Ankit Sakhuja, Deepak L. Bhatt, Vivek Y. Reddy, Alexander W. Charney, Girish N. Nadkarni, Yuanhao Qu, Kexin Huang, Joshua Lampert, and Benjamin S. Glicksberg. Kauffman and Duan contributed equally; Lampert and Glicksberg are co-senior authors.

### Journal
medRxiv preprint, version 1; not peer reviewed in the version summarized.

### Publication Date
February 20, 2026 (version 1 posting date).

### DOI
[10.64898/2026.02.19.26346539](https://doi.org/10.64898/2026.02.19.26346539)

Source: [version 1 PDF](https://www.medrxiv.org/content/10.64898/2026.02.19.26346539v1.full.pdf). Read the 33-page PDF, including embedded Supplementary Methods and figures/tables. Some supplementary result tables referenced in the prose are not present in this PDF; reported numerical findings below are distinguished from directly visible tables.

## Keywords
Target trial emulation; Biomni; autonomous agents; OMOP; atrial fibrillation; anticoagulation; Bayesian calibration; transportability; real-world evidence.

## Main Idea
An autonomous Biomni workflow emulates anticoagulation trials from EHR data and retrieves literature-derived expectations of EHR-RCT discrepancies. A Bayesian hierarchical model then learns a shared institutional shift and residual heterogeneity. The authors propose using repeated emulations to learn how external trial evidence differs from a health system's observed estimates (Figure 1, PDF p. 28; Methods, pp. 4-6).

## Evidence Supporting the Main Idea
- **Repeated execution:** Four DOAC-versus-warfarin trials generated 12 run-level estimates (three runs per trial); AVERROES was reserved for a different-comparator evaluation. The agent made choices at 26 documented decision points, exposing run-to-run variability (Results, pp. 7-8).
- **Reported calibration:** Across four held-out trials, mean absolute error decreased from 0.567 to 0.224 log-HR, a 60.5% reduction; all four trial effects were covered by 95% predictive intervals. Four observations provide limited evidence about interval calibration (Results; Figure 3).
- **Heterogeneous performance:** The RE-LY error worsened from 0.187 to 0.316 after calibration, despite aggregate improvement. ENGAGE AF error fell from 1.247 to 0.016, with the large original discrepancy driven by an outlier run (p. 8).
- **Different comparator:** AVERROES error reportedly fell from 0.379 to 0.051 log-HR, an 86.5% reduction. This is one additional trial, not validation in a separate health system (p. 8).
- **Directly visible quality diagnostics:** Table 1 (PDF p. 32) shows a maximum SMD of 0.335 for the selected ENGAGE AF run and a crude log-incidence-rate ratio for RE-LY. Its footnote states that no dabigatran run achieved propensity-score adjustment. These materially limit the causal interpretation of the uncalibrated inputs.

## Main Novelty
Combines autonomous trial emulation, replicated agent runs, literature-informed priors, and cross-trial hierarchical calibration. Its distinctive proposal is to model systematic discrepancies jointly instead of judging each emulation independently. Learning a statistical shift does not itself identify whether it reflects care differences, confounding, measurement error, or implementation error.

## Datasets Used for Evaluation
- **Mount Sinai OMOP CDM v5.4 EHR:** Drug exposures, conditions, measurements, procedures, demographics, observation periods, and death records, represented using RxNorm/SNOMED CT/LOINC and stored as Parquet on Minerva. Figure 1 labels the source as over 12 million patients; this is the source resource, not the analytic sample (Supplementary Methods S1; Figure 1).
- **Selected analytic cohorts:** Table 1 reports exposure/comparator counts of 32,208/12,500 for ARISTOTLE, 142/22,480 for ENGAGE AF, 2,738/20,690 for RE-LY, and 12,941/12,919 for ROCKET AF. Counts are for selected best runs and should not be summed as unique patients. Full per-run counts and AVERROES cohort size: Not specified in the supplied PDF.
- **RCT benchmarks:** ARISTOTLE (apixaban), ROCKET AF (rivaroxaban), RE-LY (dabigatran), and ENGAGE AF-TIMI 48 (edoxaban), each versus warfarin for stroke/systemic embolism; AVERROES compares apixaban with aspirin. Four trials support calibration and one supports a different-comparator test (Supplementary Methods S2).
- **Literature retrieval:** Table 3 (p. 33) reports 482, 174, 559, and 560 retrieved PMIDs for apixaban, edoxaban, dabigatran, and rivaroxaban, respectively. These are retrieval counts, not necessarily independent effect estimates included in the prior. Final source-level estimate counts: Not specified in the supplied PDF.

## Experimental Procedure
- Give Biomni investigator-authored instructions and trial manuscripts; extract protocol elements and construct OMOP concept sets.
- Build treatment/comparator cohorts with first qualifying exposure as index; extract baseline covariates and follow outcomes.
- Prefer stabilized IPTW with 1st/99th-percentile truncation and weighted Cox analysis; permit adjusted Cox and then unadjusted fallbacks when methods fail (Supplementary Methods S5).
- Retrieve observational literature, estimate discrepancies from RCT log-HRs, and form comparison-specific priors with domain-transfer uncertainty.
- Flag sparse events, large discrepancies, and poor balance; diagnose and, where indicated, refine and rerun the emulation while retaining artifacts.
- Execute three independent runs per trial; fit hierarchical calibration in PyMC; evaluate leave-one-trial-out performance and AVERROES generalization.
- Report institution-shift posterior medians of 0.364-0.580 and residual-heterogeneity medians of 0.199-0.264 across folds (Results).

## Key Biology Insights
No new drug mechanism or independently validated local causal effect is established. The authors interpret a positive institutional shift as attenuation of DOAC benefit relative to randomized evidence and discuss warfarin management, dosing, adherence, case mix, and outcome ascertainment as possible explanations. These mechanisms are proposed explanations, not separately measured or identified causes of the shift (Discussion, pp. 9-11).

## Implications
- **Authors' interpretation:** Automated replication could support cumulative institutional learning and uncertainty-aware translation of trial evidence. They acknowledge the small training set, additive/stable-shift assumptions, and restriction to efficacy rather than net clinical benefit.
- **Assessment:** Repeated runs reuse the same database and trials; they characterize agent variability but do not create independent patient populations or additional independent trials.
- **Assessment:** The unadjusted fallback and persistent imbalance in Table 1 show why agent execution success must be separated from causal validity. Calibration toward trial results cannot establish that a local causal effect is identified.
- **Model specification concern:** The prose and Table 2 define the literature prior as an EHR-minus-RCT discrepancy, but the equations use its mean directly as the prior mean of a latent treatment effect. These are different quantities and need reconciliation (Methods; Supplementary Methods S6-S7).
- **Evaluation concern:** The pipeline can inspect published trial effects and refine emulations after observing discrepancies. The holdout description explicitly removes held-out EHR runs but does not clearly document masking the held-out RCT result from all prior construction and refinement. Independence from benchmark information therefore remains unclear.
- **Reporting caveat:** Table numbering in the Results does not match the final displayed tables, several referenced supplementary result tables are absent, and the ethics section retains a protocol-number placeholder. These gaps limit reproducibility of the available version.
