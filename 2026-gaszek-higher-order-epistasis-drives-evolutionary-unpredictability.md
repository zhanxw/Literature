# Paper Summary

### Authors

Ilona Kamila Gaszek, Muhammed Sadik Yildiz, Zhaoxu Meng, Jose Alberto de la Paz, Sophia Maria Alvarez, Deniz Sezer, Faruck Morcos, Milo Lin, and Erdal Toprak.

### Journal

Nature Communications

### Publication Date

04 September 2026

### DOI

10.1038/s41467-026-77182-z

## Keywords

Antibiotic resistance; extended-spectrum β-lactamases (ESBLs); TEM-1 β-lactamase; epistasis; higher-order interactions; evolutionary predictability; directed evolution; *Escherichia coli*.

## Main Idea

The study asks why evolution toward ESBL-level resistance can be difficult to predict. The authors exhaustively measured a combinatorially complete library of 55,296 TEM-1 β-lactamase genotypes, containing combinations of 18 clinically observed mutations at 13 residues, under the native substrate ampicillin and the non-native substrate aztreonam. Ampicillin produced comparatively additive, funnel-like and predictable fitness landscapes, whereas aztreonam produced rugged landscapes dominated by higher-order epistasis. Thus, adaptation to a new antibiotic substrate can make both the effect of a mutation and the likely evolutionary trajectory strongly dependent on genetic background.

## Evidence Supporting the Main Idea

- More than 9,000,000 fitness measurements were obtained across the library under ampicillin and aztreonam selection.
- The graph-theoretic landscapes (Supplementary Fig. S4) show rapid funneling toward one or a few dominant peaks with ampicillin, but dozens to hundreds of competing peaks at intermediate aztreonam concentrations before peak pruning at the highest pressure.
- At the principal comparison, the additive component explained 0.35 of fitness variance for ampicillin at 781 µg/mL but only 0.10 for aztreonam at 36 µg/mL (Supplementary Figs. S9–S10), a 3.5-fold asymmetry.
- The effects of E104K, R164S, and E240K changed sign and magnitude across backgrounds carrying Q39K, A237T, or G238S (Supplementary Fig. S5). Under aztreonam, strong resistance emerged from particular combinations rather than from the individual mutations alone.
- LightGBM captured aztreonam fitness better than additive or pairwise-interaction models; pairwise Lasso closed approximately 35% of the additive-to-LightGBM error gap for aztreonam, compared with approximately 79% for ampicillin (Supplementary Fig. S13).
- AUC-fitness was experimentally grounded against monoculture IC50: Pearson correlation was 0.88 for ampicillin and 0.80 for aztreonam across representative variants (Supplementary Fig. S7).
- Direct-coupling analysis and latent generative landscapes indicated that high-performing ESBL variants preserve epistatic patterns seen in natural β-lactamases (abstract; Supplementary Fig. S6).

## Main Novelty

The work combines complete combinatorial mutational coverage, quantitative antibiotic-selection phenotyping, fitness-landscape graph analysis, epistasis decomposition, interpretable machine learning, and evolutionary sequence statistics in one TEM-1-to-ESBL system. This separates the increased unpredictability caused by non-native substrate adaptation from incomplete sampling of genotypes and provides a quantitative framework for identifying higher-order mutational rules.

## Datasets Used for Evaluation

- **TEM-1 combinatorial mutant library (TEM-1CML):** 55,296 genotypes formed from 18 clinical mutations across 13 TEM-1 residues, with wild-type residues retained at non-targeted positions. It was used for pooled fitness measurements and landscape reconstruction.
- **Pooled competition measurements:** More than 9 million fitness observations from three biological replicates across no-drug controls and dose series for ampicillin and aztreonam. The non-zero series included five ampicillin concentrations (3.1–781 µg/mL) and seven aztreonam concentrations (0.44–324 µg/mL). These data supported fitness, epistasis, graph, and machine-learning analyses.
- **Monoculture validation panel:** Representative TEM-1 variants (13 for ampicillin and 18 for aztreonam) measured by OD600 dose-response to compare IC50 with pooled AUC-fitness.
- **Clinical and natural β-lactamase sequences:** Clinical mutation frequencies guided the 13 library positions, while natural β-lactamase sequence statistics were used for direct-coupling and latent-landscape comparisons. The paper does not specify a single total sequence count in the available report.
- **Selected high-aztreonam variants:** Seven library variants selected at high aztreonam concentrations were sequenced and tested for MIC across a β-lactam panel, providing an independent resistance characterization.

## Experimental Procedure

- Compile clinically observed TEM-1 substitutions and choose 13 frequently mutated residues; construct the complete 55,296-genotype library.
- Express the library in *E. coli* NEB10B using a plasmid TEM-1 system, with wild-type and catalytically inactive controls.
- Perform pooled competition assays across ampicillin and aztreonam dose series, with three biological replicates and sequencing-based abundance measurements over time.
- Convert growth trajectories to AUC-fitness scores and validate this metric against monoculture IC50 measurements.
- Reconstruct genotype-fitness graphs by connecting single-mutation neighbors and grouping genotypes linked by fitness-neutral steps; quantify peaks and accessible routes across antibiotic concentrations.
- Decompose fitness variance into additive and higher-order epistatic components, and compare additive, pairwise, tree-based, and LightGBM predictors using held-out genotypes and mutation-stratified validation.
- Compare measured fitness with direct-coupling-analysis energies and latent generative landscapes derived from natural β-lactamase sequences.
- Sequence selected high-aztreonam variants and measure MICs against multiple β-lactams to confirm the resistance phenotype.

## Key Biology Insights

- TEM-1 is already close to optimal for its native substrate, ampicillin, so most library variants cluster near wild-type performance and evolutionary paths converge.
- Aztreonam exposes previously hidden combinations of mutations: resistance is often generated by cooperative interactions among mutations rather than by the sum of single-mutation effects.
- Higher-order interactions are concentration- and background-dependent. In particular, the E104K/R164S/E240K combination behaves differently on Q39K, A237T, and G238S backgrounds.
- The landscape can become more rugged at intermediate non-native-antibiotic pressure, with many competing local optima, and then collapse toward a global optimum at the highest pressure.
- The best ESBL-like variants are not arbitrary combinations; their mutational patterns retain statistical signatures found in naturally evolved β-lactamases.
- Predicting whether a genotype belongs to the very highest-resistance tail can remain accurate even when precise bulk fitness prediction is limited by measurement noise. For aztreonam, the top-1% classifier had AUROC 0.99, while the reported RMSD was 0.310 (Supplementary Fig. S15).

## Implications

Resistance forecasting should account for interaction order, genetic background, and antibiotic context rather than extrapolating from single mutations or pairwise effects alone. Complete or near-complete genotype measurements, combined with interpretable models and natural-sequence constraints, may help identify high-risk ESBL combinations before they spread. The framework could support surveillance, experimental prioritization, and assessment of which mutational routes are likely to emerge under new β-lactam selection pressures. It also cautions that evolutionary predictability under a native substrate may not transfer to adaptation toward a new drug.
