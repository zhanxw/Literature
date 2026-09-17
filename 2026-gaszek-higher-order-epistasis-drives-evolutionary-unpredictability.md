# Paper Summary

### Authors

Ilona Kamila Gaszek, Muhammed Sadik Yildiz, Zhaoxu Meng, Jose Alberto de la Paz, Sophia Maria Alvarez, Deniz Sezer, Faruck Morcos, Milo Lin, and Erdal Toprak.

### Journal

Nature Communications

### Publication Date

September 4, 2026

### DOI

10.1038/s41467-026-77182-z

### Source

Publisher page: https://www.nature.com/articles/s41467-026-77182-z

## Keywords

Antibiotic resistance; higher-order epistasis; evolutionary predictability; TEM-1 β-lactamase; ampicillin; aztreonam; fitness landscapes; combinatorial mutagenesis.

## Main Idea

The authors show that the predictability of antibiotic-resistance evolution depends strongly on the substrate being selected. Using a 55,296-genotype combinatorial TEM-1 library, they find that ampicillin produces a comparatively smooth, additive landscape, whereas the non-native substrate aztreonam produces concentration-dependent, rugged landscapes dominated by higher-order epistasis. Consequently, mutations that are beneficial in one genetic background or at one drug concentration can be neutral or deleterious in another.

## Evidence Supporting the Main Idea

- The TEM-1 combinatorial mutant library (TEM-1CML) targeted 13 sites chosen from frequent substitutions in non-redundant clinical β-lactamase sequences and contained 55,296 genotypes with relatively uniform amino-acid sampling at the targeted positions (Supplementary Fig. S1).
- Pooled competition assays measured AUC-Fitness for three biological replicates across five ampicillin concentrations (3.1–781 µg/mL) and seven aztreonam concentrations (0.44–324 µg/mL). AUC-Fitness was supported by monoculture IC50 measurements: Pearson r = 0.88 for ampicillin (13 variants) and r = 0.80 for aztreonam (18 variants), both p < 0.001 (Supplementary Fig. S7).
- At 781 µg/mL ampicillin, the additive component explained R² = 0.35 of fitness variance; at the reference 36 µg/mL aztreonam condition it explained only R² = 0.10. The 3.5-fold difference was robust at a second matched-stringency comparison (Supplementary Figs. S9–S10).
- The ampicillin landscape rapidly funnels toward one or a few dominant peaks, while aztreonam produces dozens to hundreds of competing peaks at intermediate concentrations before collapsing toward a single optimum at the highest pressure (Supplementary Fig. S4).
- In a focused three-mutation experiment, E104K, R164S, and E240K were strongly background-dependent under aztreonam: combinations on an R164S backbone produced high resistance, and the effect was further altered by Q39K, A237T, or G238S. The same combinations were neutral or deleterious under high ampicillin (Supplementary Fig. S5).
- A model-comparison analysis found that pairwise features closed about 79% of the additive-to-LightGBM error gap for ampicillin but only about 35% for aztreonam, indicating substantial structure beyond pairwise interactions under aztreonam (Supplementary Fig. S13).
- At 36 µg/mL aztreonam, the absence of a single global peak was robust to 30 of 31 tested neutrality cutoffs, supporting a genuine intermediate-concentration landscape feature rather than a cutoff artifact (Supplementary Fig. S18).

## Main Novelty

The study links antibiotic identity and selection concentration to the order and sign of epistatic interactions across a large, experimentally measured protein fitness landscape. It combines near-complete combinatorial coverage, dose-resolved competition measurements, graph-based landscape analysis, epistatic-order decomposition, and machine-learning validation to distinguish additive, pairwise, and higher-order contributions to resistance evolution.

## Datasets Used for Evaluation

- **TEM-1CML library:** 55,296 combinatorial TEM-1 genotypes spanning 13 targeted sites selected from clinical β-lactamase mutation frequencies. It was the primary dataset for fitness landscapes, epistasis decomposition, peak analysis, and prediction.
- **Pooled competition measurements:** Three biological replicates for each genotype across five ampicillin concentrations and seven aztreonam concentrations. These measurements supplied the AUC-Fitness values used in the main analyses.
- **Monoculture validation panel:** 13 representative variants for ampicillin and 18 for aztreonam, including wild type and clinically identified variants. Monoculture OD600 dose-response curves supplied IC50 values for validating pooled fitness.
- **Focused combinatorial panel:** All seven combinations of E104K, R164S, and E240K on the wild-type TEM-1 background and on Q39K, A237T, or G238S backgrounds. It was used to test background-specific higher-order epistasis.
- **Clinical sequence database:** Non-redundant clinical β-lactamase sequences retrieved from NCBI. Mutation frequencies from this resource guided selection of the 13 library positions; it was not an independent fitness-evaluation cohort.
- **Selected aztreonam variants:** Seven variants recovered under high aztreonam concentrations were sequenced and tested by MIC against a panel of β-lactams (Supplementary Fig. S2).

## Experimental Procedure

- Select 13 TEM-1 positions using the clinical mutational spectrum and construct the 55,296-member TEM-1CML library, alongside wild-type and catalytically inactive controls.
- Transform the library into NEB10B *E. coli* carrying the TEM-1 construct and perform pooled competition assays across graded ampicillin and aztreonam concentrations.
- Sequence barcode-linked populations at four time points in three biological replicates and calculate genotype-level AUC-Fitness values.
- Validate the pooled metric with monoculture OD600 dose-response measurements and IC50 estimates for representative variants; measure MICs for selected variants against additional β-lactams.
- Compare fitness landscapes by drug and concentration using graph-based neutral-network/peak analysis, epistatic-order variance decomposition, pairwise biochemical-epistasis maps, and additive, pairwise, tree, and LightGBM predictors.
- Test robustness with mutation-stratified holdouts, Hamming-distance holdouts, replicate agreement, and a neutrality-cutoff sensitivity analysis.

## Key Biology Insights

- Adaptation to the native substrate ampicillin is more constrained and predictable, whereas adaptation to the non-native substrate aztreonam exposes strong context dependence and higher-order interactions.
- The sign and magnitude of resistance mutations depend on both the surrounding genotype and the drug concentration; therefore, a mutation's clinical frequency or benefit in one assay does not imply a universal evolutionary advantage.
- Intermediate selection pressure can maximize the number of accessible competing peaks, creating evolutionary unpredictability even when the same protein and mutation set are considered.
- The study's principal quantitative reference condition for aztreonam (36 µg/mL) has relatively high measurement dispersion: the median coefficient of variation among viable genotypes is 37.7% across replicates, compared with 26.6% for 781 µg/mL ampicillin (Supplementary Table S2). This supports caution when interpreting small fitness differences.

## Implications

Resistance forecasting should model drug-specific and concentration-specific genetic interactions rather than rely only on single-mutation effects or pairwise maps. The data suggest that high-order epistasis is especially important when evolution moves toward activity on a non-native antibiotic substrate, which may make resistance trajectories harder to predict from existing clinical alleles. The study is focused on a TEM-1 library in *E. coli* and two antibiotics; extrapolation to other enzymes, organisms, and treatment environments requires additional experiments. The summary was prepared from the publisher's article metadata and supplementary figures/tables because the main-text PDF endpoint was not readable in the available retrieval session.
