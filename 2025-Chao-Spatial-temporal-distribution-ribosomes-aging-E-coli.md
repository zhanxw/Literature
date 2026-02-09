# Spatial and temporal distribution of ribosomes in single cells reveals aging differences between old and new daughters of Escherichia coli

**Authors:** Shi et al., Chao (primary investigator)
**Year:** 2025
**Journal:** eLife
**DOI:** https://elifesciences.org/articles/89543

---

## Main Idea

This study investigates the spatial and temporal distribution of ribosomes in single Escherichia coli cells to understand the mechanisms behind bacterial aging. The research demonstrates that **ribosomes are asymmetrically distributed between old and new daughter cells**, with new daughters containing higher ribosomal density than old daughters. This asymmetry originates from the mother cell before division and correlates with the previously observed differences in elongation rates and gene expression between daughter cells.

The key finding is that **ribosomal abundance is higher in new poles and new daughters**, matching patterns seen for expressed gene products. The authors propose that **competition for space between ribosomes and protein damage aggregates** at the cell poles explains the reduced ribosomal density in old daughters, providing a mechanistic explanation for bacterial aging.

---

## Main Novelty

1. **First quantitative analysis of ribosome distribution between old and new daughters**: Unlike previous studies that examined gene expression or damage aggregates, this work focuses on ribosomes as a more fundamental upstream factor affecting the entire proteome.

2. **Discovery of maternal origin of ribosomal asymmetry**: The study shows that ribosomal asymmetry is established in mother cells before division, with old mothers amplifying this asymmetry over time while new mothers maintain more symmetrical distributions.

3. **Space competition hypothesis**: The authors provide quantitative evidence that damage aggregates and ribosomes compete for space at cell poles, with aggregate volumes capable of displacing ribosomes enough to explain the observed elongation rate differences.

4. **Validation of S2-YFP reporter**: Extensive controls were performed to validate that the YFP-S2 ribosomal subunit fusion accurately reports ribosome distribution without artifacts.

5. **Partitioning of variance components**: The study decomposes phenotypic variance into stochastic (noise) and deterministic (asymmetry-driven) components, showing that ~40% of ribosomal density variance in daughters from old mothers is due to deterministic asymmetric partitioning.

---

## Main Datasets Used for Evaluation

1. **Time-lapse microscopy images**: Single-cell imaging of E. coli AFS55 strain with fluorescent YFP fused to ribosomal S2 subunit (rpsB gene), cultured on agarose pads.

2. **Cell lineage data**: Tracked old and new daughter pairs from old and new mothers through multiple generations, tracking:
   - Cell length and elongation rates
   - Ribosomal fluorescence density
   - Pole identity (old vs. new)

3. **Quantitative measurements**:
   - **Sample sizes**: 
     - 89 old/new daughter pairs from old mothers
     - 91 old/new daughter pairs from new mothers
   - Four length quartiles: NP (new pole), L2, L3, OP (old pole)
   - Four time quartiles: birth (B), T2, T3, division (D)

4. **Deconvolved fluorescence data**: Corrected for diffractional scatter from neighboring cells.

5. **Published aggregate size data**: From the literature, used for space competition modeling.

---

## Experimental Procedure

### 1. Bacterial Strain and Reporter
- Used E. coli strain **AFS55** with fluorescent YFP fused to the ribosomal S2 subunit (rpsB gene) as a ribosome reporter.
- Validated the S2-YFP construct through multiple control experiments to rule out fluorescence artifacts.

### 2. Cell Culture and Imaging
- Cultured cells on agarose pads
- Performed **time-lapse microscopy** tracking single cells through multiple divisions
- Applied **deconvolution** to correct fluorescence images for diffractional scatter

### 3. Cell Tracking and Classification
- Tracked individual cells to identify:
  - Old and new poles (based on division history)
  - Old and new mothers (mothers that were old vs. new daughters at birth)
  - Old and new daughters (receiving maternal old vs. new pole)
- Tracked lineages through at least two generations to determine polarity

### 4. Quantitative Analysis
- **Daughter ratios**: Calculated new/old daughter ribosome density ratios
- **Pole ratios**: Measured new pole half / old pole half fluorescence ratios
- **Length quartiles**: Divided cells into NP, L2, L3, OP regions
- **Time quartiles**: Tracked ribosome distribution from birth through division

### 5. Variance Decomposition
- Calculated total variance (VT), stochastic variance (VE), and deterministic variance (D²/4)
- Determined heritability of asymmetry: h² = (D²/4)/VT

### 6. Statistical Analysis
- Used paired t-tests for ratio comparisons
- Applied Bartlett's test for variance homogeneity
- Performed linear regression analyses for correlations
- Significance levels: *, **, *** for p < 0.05, 0.01, 0.001

---

## Key Findings

1. **Ribosomal asymmetry**: New daughters have 1.08-1.11× higher ribosome density than old daughters, with greater asymmetry from old mothers.

2. **Pole-specific distribution**: Ribosomes are denser in new poles versus old poles, matching patterns for expressed gene products.

3. **Maternal establishment**: Asymmetry is established in mothers before division - old mothers amplify asymmetry over time (birth to division), while new mothers maintain symmetry.

4. **Correlation with elongation**: Ribosome density and elongation rates are positively correlated (r = 0.387, p < 1×10⁻⁵ for old mothers; r = 0.233 for new mothers).

5. **Variance components**: Deterministic asymmetry accounts for 39.9% of ribosomal variance in daughters from old mothers vs. only 2.4% from new mothers.

6. **Space competition model**: Published aggregate sizes and ribosome-growth relationships support the hypothesis that damage aggregates displace ribosomes at old poles.

---

## Implications

This work supports a model where **bacterial aging results from the asymmetric inheritance of damage aggregates that compete with ribosomes for space at cell poles**. The mother cell's age (old vs. new) determines the degree of asymmetry passed to daughters, creating an epigenetic inheritance pattern of physiological aging in bacteria.

---

**Citation:** Shi et al., Chao. "Spatial and temporal distribution of ribosomes in single cells reveals aging differences between old and new daughters of Escherichia coli." *eLife* (2025). https://elifesciences.org/articles/89543