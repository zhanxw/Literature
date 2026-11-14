# Paper Summary

### Authors

Cale O. Seymour, Gertrude Ecklu-Mensah, Yesun Lee, Alexander R. Nicols, Wesley A. Cheng, Jaycee M. Jumarang, Carolyn Jennifer Marentes Ruiz, Jocelyn Navarro, Rafaella Navarro, Yamile Rodriguez-Angeles, David Durand, Sarah M. Allard, Zackary W. Taylor, Ruth G. De León, Theresa J. Ochoa, Jack A. Gilbert, and Pia S. Pannaraj. Seymour and Ecklu-Mensah contributed equally.

### Journal

Nature Communications, 17, 10783 (2026)

### Publication Date

15 October 2026

### DOI

[10.1038/s41467-026-78148-x](https://doi.org/10.1038/s41467-026-78148-x)

## Keywords

Rotavirus vaccine; RV1/Rotarix; infant gut microbiome; Klebsiella; Escherichia; metagenomics; fecal calprotectin; oral vaccine response; seroconversion; vaccine shedding.

## Main Idea

In a longitudinal cohort of infants from Panama, Peru, and the United States, the gut community established during the first month of life was associated with later response to the oral live-attenuated rotavirus vaccine (RV1). Klebsiella- and Escherichia-enriched communities, particularly a Klebsiella-dominant community type, were associated with lower RV1 seroconversion, lower post-vaccination rotavirus-specific IgA, and reduced shedding of vaccine-strain virus. The results support a model in which early-life pathobiont enrichment and associated inflammatory potential impede oral vaccine take.

## Evidence Supporting the Main Idea

- The study enrolled 337 healthy infants; 328 completed follow-up through 6 months. Among these, 153/328 (46.6%) met the definition of seroconversion: at least a threefold increase in serum rotavirus-specific IgA from month 2 to month 6.
- RV1 vaccine-strain shedding after the second dose was detected in 79/216 infants (36.6%). Shedding and seroconversion were not significantly associated with each other.
- Shotgun metagenomes from the first month (M1) showed that community composition correlated with seroconversion (Aitchison PERMANOVA, R² = 0.011, P = 0.030, N = 193); analogous associations were not detected at M2 or M4.
- In constrained ordination, Klebsiella was the largest contributor to the M1 ecological gradient associated with seroconversion, explaining 8.6% of total variation. Klebsiella michiganensis and Phytobacter ursingii were enriched in M1 non-responders.
- M1 non-responders had increased LPS-biosynthesis pathways and functional signatures involving aromatic-compound degradation and amino-acid catabolism. Species-level analysis linked LPS biosynthetic genes to Klebsiella in non-responders.
- Dirichlet-multinomial community typing identified a Klebsiella-dominant M1 gut type (cs-GCT3). After accounting for country, delivery mode, diet, and age, seroconverters had lower odds of belonging to cs-GCT3 and higher odds of belonging to a Klebsiella- and Escherichia-depleted type (cs-GCT6). The latter had 17/23 seroconverters (74.0%).
- Only 16% (7/42) of infants in the Klebsiella-dominant cs-GCT3 were seropositive after vaccination, and this group also showed reduced vaccine-strain shedding.
- Lower M1 fecal calprotectin was associated with later RV1 shedding (P = 0.043, N = 176). The Klebsiella- and Escherichia-enriched cs-GCT2 had higher M1 calprotectin than a demographically similar, pathobiont-depleted type, consistent with an inflammatory gut environment.
- LightGBM models did not generalize: held-out auROC did not exceed 50% at any sampling time point, indicating that the observed ecological associations did not yield a broadly predictive classifier.

## Main Novelty

The study integrates longitudinal shotgun metagenomics, rotavirus-specific IgA, vaccine-virus shedding, community-state modeling, and fecal calprotectin across three countries. It identifies a specific early-life microbial-metabolic-inflammatory axis centered on Klebsiella, rather than overall microbial richness, as a correlate of impaired oral RV1 response. It also shows that the association is strongest in the first month of life and is not captured by a globally generalizable microbiome-only prediction model.

## Datasets Used for Evaluation

- **Infant cohort:** 337 healthy mother-infant pairs recruited in Los Angeles, Lima, and Panama City; 328 infants completed the longitudinal clinical follow-up, and 324 contributed quality-filtered metagenome data. The cohort included 147 infants from Panama, 131 from Peru, and 50 from the U.S. It was used to assess clinical, dietary, demographic, and vaccine-response associations.
- **Stool metagenomes:** Samples were collected at 1–2 weeks (M1), 2 months (M2), and 4 months (M4). Of 816 collected samples, 765 from 324 infants passed the primary quality-filtering step (252 M1, 288 M2, 225 M4); the sequencing workflow ultimately reported 792 high-quality fecal samples for metagenomic processing. These data were used for taxonomic, functional, diversity, differential-abundance, and gut-community-type analyses.
- **Blood RV-IgA measurements:** Pre-vaccination samples at M2 and post-vaccination samples at M6 were available for 328 infants. They defined seroconversion and seropositivity outcomes.
- **Post-dose stool RV1 shedding:** Stool collected 1–14 days after the second dose at M4 was available for 216 infants and was tested by RT-qPCR for vaccine-strain RNA.
- **Fecal calprotectin:** Stool inflammation measurements were analyzed for approximately 250 infants at M1 and M2, with sample counts varying by analysis. These measurements evaluated the proposed inflammatory mechanism.

Raw shotgun metagenomic data are available under NCBI BioProject **PRJNA1404625**. Sample metadata and RV1-response variables are supplied as Supplementary Data; source data accompany the article. Analysis code is available at [PIA-LabUCSD/rv1-metagenomics-2025](https://github.com/PiaLabUCSD/rv1-metagenomics-2025).

## Experimental Procedure

- Recruit healthy term or near-term mother-infant pairs at four clinical sites in the U.S., Peru, and Panama; administer Rotarix at approximately 2 and 4 months.
- Collect clinical and feeding information throughout follow-up, plus stool at M1, M2, and M4 and blood before and after vaccination.
- Measure serum rotavirus-specific IgA by ELISA. Define seroconversion as a threefold or greater increase from M2 to M6; define seropositivity as RV-IgA above 20 AU/mL.
- Detect vaccine-strain RV1 RNA in M4 stool by RT-qPCR.
- Perform Illumina shotgun metagenomic sequencing, remove host and contaminant reads, and annotate organisms and functions using the Web of Life, MetaCyc, and KEGG resources.
- Quantify alpha and beta diversity and test associations with country, delivery mode, diet, age, and vaccine outcomes using mixed models and PERMANOVA on compositional distances.
- Use multivariable differential-abundance methods to identify taxa, pathways, LPS-related genes, and metabolic functions associated with response status.
- Cluster genus-level profiles at each visit with Dirichlet multinomial mixtures, then use multinomial regression to relate gut community types to vaccine outcomes while adjusting for clinical covariates.
- Quantify fecal calprotectin by ELISA as a marker of intestinal inflammation and relate it to microbial taxa, gut community types, and vaccine shedding.
- Train and evaluate LightGBM classifiers with cross-validation and held-out samples to test whether metagenomic composition could predict seroconversion.

## Key Biology Insights

- The timing of colonization mattered: M1 community structure, but not the contemporaneous M2 or M4 structure, was associated with later RV1 response.
- Klebsiella-rich configurations were associated with LPS-producing potential and higher inflammatory tone. This provides a plausible mechanistic link to impaired mucosal vaccine replication or immune priming, although the observational design does not establish causality.
- Reduced early-life inflammation was associated with vaccine-virus shedding, suggesting that inflammation may promote clearance of the live vaccine before effective immune memory develops.
- Bifidobacterium longum and B. saguini were inversely associated with M1 calprotectin, but Bifidobacterium enrichment itself did not define the highest-response community type. Exclusion of pro-inflammatory taxa may be more important than enrichment of a single presumed beneficial genus.
- Microbial richness increased with age but did not predict RV1 outcomes, emphasizing community configuration and functional capacity over simple diversity measures.

## Implications

The findings nominate the neonatal microbiome and gut inflammatory state as potentially modifiable determinants of oral rotavirus vaccine performance, especially in populations where oral vaccine effectiveness is reduced. Future work should test causality and evaluate age-appropriate interventions such as targeted prebiotics, synbiotics, or selective depletion of Klebsiella. The study does not support immediate clinical microbiome-based prediction or treatment: it was observational, used systemic IgA as a proxy for protection at the gut surface, did not measure maternal rotavirus-specific antibodies, and produced no generalizable microbiome-only classifier.

