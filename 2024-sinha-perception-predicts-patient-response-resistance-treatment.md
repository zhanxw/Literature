# Paper Summary
### Authors
- Sanju Sinha et al.

### Journal
- Nature Cancer

### Publication Date
- 2024 (accepted March 8, 2024)

### DOI
- 10.1038/s43018-024-00756-7

## Keywords
- Precision oncology
- Single-cell transcriptomics
- Drug response prediction
- Tumor heterogeneity
- Treatment resistance

## Main Idea
- The paper introduces PERCEPTION, a computational pipeline that uses single-cell tumor transcriptomics to predict patient treatment response and resistance.

## Evidence Supporting the Main Idea
- The authors report validation in cultured cells, patient-tumor-derived primary cells, and clinical cohorts (multiple myeloma and breast cancer).
- They state that PERCEPTION also tracks resistance development in lung cancer patients treated with tyrosine kinase inhibitors.
- The manuscript reports PERCEPTION outperforming previously published single-cell-based and bulk-expression-based predictors across the evaluated clinical cohorts.

## Main Novelty
- A unified framework linking matched bulk/single-cell expression from drug screens to patient-level treatment prediction from single-cell tumor data.

## Datasets Used for Evaluation
- Large-scale matched bulk and single-cell expression profiles from cell-line drug screens.
- Clinical trial cohorts in multiple myeloma and breast cancer.
- Lung cancer patient cohorts treated with tyrosine kinase inhibitors.
- Exact sample sizes: Not specified in extracted text.

## Experimental Procedure
- Build response models using matched bulk and single-cell expression plus drug-screen outcomes.
- Apply models to patient single-cell tumor transcriptomes.
- Evaluate prediction of response/non-response across clinical cohorts.
- Compare against prior state-of-the-art single-cell and bulk-based predictors.

## Key Biology Insights
- Single-cell tumor heterogeneity carries actionable information for treatment matching and resistance tracking.

## Implications
- Supports broader clinical adoption of single-cell omics for precision oncology treatment planning.
