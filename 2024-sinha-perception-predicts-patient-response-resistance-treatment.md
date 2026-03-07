# Paper Summary

### Authors
- Sanju Sinha et al.

### Journal
- Nature Cancer

### Publication Date
- 2024

### DOI
- https://doi.org/10.1038/s43018-024-00756-7

## Keywords
- precision oncology
- single-cell transcriptomics
- treatment response prediction
- resistance evolution
- tumor heterogeneity
- PERCEPTION

## Main Idea
- The paper presents PERCEPTION, a computational pipeline that predicts patient treatment response and resistance using single-cell tumor transcriptomics.
- It is trained using large preclinical resources linking expression profiles and drug-response phenotypes, then transferred to patient settings.
- The framework aims to personalize therapy by modeling clone-level heterogeneity rather than relying only on bulk averages.

## Evidence Supporting the Main Idea
- PERCEPTION was validated in cultured and patient-derived primary-cell settings for targeted therapy prediction.
- The framework showed predictive utility in clinical-trial cohorts for multiple myeloma and breast cancer.
- It captured resistance development trajectories in tyrosine-kinase-inhibitor-treated lung cancer patients.
- The paper reports that PERCEPTION outperformed published single-cell-based and bulk-expression-based comparators across evaluated clinical cohorts.

## Main Novelty
- Systematic use of single-cell tumor expression to build patient-level treatment response predictions.
- Explicit integration of intra-tumor heterogeneity into response and resistance modeling.
- A reusable computational framework bridging preclinical screens and clinical single-cell data.

## Datasets Used for Evaluation
- Large-scale preclinical drug-screen expression datasets.
  - Main content: matched expression and treatment-response data for model training.
  - Sample size: not specified in paper excerpt.
- Single-cell patient tumor transcriptomic cohorts from clinical studies.
  - Main content: scRNA-seq profiles linked to treatment outcomes across multiple cancer types.
  - Sample size: trial-specific counts not specified in paper excerpt.

## Experimental Procedure
- Build response models from matched bulk and single-cell preclinical expression data.
- Convert patient scRNA-seq tumor profiles into model-compatible features.
- Predict response at clone/cell-subpopulation resolution and aggregate to patient-level predictions.
- Validate predictions in independent clinical cohorts.
- Assess resistance dynamics in longitudinal or progression-associated contexts.

## Key Biology Insights
- Intra-tumor transcriptional heterogeneity carries actionable signal for treatment response prediction.
- Single-cell profiles can reveal resistant subpopulations that bulk methods may dilute.
- Resistance evolution can be tracked computationally from tumor-cell-state composition.

## Implications
- Supports clinical value of incorporating single-cell omics into precision oncology workflows.
- May improve treatment selection and early resistance-risk stratification.
- Encourages prospective clinical integration of sc-omics-guided decision support tools.
