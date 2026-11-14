# Paper Summary

### Authors

Fateme Nateghi Haredasht, Nicholas P. Marshall, Wenyuan Chen, Lauren N. Cooper, Ziming Wei, Harrison Konsker, Jacob S. Chen, Michael Klompas, Cara McKenna, Richard J. Medford, Sanjat Kanjilal, Austin J. Schoeffler, Stephen P. Ma, Niaz Banaei, Steven M. Asch, Amy Chang, Stanley C. Deresinski, Mary K. Goldstein, Robert Tibshirani, and Jonathan H. Chen.

### Journal

Not specified in paper; arXiv preprint (arXiv:2610.32998v1, q-bio.QM / cs.LG).

### Publication Date

2026-10-06 (arXiv v1).

### DOI

Not specified in paper.

## Keywords

Antimicrobial resistance; antibiotic susceptibility; electronic health records; machine learning; XGBoost; empiric therapy; transportability; calibration; personalized antibiogram; stewardship.

## Main Idea

ARMD-Predict uses routinely available EHR information at the time of culture ordering to estimate antibiotic-specific susceptibility before laboratory susceptibility results are available. It combines two research pipelines: (1) 23 pooled models predicting susceptibility to individual antibiotics and (2) a hierarchical pipeline predicting Gram class, organism identity, and organism-specific resistance phenotypes aligned where applicable with 2024 IDSA guidance (Fig. 2).

The models were trained across Stanford Health Care, East Carolina University Health, UT Southwestern Medical Center, and Mass General Brigham. The authors argue that multi-site pooling can provide reasonably consistent discrimination across represented hospitals and generate testable stewardship hypotheses, but they do not present the system as ready for clinical use.

## Evidence Supporting the Main Idea

- The source cohort contained 7,516,390 culture–antibiotic observations from adults with urine, blood, or respiratory cultures at four U.S. academic medical centers. After excluding 116,607 observations with unknown ordering mode and applying cell-size and class-balance criteria, the modeling cohort contained 7,337,676 observations across 249 eligible antibiotic–specimen–setting cells (Fig. 1).
- Across 23 pooled susceptibility models, median held-out AUROC was 0.77 for inpatient urine cultures, 0.70 for inpatient blood cultures, 0.71 for outpatient urine cultures, and 0.82 for the single outpatient respiratory model (Table 1). Site-specific AUROC across 87 reportable cells had a median of 0.710.
- In inpatient urine cultures, ceftriaxone susceptibility had AUROC 0.773 and meropenem susceptibility 0.831; in inpatient blood cultures, ceftriaxone had AUROC 0.703 and meropenem 0.835 (Table 1).
- The site-aware pooled model had median AUROC 0.765 across 28 inpatient urine antibiotic–site cells. A site-agnostic pooled model performed nearly identically, with a median difference below 0.001 AUROC, supporting release of models without site identity (Fig. 3).
- At an exploratory threshold requiring at least 95% positive predictive value for narrowing, 54.9% of ceftriaxone-susceptible inpatient urine observations were identified for narrower therapy. A complementary threshold flagged 60.1% of ceftriaxone-resistant observations for broader coverage while limiting flags among susceptible observations to 20% (Fig. 4).
- The organism classifiers achieved top-1 accuracy of 25.1–67.0% and top-3 accuracy of 51.3–83.3% across ten completed variants. Conditional organism-specific phenotype models reached AUROC 0.759 for ceftriaxone non-susceptibility in *E. coli*, 0.793 in *K. pneumoniae*, and 0.834 for meropenem resistance in *P. aeruginosa*.
- Prior-resistance features ranked first in 13 of 23 susceptibility models and within the top two in 18; recent antibiotic exposure was among the ten leading encoded features in 19 models, and an Area Deprivation Index feature was among the top features in 15 (Extended Data Fig. 6). These are predictive associations, not causal findings.

## Main Novelty

- Multi-site development using harmonized EHR data from four academic medical centers rather than a single-hospital model.
- Parallel prediction of antibiotic-specific susceptibility and organism/resistance phenotypes, allowing the two outputs to address complementary pre-culture questions.
- Explicit evaluation of site pooling, temporal degradation, calibration, local-prevalence re-anchoring, exploratory stewardship thresholds, and prespecified subgroup discrimination.
- Public research applications and model artifacts intended for external technical evaluation.

## Datasets Used for Evaluation

- **Stanford Health Care:** 1,979,116 culture–antibiotic observations, collected October 2007–January 2024. Used in pooled training/evaluation and in a separate family of 24 chronologically evaluated Stanford-only models.
- **East Carolina University Health (ECUH):** 1,991,320 observations, collected November 2014–February 2025. Used in pooled training/evaluation and transportability analyses.
- **UT Southwestern Medical Center (UTSW):** 1,340,851 observations, collected April 2006–February 2025. Used in pooled training/evaluation and transportability analyses.
- **Mass General Brigham (MGB):** 2,205,103 observations. Patient-specific date shifts preserved within-patient intervals but prevented use of a calendar window; MGB used a deterministic patient-hash split for some model families.
- **Pooled modeling cohort:** 7,337,676 observations after exclusions and eligibility filters: 4,019,315 inpatient and 3,318,361 outpatient observations, from urine, blood, and respiratory cultures. The final models were evaluated on held-out patient-grouped partitions; the pooled susceptibility test partitions contained 375,501 observations across 23 released models.
- The data included culture orders and susceptibility results linked to demographics, care setting, prior antibiotics, procedures, nursing-home history, prior resistance events, comorbidities, Area Deprivation Index, and—where available—laboratory values and vital signs. Vital signs were omitted from the released pooled models because they were not available at all four sites.

## Experimental Procedure

- Harmonize microbiology and EHR data from the four sites using a common data model and normalize antibiotic names across sites.
- Encode susceptible results as the positive class; treat resistant and intermediate results as not susceptible. Use measured laboratory results preferentially when measured and inferred labels conflict.
- Construct longitudinal feature blocks for demographics, care setting, comorbidities, prior antibiotics, procedures, nursing-home history, prior organisms, resistance events, same-antibiotic resistance, Area Deprivation Index, laboratory values, and available vital signs.
- Exclude same-day history records when the data could not establish that the event preceded the culture order, remove leakage-prone timestamps, and represent missingness separately from zero.
- Train one XGBoost susceptibility model per eligible antibiotic–specimen–setting cell. Eligibility required at least 500 pooled observations and at least 25 susceptible and 25 resistant results. Apply monotonic constraints so that additional prior resistance or antibiotic exposure cannot increase predicted susceptibility.
- For pooled susceptibility models, use a random patient-grouped 60/20/20 train/validation/test split. Compare pooled models with Stanford-only models, site-aware pooling, site-agnostic pooling, and GroupDRO. Also evaluate chronological splits; chronological retraining reduced AUROC by a mean of 0.0396 and median of 0.0411 in 21 matched analyses.
- For the organism/resistance pipeline, use Gram-positive versus Gram-negative classification, 21-class organism prediction (20 frequent labels plus Other), and 30 organism-specific binary phenotype models. Phenotype targets include ESBL, AmpC, CRE, difficult-to-treat *P. aeruginosa* proxies, MRSA, and VRE where data supported training.
- Evaluate AUROC, AUPRC, specificity at 90% sensitivity for susceptibility, calibration error, Brier score, subgroup AUROC, and SHAP feature attribution. Assess operating points for narrowing at positive predictive value of at least 95% and for broader coverage while flagging no more than 20% of susceptible observations.
- Evaluate local-prevalence re-anchoring using a prior-probability-shift correction. The held-out-site prevalence used in this retrospective analysis is an oracle quantity and would need to be prespecified prospectively.

## Key Biology Insights

- Patient history of resistance and recent antibiotic exposure were the strongest recurring predictive signals, consistent with the known contribution of previous antimicrobial selection and colonization/infection history to resistance risk.
- Resistance prevalence varied substantially among the participating hospitals and differed from national surveillance estimates; for example, VRE prevalence among *E. faecium* was 54.3% in this cohort versus approximately 30% nationally.
- Organism identity remains a major biological determinant of antibiotic activity. Ampicillin susceptibility was difficult to predict without knowing the organism because *P. aeruginosa* and *K. pneumoniae* were almost never susceptible while *E. faecalis* was nearly always susceptible.
- The organism-specific phenotype results support conditional prediction after the organism is known, but they do not validate the full pre-culture cascade: phenotype AUROCs were evaluated using the observed organism label rather than the organism predicted by the preceding hierarchy.
- Socioeconomic context, represented by the neighborhood-level Area Deprivation Index, contributed predictive signal, but the study does not establish a causal pathway or demonstrate equitable clinical effects.

## Implications

ARMD-Predict demonstrates that multi-site EHR models can provide moderate-to-good retrospective discrimination for several antibiotic–specimen–setting combinations before culture results are available. The results support further research into personalized empiric therapy and stewardship, especially where prior resistance and antibiotic exposure histories are available.

The findings do not establish improved prescribing, patient safety, time to active therapy, or clinical outcomes. Chronological performance was lower than same-period performance; calibration model selection reused the test set; operating thresholds and yields were derived and evaluated on the same observations; phenotype models were not evaluated end-to-end; and all sites were U.S. academic medical centers. Polymicrobial cultures were represented at the organism level rather than as order-level coverage outcomes, and 7.1–21.4% of observations used laboratory-inferred susceptibility labels across sites.

Before clinical use, the authors recommend independent temporal and geographic validation, calibration and threshold selection without test-set reuse, end-to-end validation of the organism hierarchy, auditing of inferred labels, silent prospective evaluation, and later assessment of prescribing changes, broad-spectrum exposure, adverse events, patient outcomes, alert burden, and subgroup effects. Research applications are available at <https://armd-predict.stanford.edu>.

