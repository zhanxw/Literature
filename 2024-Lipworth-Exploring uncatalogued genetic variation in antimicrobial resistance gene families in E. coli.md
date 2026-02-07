# Exploring uncatalogued genetic variation in antimicrobial resistance gene families in Escherichia coli: an observational analysis

**Authors:** S. Lipworth, Derrick Crook, A. S. Walker, T. Peto, N. Stoesser

**Publication:** Cell Genomics, 2024

**DOI:** https://doi.org/10.1016/S2666-5247(24)00152-6

---

## Main Idea

This study evaluates the performance of antimicrobial resistance (AMR) gene detection tools (specifically AMRFinder) and investigates the extent of uncatalogued genetic variation within known AMR gene families in *Escherichia coli*. The central premise is that current AMR gene databases rely on fuzzy matching (90% identity/coverage thresholds), potentially missing significant phenotypically important genetic variation. The authors systematically quantify how much resistance remains unexplained by existing databases and explore whether including 100% sequence-matched variants (including synonymous mutations) could improve genotype-to-phenotype predictions.

The study reveals that current database approaches fail FDA performance thresholds for clinical deployment, particularly for β-lactam–β-lactamase inhibitor combinations. Most significantly, the authors demonstrate that synonymous mutations - traditionally ignored in AMR detection because they don't change amino acid sequences - are associated with clinically relevant phenotypic differences in resistance.

---

## Main Novelty

1. **Empirical Reclassification of AMR Gene Families**: Rather than relying on existing nomenclature, the authors empirically redefined AMR-associated gene families using Mash distance matrices at 70% sequence similarity and ARGs at 100% nucleotide identity, revealing considerable diversity within "named" gene families.

2. **Quantification of Uncatalogued Variation**: Systematic cataloging of 1042 unique ARGs at 100% sequence identity, showing that only 51.5% (18,199 of 35,343) had perfect matches in the AMRFinder database.

3. **Synonymous Mutations Matter**: Demonstration that synonymous mutations (traditionally ignored) have phenotypic consequences. Two common uncatalogued *bla*TEM-1 alleles with only synonymous mutations showed significantly reduced resistance to amoxicillin-clavulanic acid (aOR 0.58) and piperacillin-tazobactam (aOR 0.50).

4. **Accumulation Curve Analysis**: Discovery that while new ARGs present multiple times plateau quickly, singleton ARGs continue to be discovered even after thousands of isolates, suggesting an enormous reservoir of unknown variation.

5. **International Validation**: Strong correlation (Spearman ρ = 0.76) between ARG frequencies in a local UK dataset and international datasets, indicating that locally discovered variants have global relevance.

---

## Main Datasets Used for Evaluation

### Primary Datasets (Five International Collections):
| BioProject | Location | Years | Description |
|------------|----------|-------|-------------|
| PRJEB11403 | Thailand | 2014-15 | Bloodstream infections (unpublished) |
| PRJEB23294 | Multiple (incl. Sweden) | 2018 | International collection |
| PRJEB32059 | Norway | 2002-17 | Longitudinal study |
| PRJEB4681 | UK | 2001-11 | National collection |
| PRJNA604975 | Oxfordshire, UK | 2008-18 | Local longitudinal study |

### Dataset Statistics:
- **Total *E. coli* isolates**: 9,001
- **Isolates with linked phenotype data**: 8,555
- **Study design**: Cross-sectional, retrospective secondary analysis

### Antibiotics Evaluated (7 drugs in 5 classes):
1. **Aminoglycosides**: Gentamicin
2. **β-lactams**: Ampicillin
3. **β-lactam-β-lactamase inhibitors**: Amoxicillin-clavulanic acid, Piperacillin-tazobactam
4. **Cephalosporins**: Ceftriaxone
5. **Quinolones**: Ciprofloxacin
6. **Folate pathway inhibitors**: Trimethoprim

### Reference Standards:
- **EUCAST breakpoints** for antimicrobial susceptibility testing
- **FDA guidance** for acceptable performance (major error <3%, very major error <7.5%)

---

## Experimental Procedure/Methodology

### 1. Data Acquisition & Assembly
- Raw reads downloaded from **European Nucleotide Archive**
- Assembly using **Shovill v1.0.4** (default settings)
- Quality control: Excluded assemblies <4 Mb or >6 Mb
- **Quast v5.2.0** for assembly metrics

### 2. AMR Gene Detection
- **AMRFinder v3.10.23** (database version 2022-12-19.1)
- Dual analysis with both:
  - Strict: 100% identity and coverage
  - Default: 90% identity, 50% coverage
- Focus on seven clinically relevant antibiotic classes

### 3. Empirical Gene Reclassification
- Used **Mash** to calculate Jaccard distances between gene sequences
- **AMR-associated gene families**: ≥70% sequence similarity (Mash threshold)
- **ARGs (antibiotic resistance genes)**: 100% nucleotide sequence identity
- Graph-based clustering using **igraph** (complete linkage)

### 4. Statistical Analysis
- **Performance metrics**: Sensitivity, specificity, PPV, NPV, major/very major errors
- **Accumulation curves**: R package **Micropan** (n.perm=100)
- **Correlation analysis**: Spearman coefficient for ARG frequency patterns
- **Association modeling**: Firth regression (logistf package) for *bla*TEM-1 variants
- **Software**: R version 4.3.1

### 5. Validation Strategies
- Sensitivity analysis for resistance prevalence effects
- Stratified analysis by study/source
- Investigation of potential confounding by population structure
- Assessment of sequencing/assembly error impact on singleton detection

---

## Key Findings

### Performance of AMRFinder Database:
- **Strict thresholds (100%)**: Failed FDA criteria for all 7 antibiotics
- **Default thresholds (90%/50%)**: Improved sensitivity at cost of specificity
- **Best performance**: Ciprofloxacin (unexplained resistance: 3.4%)
- **Worst performance**: Amoxicillin-clavulanic acid (unexplained resistance: 75.1%)

### ARG Distribution:
- **Total unique ARGs identified**: 1,042
- **Present ≥10 times**: 126 (12.1%)
- **Present 2-9 times**: 313 (30.0%)
- **Singletons**: 603 (57.9%)

### Significant Associations (*bla*TEM-1 variants):
- Uncatalogued alleles with synonymous mutations associated with reduced resistance
- Amoxicillin-clavulanic acid: aOR 0.58 (95% CI 0.35-0.95), p=0.031
- Piperacillin-tazobactam: aOR 0.50 (95% CI 0.29-0.82), p=0.005

---

## Funding
- National Institute for Health and Care Research (NIHR)
- Wellcome Trust
- UK Medical Research Council (MRC)

---

## Data Availability
- Sequencing data: European Nucleotide Archive (PRJEB11403, PRJEB23294, PRJEB32059, PRJEB4681, PRJNA604975)
- Analysis code: Available in binder environment (referenced in publication)

---

## Implications

The study highlights critical limitations in current AMR detection approaches:
1. **Clinical deployment**: Current fuzzy-matching approaches are insufficient for clinical use
2. **Database completeness**: Over half of detected ARGs lack perfect database matches
3. **Nucleotide-level matters**: Synonymous mutations can affect resistance phenotypes
4. **Future directions**: Need for comprehensive nucleotide-level databases and discovery of novel resistance mechanisms
