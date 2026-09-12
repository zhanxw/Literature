# Paper Summary

### Authors

Lae-Guen Jang, Ji-Won Huh, Seolah Kim, Ji-Young Lee, Hee-Soo Hwang, Jaekyung Yoon, Hyeon Gwon Lee, Tae Il Kim, Yong Chan Lee, Sun Ha Jee, and Jihyun F. Kim.

### Journal

Cell Host & Microbe, volume 34, issue 9, pages 1829–1842.e5.

### Publication Date

20 August 2026 (electronic publication); 9 September 2026 (issue publication).

### DOI

[10.1016/j.chom.2026.07.007](https://doi.org/10.1016/j.chom.2026.07.007)

## Keywords

Gastrointestinal cancer; oral microbiome; fecal microbiome; mouth-to-feces microbial transmission; microbiome biomarker; metagenomics; machine learning; random forest; non-invasive diagnosis.

## Main Idea

The authors propose quantifying oral-to-fecal microbial transmission with a mouth-to-feces (MF) index. In the indexed abstract, MF transmission is elevated in gastrointestinal cancer and is associated with host metabolic and inflammatory indicators. Microbial taxa identified as transmitted were then used to build a classifier that could distinguish gastric or colorectal cancer from healthy controls, including when the model was trained using oral microbiome data alone.

## Evidence Supporting the Main Idea

- Paired oral and fecal microbiomes from 507 participants were analyzed across healthy controls, people with metabolic disorders, and patients with gastrointestinal cancers.
- The MF index showed increased mouth-to-gut transmission in cancer and a strong association with metabolic and inflammatory host indicators.
- A random-forest model based on transmitted taxa reportedly discriminated gastric/colorectal cancer from healthy controls across seven independent cohorts.
- The MF-based model reportedly had markedly higher sensitivity than fecal occult blood testing in the benchmark described by the abstract.
- The publisher’s full text and figures were inaccessible during preparation; exact effect sizes, confidence intervals, cohort-level sample sizes, and figure/table references are therefore not available in this record.

## Main Novelty

The study reframes oral and fecal microbiome comparison as a quantitative transmission signal rather than treating each body site only as an independent microbial community. It further links this transmission metric to a cross-cohort cancer diagnostic model and tests whether oral sampling alone can provide the relevant signal.

## Datasets Used for Evaluation

- **Paired oral–fecal microbiome cohort:** 507 participants comprising healthy controls and participants with metabolic disorders or gastrointestinal cancers. Role: discovery and evaluation of the MF transmission index and its associations with host indicators. The abstract does not specify exact group sizes, diagnoses within the cancer group, sequencing platform, or accession identifiers.
- **Seven independent cohorts:** Independent cohorts containing healthy controls and gastric/colorectal cancer cases, used to evaluate the random-forest classifier based on transmitted taxa. Per-cohort names, sample sizes, geographic composition, and train/test allocation are not specified in the indexed abstract.
- **Fecal occult blood test benchmark:** The conventional screening test used as a comparator for sensitivity. The abstract does not specify the comparator cohort, threshold, or numerical performance values.

## Experimental Procedure

- Collect paired oral and fecal microbiome samples from participants spanning healthy, metabolic-disorder, and gastrointestinal-cancer groups.
- Quantify microbial overlap and infer mouth-to-feces transmission to construct the MF index.
- Test whether MF transmission differs by disease status and whether it correlates with host metabolic and inflammatory indicators.
- Identify transmitted taxa and use them as features for a random-forest cancer classifier.
- Evaluate discrimination of gastric/colorectal cancer versus healthy controls across seven independent cohorts.
- Train/evaluate a model using oral microbiome data alone to assess whether oral sampling retains the diagnostic signal.
- Compare MF-based model sensitivity with fecal occult blood testing.

## Key Biology Insights

- Oral bacteria can appear at distal gastrointestinal sites in disease-associated patterns, supporting a measurable mouth-to-gut microbial transmission axis.
- Gastrointestinal cancer is associated with increased transmission signatures and with host metabolic/inflammatory changes.
- Disease-associated transmission signals may be detectable from the oral microbiome, potentially reflecting a non-invasive proxy for distal gastrointestinal pathology.

## Implications

MF profiling could support non-invasive gastrointestinal-cancer screening or risk stratification, particularly where oral sampling is easier than stool or endoscopic sampling. Clinical adoption would require independent prospective validation, standardized sampling and sequencing, assessment of confounding by diet, medication, age, geography, and comorbidity, and direct comparison with established screening pathways. The PubMed record notes that several authors are inventors of a patent application concerning MF-profile-based diagnostics, which is a relevant potential conflict of interest.

## Source and Evidence Limitation

This summary was prepared from the PubMed indexed record and Elsevier bibliographic metadata for the open-access article. Direct retrieval of the publisher full text was blocked during preparation, so details not present in the abstract are explicitly marked as unspecified rather than inferred.
