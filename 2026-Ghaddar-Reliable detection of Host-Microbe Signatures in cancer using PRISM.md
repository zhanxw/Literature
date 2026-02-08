# Reliable detection of Host-Microbe Signatures in cancer using PRISM

**Authors:** Bassel Ghaddar, Martin J. Blaser, Subhajyoti De  
**Journal:** Cancer Cell, 2026, 44, 1–12  
**DOI:** https://doi.org/10.1016/j.ccell.2026.01.007

---

## Main Idea

This paper introduces **PRISM (Precise Identification of Species of the Microbiome)**, a computational framework designed to reliably identify microorganisms from low-biomass human genomic sequencing data while distinguishing true microbial signals from contaminants and technical artifacts. The method addresses existing controversies in the cancer microbiome field by providing a rigorous, benchmarked approach to microbial detection. PRISM was applied to large-scale cancer genomics datasets (TCGA and CPTAC) to uncover microbial signatures in various tumor types and their associations with host molecular and clinical features.

---

## Main Novelty

PRISM introduces several key innovations:

1. **Two-Step Decontamination Strategy**: 
   - Step 1: Removal of technical artifacts (misclassified taxa) through multi-layered host-read depletion and BLAST-based alignment
   - Step 2: Machine learning-based classification of truly present vs. contaminant taxa using a gradient-boosted tree (XGBoost) model

2. **Comprehensive Misclassification Correction**: Addresses three major sources of taxonomic misclassification:
   - Insufficient host read removal
   - Multi-mapping reads (reads aligning to multiple taxa)
   - Vector and model organism contamination

3. **Multi-Stage Alignment Pipeline**:
   - Initial k-mer-based classification with Kraken2
   - Additional host removal using Minimap2 (against T2T-CHM13v2.0 human genome) and STAR
   - Taxa-representative subsampling and full-length BLAST alignment
   - Final realignment to refined taxa set

4. **40-Feature Machine Learning Model**: The XGBoost classifier uses features spanning:
   - Gene-product diversity (Shannon diversity metrics)
   - Read multi-mappability statistics
   - Kraken2 read count estimates
   - K-mer taxonomy proportions
   - Misclassification patterns

5. **Probabilistic Scoring**: Outputs a "PRISM score" (0-1 probability) for each taxon indicating likelihood of being truly present vs. contaminant

6. **Benchmarking on 230+ Datasets**: Extensive validation showing superior sensitivity (0.95) and specificity (0.97) compared to existing methods (Kraken2, MetaPhlAn, Metabuli, SAHMI)

---

## Datasets Used for Evaluation

### Training Datasets

| Dataset | Description | Size |
|---------|-------------|------|
| **CLID** | Cell-Line Infection Dataset: 515 RNA-seq experiments of human cell lines deliberately infected with 60 unique microbial species | 515 samples |
| **CLID-C** | In silico random combinations of CLID samples | 153 samples |
| **WGS** | In silico combinations of whole genome sequenced bacterial isolates + negative controls | 236 samples + 79 negative controls |
| **META** | Metatranscriptomic data from human gut, mouth, skin, and vagina | Grouped into 4 folds |
| **Total** | Combined training data | 833 samples, 416 true-positive species, 1,266 contaminants, 20,892 observed taxa |

### Validation Datasets

- **Negative Controls**: RNA-seq (uninfected cell lines), WGS, and 16S-rRNAseq reagent/blank samples (all taxa are contaminants)
- **Positive Controls**: 13 datasets with 5 common + 24 uncommon species validated as truly present via positive cultures from human infections
- **CDC-HAI**: 48 WGS samples from CDC Healthcare-Associated Infections dataset

### Cancer Application Datasets

| Dataset | Cancer Types | Sample Size |
|---------|--------------|-------------|
| **TCGA WGS** | 25 cancer types (colorectal, gastric, esophageal, cervical, head & neck, etc.) | 2,323 samples |
| **CPTAC3** | Brain, head & neck, kidney, lung, ovary, pancreas (ribosome-depleted RNA-seq) | Multi-omics data |
| **CPTAC2** | Breast, colon, ovary (poly-A selected RNA-seq) | 2,075 total sequencing runs |

---

## Experimental/Computational Procedure

### PRISM Algorithm Overview

The PRISM workflow consists of 6 main steps:

1. **Initial Microbial Surveillance with Kraken2**
   - Rapid k-mer-based classification using reference database with:
     - Complete microbial genomes (bacteria, fungi, viruses)
     - Human genomes (GRCh38, T2T-CHM13v2.0)
     - Common model organisms (mouse, fly, worm, zebrafish, rat, Arabidopsis)
     - Known vector sequences

2. **Additional Host-Read Depletion**
   - Minimap2 alignment against T2T human genome
   - STAR alignment for transcriptomic data to remove spliced/repetitive elements

3. **Taxon-Representative Subsampling and BLAST Alignment**
   - Construct subsampled dataset for computational efficiency
   - BLAST against core_nt database (human, model organisms, microbial genomes)
   - Identify uniquely identifiable taxa

4. **Full-Dataset BLAST to Refined Taxa**
   - Realign all microbial reads to refined taxa set
   - Filter alignments by quality, percent identity, and coverage
   - Map reads to GenBank annotations

5. **Machine Learning–Based Contamination Prediction**
   - Calculate 40 features for each taxon
   - XGBoost model predicts PRISM score (probability of being truly present)
   - Features capture gene-product diversity, multi-mappability, read abundance, taxonomic distribution, and misclassification patterns

6. **Output Generation**
   - Per-species read counts and PRISM scores
   - Read-level alignments with gene annotations
   - All taxonomic ranks and least common ancestor
   - Validated microbial reads in FASTA format

### Model Training

- **Algorithm**: XGBoost gradient-boosted decision tree
- **Parameters**: nrounds=40, eval_metric='auc', objective='binary:logistic'
- **Validation**: 5-fold cross-validation (stratified by project to prevent data leakage)
- **Performance**: Sensitivity = 0.95, Specificity = 0.97, PPV = 0.97, NPV = 0.94

### Cancer Data Analysis

1. **TCGA Analysis**:
   - Pre-processed with comprehensive host filtration (Minimap2 against GRCh38, T2T, 94 pangenomes)
   - Applied PRISM with default parameters
   - Filtering: CPM > 0.5, PRISM score > 0.1
   - Batch effect assessment using Aitchison distances and PERMANOVA

2. **CPTAC Analysis**:
   - Downloaded RNA-seq data from GDC for 7 cancer types
   - Analyzed reads unmapped to human reference
   - Applied PRISM pipeline with same filtering criteria
   - Correlated microbial detection with molecular data (protein, phosphoprotein, glycoprotein levels, mutation counts)

3. **Statistical Analyses**:
   - Wilcoxon testing for group comparisons
   - FDR correction for multiple hypotheses
   - Gene ontology analysis using clusterProfiler for glycoprotein associations

---

## Key Findings

- **High Microbial Detection**: Oral, GI tract, and urogenital tumors showed robust microbial signatures
- **Colorectal Cancer**: Dominated by anaerobic gut and oral commensals (Bacteroides fragilis, Fusobacterium nucleatum animalis, Prevotella species)
- **Pancreatic Cancer**: Microbial detection associated with altered host protein glycosylation pathways and greater smoking exposure
- **Technical Considerations**: Poly-A selection (PAS) significantly reduces microbial detection compared to ribosome-depleted (RD) sequencing; ribosome-depleted RNA-seq and WGS superior for microbial detection

---

## Code Availability

- **GitHub**: https://github.com/sjdlabgroup/PRISM
- **Zenodo**: https://doi.org/10.5281/zenodo.17613853
