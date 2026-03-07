# Paper Summary

### Authors
- Wei-Shi Liu et al.

### Journal
- Nature Aging

### Publication Date
- 2024 (accepted October 17, 2024)

### DOI
- https://doi.org/10.1038/s43587-024-00753-6

## Keywords
- brain age gap (BAG)
- plasma proteomics
- multimodal MRI
- BCAN
- GDF15
- Mendelian randomization
- aging trajectories

## Main Idea
- The study integrates multimodal brain imaging and plasma proteomics to identify circulating protein biomarkers of brain aging.
- It uses brain age gap (BAG; predicted brain age minus chronological age) as the aging phenotype and links BAG to plasma proteins.
- The authors further propose that brain aging follows non-linear proteomic waves with distinct biological programs at different ages.

## Evidence Supporting the Main Idea
- Brain-age modeling used 10,949 healthy adults from UK Biobank with 1,705 imaging-derived phenotypes (IDPs); the final LASSO model retained 864 IDPs and achieved mean absolute error of 2.76 years in testing.
- Proteome-wide association in 4,696 participants across 2,922 proteins identified 13 proteins significantly associated with BAG after Bonferroni correction.
- Strongest BAG associations included BCAN (beta = -0.838, P = 2.63 x 10^-10) and GDF15 (beta = 0.825, P = 3.48 x 10^-11).
- Six proteins were supported in repeat-imaging validation analyses: LGALS4, ADGRG1, GDF15, BCAN, KLK6 and TIMP4.
- Clinical outcome analyses showed BCAN associated with lower risk of all-cause dementia (HR = 0.613), AD (HR = 0.625), and stroke (HR = 0.716), whereas GDF15 associated with higher risk of all-cause dementia (HR = 1.449), AD (HR = 1.340), vascular dementia (HR = 1.763), and stroke (HR = 1.540).
- Mendelian randomization analyses supported a causal association between BCAN and BAG, with additional associations to cortical/subcortical structural traits.
- Proteomic trajectory analyses detected three brain-age-related peaks at ages 57, 70, and 78, with distinct pathway enrichments across peaks.

## Main Novelty
- Combines a multimodal MRI-derived BAG framework with large-scale plasma proteomics in one analysis pipeline.
- Identifies both cross-sectional BAG biomarkers and dynamic age-wave proteomic transitions during brain aging.
- Provides convergent observational and genetic (MR) support for BCAN as a candidate biomarker with potential causal relevance.

## Datasets Used for Evaluation
- UK Biobank multimodal imaging cohort: 10,949 healthy adults.
  - Content: 1,705 IDPs across structural MRI, fMRI, diffusion MRI, and susceptibility-weighted imaging.
  - Role: train/test multimodal brain-age model and derive BAG.
- UK Biobank proteomics subset: 4,696 participants.
  - Content: 2,922 plasma proteins.
  - Role: proteome-wide association with BAG and downstream clinical linkage.
- Repeat imaging visit subset (from UK Biobank).
  - Content: follow-up imaging and proteomics overlap.
  - Role: nominal validation of primary BAG-associated proteins.
- External/auxiliary expression resources (single-cell/single-nucleus RNA-seq) used for cellular expression characterization of BAG-protein genes.

## Experimental Procedure
- Select healthy participants and imaging features; exclude major neuropsychiatric and systemic confounders per study criteria.
- Build multimodal brain-age predictor using LASSO on imaging-derived phenotypes; compute BAG for each participant.
- Run protein-wide association analysis between BAG and plasma proteins with multiple-testing correction.
- Validate top protein associations in repeat-imaging analyses.
- Perform functional enrichment and cell-type expression analyses for BAG-associated proteins.
- Test associations of BAG proteins with brain structure, cognition/movement/mental-health traits, and incident brain disorders.
- Conduct Mendelian randomization to evaluate potential causal links between key proteins and BAG-related outcomes.
- Model non-linear protein trajectories across brain age and identify statistically enriched age-wave peaks.

## Key Biology Insights
- Brain aging has a measurable plasma-proteomic signature that includes stress, regeneration, and inflammation-related proteins.
- BCAN (generally lower with higher BAG) and GDF15 (higher with higher BAG) emerge as key and biologically contrasted markers.
- Protein changes are not monotonic across aging; major wave-like transitions occur near brain ages 57, 70, and 78 years.
- Distinct biological processes are enriched at different aging waves, supporting phase-specific biology in brain aging progression.

## Implications
- Plasma proteomics can provide minimally invasive biomarkers for stratifying brain aging risk.
- BCAN and GDF15 are high-priority candidates for risk modeling and mechanistic follow-up in neurodegenerative and cerebrovascular aging.
- Non-linear aging waves suggest intervention windows may differ by biological stage rather than chronological age alone.
- The multimodal imaging + proteomics framework can be adapted for longitudinal risk prediction and precision prevention studies.
