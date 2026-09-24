# Paper Summary

### Authors

Lora Khatib, Renee Oles, Alejandra Ríos Hernández, Tyler Myers, Jianshu Zhao, Megha Kumar, Ana Laroya, Veronica Tolosa-Enguis, Nobuko Matsunami, Daisuke Suzuki, Nodoka Chiba, Katharine E. Gilbert, Promi Das, Jon G. Sanders, Lucas Patel, Nicole Litwin, Brent Nowinski, Amanda Birmingham, Sawyer Farmer, Caitriona Brennan, MacKenzie Bryant, Caitlin Tribelhorn, Karenina Sanders-Bodai, Charles Cowart, Oliver Nizet, Edgar A. Diaz, Patrick Veiga, Sudarshan A. Shetty, Jan Knol, Christophe Lay, Hana Koutnikova, Soline Chaumont, Julien Tap, Aurélie Cotillard, Muriel Derrien, Manolo Laiola, Antonio González, Armando R. Tovar, Nimbe Torres, Yolanda Sanz, Takuji Yamada, Daniel McDonald, Se Jin Song, Andrew Bartko, Rob Knight.

### Journal

Nature Communications

### Publication Date

2026-09-21

### DOI

[10.1038/s41467-026-77928-9](https://doi.org/10.1038/s41467-026-77928-9)

## Keywords

Gut microbiome; diet; metagenomics; shotgun sequencing; population variation; nutritional ecology; strain-level variation; precision nutrition.

## Main Idea

The Human Diets and Microbiome Initiative (THDMI) used harmonized recruitment, dietary assessment, metadata collection, and shotgun metagenomics in 1,976 adults from the United States, United Kingdom, Spain, Mexico, and Japan. Gut microbiome composition, dietary intake, and microbiome–diet relationships were strongly structured by country. Although some microbial responses to healthier eating were shared, most associations and strain-level genomic features were population-specific, limiting the validity of universal diet–microbiome biomarkers.

## Evidence Supporting the Main Idea

- After quality control, the cohort contained 1,976 participants and 3,375 microbial operational genomic units (OGUs): US 411, Mexico 397, UK 308, Spain 450, and Japan 410 (Fig. 1a–b).
- Principal-component analyses of microbiome profiles, metadata, nutrients, and foods showed strong country clustering (PERMANOVA P < 0.001). In microbiome profiles, country explained R² = 0.28, far more than cosmetics use (R² = 0.006), BMI (R² = 0.003), age (R² = 0.001), sex (R² = 0.002), or sequencing depth (R² = 0.005) (Fig. 1c–j).
- Sparse canonical correlation analysis found overall correlations between metagenomics and metadata (r = 0.70), nutrients (r = 0.83), and foods (r = 0.72), but the canonical structures were largely separated by country (Fig. 2).
- Healthy Eating Index (HEI-2015) scores differed across countries, with Spain highest and Japan lowest on average. No HEI component was associated with microbiome composition in all five countries; significant associations occurred mainly in the US, Mexico, and Spain (Fig. 3a–d).
- Elastic Net models trained within one country showed marked declines in RMSE and R² when evaluated in another country, demonstrating limited cross-country generalization of diet-quality predictors (Fig. 3e). Forty-eight OGUs, largely within Clostridia, were nevertheless associated with HEI across all five cohorts (Fig. 3g–h).
- Genome-resolved analyses retained 73 species-level bins with at least 30 MAGs. Thirty-five species showed significant country-structured Mash genomic distances after FDR correction, with differentiation involving Lachnospiraceae and Prevotella lineages and genes/pathways for carbohydrate, amino-acid, cofactor, vitamin, and energy metabolism (Fig. 4a–c).
- Dietary folate intake and microbial folate-biosynthesis enrichment showed an inverse country-level pattern: enrichment was observed in Spain and Mexico, where reported folate intake was lower, and depletion in Japan and the UK, where intake was higher (Fig. 4d–e). These are cross-sectional associations, not evidence of causality.

## Main Novelty

This is a large, single-study, five-country comparison designed to reduce the technical heterogeneity that complicates comparisons between independent microbiome cohorts. It combines harmonized diet and metadata with shotgun metagenomics, OGU-level association analyses, and genome-resolved strain/population analyses to show that both community composition and microbial genomic function vary with geographic and dietary context.

## Datasets Used for Evaluation

- **THDMI cohort:** 1,976 adult participants recruited through the Microsetta Initiative from the US (411), Mexico (397), UK (308), Spain (450), and Japan (410); 75% were female and mean age was 45.5 years. The cohort supplied fecal samples, self-reported metadata, country-specific FFQ data, nutrient and food-group intake, HEI-2015 scores, and shotgun metagenomic data for all analyses.
- **Qiita study #10317 / EBI PRJEB11419:** Quality-controlled metagenomic reads processed through Qiita and mapped to Web of Life release 2, yielding 3,375 OGUs for community-level analyses. The EBI accession is the sequencing-read repository, not a separate validation cohort.
- **Genome-resolved THDMI data:** MAGs assembled from the same metagenomic samples, filtered at ≥80% completeness and ≤10% contamination, clustered at ≥95% ANI, and restricted to 73 species bins with at least 30 MAGs for genomic differentiation analyses.
- **No independent external evaluation cohort was used.** Cross-country model transfer within THDMI was used to assess generalization.

## Experimental Procedure

- Recruit consenting adults through the Microsetta Initiative in five countries and collect fecal swabs, metadata, and country-appropriate validated FFQs.
- Harmonize FFQ-derived measurements to shared food codes, 60 food groups, and 30 nutrient variables; standardize intake by total calories and calculate HEI-2015 scores.
- Extract DNA from fecal samples, sequence normalized libraries on Illumina NovaSeq 6000, quality-control reads, remove human-aligned reads, and process samples through Qiita.
- Filter samples and features for metadata completeness, dietary data, sequencing quality, coverage, and read depth; retain 1,976 samples and 3,375 OGUs.
- Use PCA/RPCA, PERMANOVA, and covariate-adjusted sensitivity analyses to quantify country-level structure in microbiome, demographic, nutrient, and food data.
- Apply sparse canonical correlation analysis to link microbiome profiles with metadata, nutrients, and foods within and across countries.
- Test HEI–microbiome associations using PERMANOVA and BIRDMAn; train five-fold Elastic Net models within countries and evaluate them across countries.
- Assemble and dereplicate MAGs, calculate Mash genomic distances, test country structure with PERMANOVA, and use unitig-based pyseer analyses plus KEGG enrichment to characterize geographically structured genes and pathways.

## Key Biology Insights

- Geography and long-term dietary/lifestyle context were stronger determinants of microbiome community structure than the measured demographic and technical covariates in this cohort.
- Similar overall community composition does not imply similar diet–microbiome mechanisms: Spain and Mexico were relatively similar taxonomically, yet cross-country predictive transfer remained poor.
- A conserved subset of Clostridia-associated OGUs may respond to healthier eating across populations, but most HEI-associated OGUs were country-specific.
- Country-associated microbial genomic variation involved distributed metabolic functions rather than one universal pathway. Examples included folate biosynthesis, fatty-acid biosynthesis, carbohydrate metabolism, and amino-acid metabolism.
- Japanese B. subtilis OGUs were strongly associated with natto intake (r = 0.59, P = 4.9 × 10⁻³⁹), illustrating how culturally specific foods can relate to population-specific microbial features.
- In Bifidobacterium longum, galactose-metabolism genes were present in >70% of non-Mexican genomes but <10% of Mexican genomes; the authors discuss this in relation to lactose intolerance prevalence, while noting that the cross-sectional design cannot establish causality.

## Implications

The results support culturally informed, population-aware precision nutrition rather than assuming that one microbiome biomarker or dietary score will generalize globally. Future work should use more representative populations, improve cross-country nutrient harmonization, include stronger technical controls, and test proposed mechanisms in longitudinal and dietary-intervention studies. The authors caution that the cohort is enriched for women and relatively health-conscious participants, country-specific FFQs may introduce harmonization bias, mock-community controls were unavailable, and residual confounding and technical variation cannot be excluded.
