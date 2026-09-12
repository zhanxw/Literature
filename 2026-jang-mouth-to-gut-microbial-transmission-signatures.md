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

Gastrointestinal cancer; oral microbiome; fecal microbiome; mouth-to-feces microbial transmission; microbiome biomarker; 16S rRNA sequencing; metagenomics; machine learning; random forest; non-invasive diagnosis.

## Main Idea

The authors introduce a mouth-to-feces (MF) index that quantifies the proportion of gut microbial abundance represented by amplicon sequence variants (ASVs) shared exactly between paired oral and fecal samples. They show that oral-to-gut transmission is elevated in gastric cancer (GC) and colorectal cancer (CRC), is associated with clinical metabolic and inflammatory indicators, and carries cancer-specific information. Random-forest models built from MF-shared features classify GC and CRC across independent cohorts; oral MF-ASV features also perform strongly, suggesting a non-invasive diagnostic route based on oral samples.

## Evidence Supporting the Main Idea

- The Yonsei discovery cohort included 507 participants: 129 healthy controls, 215 participants with metabolic disorders, 77 GC patients, and 86 CRC patients. It produced 1,010 samples; 502 participants provided oral and fecal samples simultaneously.
- The MF index was higher in GC (3.63 ± 5.61) and CRC (3.09 ± 7.01) than in healthy controls (1.19 ± 2.44), approximately a 2.6–3.0-fold increase. The difference persisted across rarefaction thresholds of 5,000–20,000 reads.
- MF elevation was cancer-specific in the discovery analysis: the metabolic-disorder group did not differ significantly from healthy controls after adjustment.
- The highest MF quartile contained 44.2% of GC patients and 33.7% of CRC patients, compared with 14.3% of healthy controls.
- GC oral microbiota showed greater community alteration, whereas CRC showed stronger fecal microbiota alteration. Cancer-associated transmitted taxa included Streptococcus, Veillonella, Fusobacterium, Peptostreptococcus, Parvimonas, and related oral taxa.
- In the mouth–tumor–feces analysis, oral-to-tumor and tumor-to-feces transmission patterns differed between GC and CRC. MF and mouth-to-tumor indices were strongly correlated in GC (rho = 0.74) and CRC (rho = 0.54).
- MF-ASV models achieved internal AUCs of 0.66 (oral) and 0.73 (fecal) for GC, and 0.82 (oral and fecal) for CRC. Late-stage classification was generally stronger than early-stage classification.
- External validation used four paired cohorts: Zhang-GC, Russo-CRC, Uchino-CRC, and Zhang-CRC. Across CRC cohorts, oral, fecal, and binary-feature AUCs were 0.73–0.81, 0.71–0.81, and 0.76–0.85, respectively. GC AUCs were 0.62 (oral), 0.61 (fecal), and 0.65 (binary).
- In a Zhang-cohort subset with FOBT data (66 participants: 28 CRC cases and 38 controls), oral MF-ASV achieved AUC 0.969, sensitivity 0.929, and specificity 0.921; fecal MF-ASV achieved AUC 0.984, sensitivity 0.929, and specificity 0.947. FOBT had sensitivity 0.610 and specificity 1.000.
- The authors report that MF-based RF models outperformed logistic regression, support vector machines, XGBoost, and the MDeep microbiome deep-learning model for CRC classification.

## Main Novelty

The study turns oral–gut microbial overlap into a quantitative, ASV-level transmission metric instead of relying only on taxonomic abundance differences. It combines this metric with mouth–tumor–feces tracking and tests whether exact-sequence transmission signatures generalize across cohorts and remain useful when only oral samples are available.

## Datasets Used for Evaluation

- **Yonsei discovery cohort:** 507 Korean participants recruited between September 2021 and February 2024. Groups were healthy controls (n=129), metabolic disorders (n=215; metabolic syndrome, hypertension, hyperlipidemia, and type 2 diabetes), GC (n=77), and CRC (n=86). A total of 1,010 samples were processed, including 505 oral and 505 fecal samples. Role: discovery of disease-associated microbiome structure, MF-index construction, clinical association analyses, and model training.
- **Zhang GC/CRC cohort:** Matched oral, tumor/paratumor, and fecal samples used to compute mouth-to-tumor (MT), mouth-to-paratumor (MP), tumor-to-feces (TF), paratumor-to-feces (PF), and MF indices; also used for external classification and FOBT benchmarking. The FOBT subset contained 66 participants (28 CRC, 38 controls).
- **Russo CRC, Uchino CRC, and Zhang CRC cohorts:** External paired oral–fecal cohorts used for cross-cohort validation. The Uchino cohort used an incompatible V1–V2 region for ASV-level comparison in one analysis.
- **Additional unpaired external cohorts:** Flemer CRC, Wang CRC, Zackular CRC, and Zeller CRC datasets were used for broader unpaired validation. Across the Yonsei and seven published studies, the analysis comprised 2,031 samples from 1,096 individuals, including 1,547 paired oral–fecal samples.
- **Public data identifiers:** Yonsei: PRJNA1248208; Zeller: PRJEB6070; Zhang: PRJNA778008; Russo: PRJNA356414; Uchino: PRJDB11845; Flemer: PRJEB50080; Wang: PRJNA698923; Zackular: PRJNA389927.

## Experimental Procedure

- Recruit pre-treatment participants with healthy status, metabolic disorders, GC, or CRC; exclude participants with antibiotic exposure during the preceding three months.
- Collect oral rinse, fecal, and blood samples before cancer treatment and before diagnostic endoscopy or bowel preparation. Oral and fecal samples were collected on the same morning when possible.
- Extract DNA using Fast DNA SPIN and SPINeasy DNA kits. Amplify the V3–V4 region of the 16S rRNA gene with primers 337F/806R and sequence on Illumina MiSeq (2 × 300 bp).
- Process reads with QIIME2 2021.02 and DADA2; assign taxonomy using a V3–V4 Greengenes2 naïve Bayes classifier. Rarefy ASV tables to 15,000 reads per sample.
- Calculate alpha diversity, Bray–Curtis beta diversity, PCoA, PERMANOVA, and differential abundance using LEfSe and MaAsLin2.
- Define MF as the ratio of abundance from ASVs with 100% sequence identity shared between matched oral and fecal samples to total fecal ASV abundance.
- Apply the same exact-ASV matching principle to MT, MP, TF, and PF indices in the Zhang mouth–tumor–feces dataset.
- Build total, MF-shared, and total-minus-MF feature tables. Train random-forest models using abundance and binary presence/absence representations, with feature matching across external cohorts by 100% sequence identity using VSEARCH.
- Compare model performance across taxonomic resolutions and against logistic regression, support vector machines, XGBoost, MDeep, and FOBT.
- Evaluate performance with ROC/AUC analyses, bootstrap confidence intervals, Kruskal–Wallis and Dunn tests for model comparisons, and corrected p values. Analyses used R 4.1.0 and microbiome-analysis packages including vegan, tidyverse, rstatix, and ggpubr.

## Key Biology Insights

- GI cancer weakens the normal compartmentalization between oral and gut microbiomes, with disease-specific differences in how oral bacteria reach feces or tumor-associated sites.
- MF transmission is not simply a generic disease signal: its magnitude and taxonomic composition differ between metabolic disorders, GC, and CRC.
- CRC-associated transmitted organisms included F. nucleatum, P. stomatis, P. micra, P. intermedia, and other taxa previously implicated in CRC biology.
- In GC, oral-to-tumor transmission was relatively prominent; in CRC, a larger fraction of tumor-transmitted organisms continued to feces.
- Exact ASV-level matching was essential for oral classification: taxon-level oral models performed poorly (weighted mean AUC 0.42–0.47), whereas ASV-based oral models reached AUCs of 0.57–0.80 across external cohorts.
- Associations between transmitted taxa and cholesterol, LDL, HbA1c, thyroid hormones, blood-cell counts, blood pressure, triglycerides, and other indicators support a connection between transmission and host metabolic or inflammatory state, but do not establish causality.

## Implications

MF profiling could provide a non-invasive screening or risk-stratification framework, with oral sampling potentially improving compliance compared with stool testing. The results are promising but not yet sufficient for clinical deployment: the study was observational, did not perform a prospective sample-size calculation, and did not establish whether transmitted microbes cause cancer or merely reflect a cancer-associated environment.

Important limitations include the Korean single-population discovery cohort, heterogeneous external sequencing regions and platforms, limited strain-level resolution of 16S data, self-collection and handling variability, absence of extraction blanks and mock-community controls, and incomplete participant-level metadata for external datasets. The authors also note that several investigators are inventors of a patent application for MF-profile-based diagnostics.

## Data and Code Availability

Sequencing data are available under the repositories listed above. Analysis code is available at [MF-GI-cancer-classifier](https://github.com/Lae-Guen/MF-GI-cancer-classifier) and archived at Zenodo under [10.5281/zenodo.20302778](https://doi.org/10.5281/zenodo.20302778).
