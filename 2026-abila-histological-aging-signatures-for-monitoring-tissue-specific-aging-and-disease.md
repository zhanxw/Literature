# Paper Summary

### Authors

- Ernesto Abila, Iva Buljan, Yimin Zheng, Lisa Kleissl, Sigrid Klotz, Tamas Veres, Zhilong Weng, Maja Nackenhorst, Rizqah Kamies, Anja Michl, Safwen Kadri, Samir Moustafa, Wolfgang Hulla, Matthias Perkonigg, Mathias Drach, Philipp Tschandl, Barbara Sterniczky, Matthias Heinig, Laurens J. De Sadeleer, Wim Wuyts, Bart Vanaudenaerde, Laurens J. Ceulemans, Daniel D. Buchanan, Lochlan J. Fennell, Georg Stary, Yuri Tolkach, Adelheid Wöhrer, Herbert B. Schiller, and André F. Rendeiro

### Journal

- Nature Medicine (advance online publication)

### Publication Date

- August 14, 2026

### DOI

- https://doi.org/10.1038/s41591-026-04566-5

## Keywords

- biological aging
- tissue clocks
- whole-slide histopathology
- computational pathology
- deep learning
- organ-specific aging
- age acceleration
- GTEx
- telomere attrition
- transcriptomics
- DNA methylation clocks
- blood biomarkers
- chronic disease

## Main Idea

- The study uses deep features from histopathology whole-slide images to construct tissue-specific age predictors, or “tissue clocks,” across 40 human tissue types. The difference between image-predicted age and chronological age is treated as a tissue-specific age gap that may reflect structural aging beyond elapsed time.
- Histological age gaps correlate with shorter telomeres, subclinical pathology, comorbidity, and stronger age-related transcriptional dysregulation. Aging patterns vary within individuals, ranging from relatively resilient or systemic aging to acceleration concentrated in one or a few organs.
- By linking GTEx tissue histology to matched blood gene expression, the authors train models that infer tissue-specific age gaps from blood alone and associate those predictions with organ-relevant patterns in eight diseases. These cross-sectional associations demonstrate biomarker feasibility, not prospective prediction of disease onset or proof that the inferred gaps measure a causal aging process.

## Evidence Supporting the Main Idea

- **Large multi-organ resource (Figure 1a-c):** The analysis used 25,713 whole-slide images from 40 tissues in 29 organs across 983 GTEx donors aged 20-70 years (mean, 52.77 years). Images were decomposed into roughly 480 million multiscale tiles for feature extraction. The paper abstract reports 25,712 images, while the Results and Figure 1 report 25,713; this summary preserves that source discrepancy.
- **Tissue-clock performance (Figure 1d and Extended Data Figure 2):** Cross-validated tissue-specific Ridge models predicted chronological age with a mean absolute error of 4.88 years and mean coefficient of determination of 0.69 across tissues. Models trained on shuffled ages did not show comparable performance, although several tissues with fewer than 100 samples were underpowered and five low-sample tissues were excluded from downstream analyses.
- **Independent image validation (Figure 1h and Extended Data Figure 4):** GTEx-trained clocks generalized to external brain (n = 70), lung (n = 40), and skin (n = 185) cohorts, with tissue-matched Pearson correlations of 0.56, 0.76, and 0.46, respectively. Calibration slopes below 1 indicated regression-to-the-mean compression under domain shift, and performance varied by tissue and cohort.
- **Architecture robustness (Figure 1g and Extended Data Figure 3):** Six to seven conventional ImageNet vision architectures and 18 pathology foundation models retained age-related signal. Mean error across classical models was 8.67 years and across foundation models was 5.74 years, compared with 4.88 years for the study's primary clocks. Some foundation models may have seen GTEx images during pretraining, motivating the independent-cohort tests.
- **Biological and pathological associations:** In 6,197 samples with matched telomere measurements, image-derived biological age and age gaps were associated with shorter telomeres, especially in gastrointestinal tissues, kidney, prostate, pancreas and lung (Supplementary Figure 3). Larger gaps were also enriched for subclinical pathology, including muscle atrophy and arterial calcification, beyond associations with chronological age alone (Figure 1e,f and Supplementary Figure 4).
- **Interpretable morphology (Figure 2):** Vision-language queries over 150 histological terms identified recurrent increases in atrophy, microvascular rarefaction and fibrosis and reductions in epithelial or hyperplastic features with age. Tissue-specific examples included fat infiltration in skeletal muscle, uterine microvascular rarefaction and peripheral nerve atrophy. These are model-associated image patterns supported by visual examples, not longitudinal rates measured within the same people.
- **Comparison with epigenetic clocks (Extended Data Figures 7 and 8):** Among 987 GTEx samples from eight tissues, 28 DNA-methylation clocks and 19 histological clocks showed complementary associations: histology was more consistently related to comorbidity in colon and lung, whereas methylation performed comparably or better for telomere length. Their age gaps agreed poorly in GTEx (Pearson r = 0.09), but histological and methylation estimates correlated at r = 0.30-0.47 in the external lung cohort when assayed from the same tissue blocks.
- **Matched transcriptomics (Figure 3):** Analysis of 17,382 matched bulk RNA-sequencing samples found age-gap-associated genes that were largely tissue specific. Across organs, histological biological age was linked to stronger changes than chronological age in apoptosis, inflammation, p53 signaling, cellular senescence, hypoxia and TNF signaling, with stronger reductions in oxidative phosphorylation, peroxisome, adipogenesis, G2M checkpoint and mitotic-spindle signatures. The mean biological-versus-chronological change slope was 1.26.
- **Within-person heterogeneity (Figure 4a-c):** Donors exhibited patterns described as resilient, average, single-tissue, few-tissue and systemic aging. Among 303 donors with a markedly high gap in at least one tissue, some had coordinated acceleration across organs whereas others had a dominant heart, lung, stomach or other tissue signal.
- **Clinical and lifestyle associations (Figure 4d,e):** Exploratory models linked renal failure to accelerated aging in several nonrenal tissues, chronic respiratory disease to lung aging, type 2 diabetes to pancreatic aging, heart disease to adipose aging and long-term steroid use to spleen aging. Figure 4 explicitly reports no statistical testing for this association map, so these patterns should be treated as hypothesis generating rather than confirmed risk factors.
- **Blood-based model validation (Figure 5):** Tissue age-gap predictors trained from GTEx blood expression were applied to 1,205 independent ARCHS4 samples: 577 healthy controls and 628 samples spanning systemic lupus erythematosus (n = 202), Crohn's disease (n = 132), diabetes (n = 91), cystic fibrosis (n = 68), ulcerative colitis (n = 49), vasculitis (n = 43), Alzheimer's disease (n = 22) and stroke (n = 21).
- **Organ-disease specificity (Figure 5c-e):** Stroke showed its largest deviation in the brain; Crohn's disease was associated with higher gaps across esophagus, stomach, small intestine and colon; vasculitis with kidney, liver and heart; and Alzheimer's disease significantly only with the brain. Kidney and liver elevations also appeared across several conditions, which may reflect systemic disease, treatment effects or confounding rather than primary organ aging.
- **Screening signal (Supplementary Figure 15):** Thresholded blood-derived gaps yielded moderate-to-strong AUROCs and positive predictive values above 0.30 in several disease-organ comparisons. External cohorts lacked paired tissue histology, however, so absolute calibration of their predicted tissue gaps could not be verified.

## Main Novelty

- Builds a coordinated atlas of image-derived aging signatures across 40 tissue types from the same multi-organ donor cohort, enabling comparison of organ-specific and systemic patterns within individuals.
- Treats tissue architecture as an integrative aging phenotype and connects it to matched telomere length, pathology annotations, DNA methylation and bulk RNA expression rather than assessing image-age prediction in isolation.
- Uses vision-language models to translate otherwise opaque slide embeddings into interpretable histological concepts such as atrophy, fibrosis, epithelial loss and microvascular rarefaction.
- Bridges invasive tissue measurements to a minimally invasive assay by learning tissue-specific histological age gaps from matched blood transcriptomes and then testing disease associations in independent blood cohorts.
- Evaluates portability across independent histology cohorts, numerous image encoders and regression architectures and provides open source code and processed features.

## Datasets Used for Evaluation

- **GTEx discovery cohort:** 25,713 whole-slide histopathology images representing 40 tissue types and 29 organs from 983 postmortem donors. Donors were 20-70 years old and had demographic, lifestyle, clinical, cause-of-death, ischemic-time and pathologist-annotated subclinical pathology data. Images are public; protected phenotypes are available through dbGaP accession phs000424.v9.p2.
- **GTEx telomere subset:** 6,197 tissue samples, or 25.2% of the image collection, with telomere quantity measurements from matched tissues and individuals.
- **GTEx DNA-methylation subset:** 987 samples from eight tissues profiled with the approximately 850,000-site Illumina EPIC array. Twenty-eight methylation clocks and 19 histological clocks were compared on overlapping donors.
- **GTEx transcriptomic subset:** 17,382 bulk RNA-sequencing samples matched to tissue histology. These data were used to identify tissue-specific genes and pathways associated with chronological age and histological age gaps.
- **Independent histology cohorts:** Brain tissue from 70 postmortem donors aged 35-99 years in Innsbruck, skin biopsies from 185 donors in Vienna, and lung samples from 40 donors in Leuven. Different scanners, magnifications and preparation protocols created a realistic cross-institutional domain shift; the lung samples also had methylation data from the same blocks.
- **ARCHS4 blood-expression validation:** 1,205 peripheral-blood mononuclear-cell profiles from nine cohorts, comprising 577 healthy samples and the eight disease groups listed above. Source studies are available through the GEO accessions enumerated in the paper's Data Availability section.
- **Model-comparison resources:** Six classic ImageNet feature extractors, 18 pathology foundation models, graph neural networks, multiple vision-language models and a broad set of regularized, robust, kernel, ensemble and neural-network regressors were evaluated for robustness or interpretability.

## Experimental Procedure

1. Download GTEx hematoxylin-and-eosin whole-slide images and protected donor phenotypes, exact ages, clinical variables and gene-expression data; exclude three slides with incorrect tissue labels.
2. Segment foreground tissue, remove background and small artifacts, and tile each slide at matched centers using 224-, 448- and 896-pixel fields of view to represent progressively broader spatial contexts.
3. Fine-tune pretrained vision networks on a dataset balanced by tissue, sex and age bracket using tissue classification, then extract tile embeddings and mean-aggregate multiscale features into one vector per slide.
4. Train a separate Ridge regression clock for each tissue using fivefold GroupKFold cross-validation grouped by donor, with age as the target and sex, cohort and postmortem ischemic time as covariates. Correct residual age gaps for regression to the mean and compare with shuffled-age controls.
5. Test robustness with classical vision models, pathology foundation models, graph neural networks and alternative regression methods. Apply GTEx-trained clocks without refitting to external brain, lung and skin images and assess error, correlation, Bland-Altman agreement and calibration.
6. Relate tissue-clock outputs to matched telomere length, pathologist annotations and comorbidity burden. Compare histological gaps with estimates from 28 established DNA-methylation clocks where paired methylation data are available.
7. Use PLIP and CONCH vision-language models to calculate each slide's similarity to 150 curated histological and pathological terms; model term changes with age and visually inspect representative tissue regions.
8. Regress matched tissue RNA expression on chronological age and histological age gaps, adjust for sex, cohort and ischemic time, and perform MSigDB Hallmark, aging-signature and extracellular-matrix enrichment analyses.
9. Compare age gaps across tissues within each donor and fit sex- and tissue-specific Ridge models against recurrent demographic, lifestyle and medical variables. Treat this stage as an exploratory association map without formal hypothesis testing.
10. Filter GTEx blood expression to 11,859 sufficiently expressed genes, regress out chronological-age effects and train nested fivefold RidgeCV models to predict each tissue's histological age gap and the donor's mean systemic gap from blood.
11. Normalize independent ARCHS4 blood profiles and apply the fixed GTEx coefficients. Compare each disease group with healthy controls using t-tests with Benjamini-Hochberg correction; additionally threshold gaps at 1 year to calculate AUROC and positive predictive value.

## Key Biology Insights

- Common architectural correlates of aging included tissue atrophy, fibrosis, microvascular rarefaction and loss of epithelial features, while the prominence and morphology of these processes differed by organ.
- Histological age acceleration aligned with shorter telomeres and greater subclinical pathology, supporting tissue architecture as an integrative readout of accumulated cellular and extracellular changes. The modest or absent agreement with methylation age in GTEx indicates that morphology and epigenetic drift capture partly distinct dimensions of aging.
- Biological-age-associated transcription emphasized inflammation, apoptosis, p53 signaling, senescence and hypoxia, together with reduced mitochondrial metabolism and cell-cycle activity. Extracellular-matrix remodeling included broad collagen and basement-membrane reductions and relative increases in elastic-fiber components.
- Examples of tissue-specific expression included increased EYA4 in aging visceral adipose tissue and increased IGFBP2 in the adrenal gland. These are candidate biomarkers or correlates; the cross-sectional study does not show that they drive structural aging.
- Aging was heterogeneous both between organs and between people. Systemic patterns coexist with organ-dominant acceleration, consistent with a combination of shared systemic exposures and tissue-specific susceptibility.
- Disease-associated blood signatures often localized to biologically plausible organs, but elevations outside the primary disease site may represent systemic inflammation, complications, treatments, cohort effects or expression-composition differences rather than accelerated aging itself.

## Implications

- Histology obtained during routine clinical procedures could potentially provide an organ-specific aging measure alongside standard pathology, enabling retrospective studies of tissue resilience, disease burden and treatment response.
- Blood-based inference could make multi-organ monitoring less invasive, but it is not yet a validated diagnostic or prognostic test. The external blood cohorts contained prevalent disease and no paired tissue slides, so the study cannot establish calibration, temporal direction, incident-disease prediction or clinical utility.
- Cross-institutional deployment will require harmonization or domain adaptation for fixation, staining, scanner and sampling differences. External calibration slopes below 1 show that apparently strong correlations do not guarantee accurate individual age estimates.
- The operational “biological age” is a model prediction of chronological age from morphology; its residual is not a direct measure of aging rate. Associations may reflect disease, treatment, postmortem change, lifestyle or unmeasured confounding.
- Major limitations include the 1:2 female-to-male imbalance in GTEx, low sample sizes for several female reproductive tissues, variable postmortem autolysis, cross-sectional sampling, a restricted 20-70-year GTEx age range and lack of causal inference.
- Prospective longitudinal cohorts with prediagnostic blood, repeated measurements, paired tissue or orthogonal organ-function measures and subsequent clinical outcomes are needed before tissue-age gaps can support early detection or intervention monitoring.
- Public code, processed GTEx features, balanced image crops and open whole-slide analysis tools improve reproducibility and provide a foundation for testing tissue clocks in larger and more diverse cohorts.
