# Genomic atlas of Bifidobacterium infantis and B. longum informs infant probiotic design

**DOI:** https://doi.org/10.1016/j.cell.2026.01.007

**Published:** Cell, March 19, 2026

**Authors:** Yan Shao (邵岩), Shuyi Wang (王舒意), Bonface M. Gichuki, ..., Judd L. Walson, James A. Berkley, Trevor D. Lawley

---

## Main Idea

This study presents a **global genomic atlas** of the *Bifidobacterium infantis-longum* (BIL) species complex, challenging the current classification by providing evidence that **B. infantis and B. longum are distinct, speciating species** rather than subspecies. The 4,098-genome catalog reveals dramatic **geographic stratification**: *B. infantis* dominates infant guts in low- and middle-income countries (LMICs) but is rare in Western, industrialized populations—raising critical concerns that current commercial probiotic strains (derived from high-income countries) may be ineffective for the populations that need them most.

## Main Novelty

1. **Taxonomic reclassification evidence**
   - Support for delineating *B. infantis* and *B. longum* as **distinct species**
   - Phylogenomic analysis shows BI is more ancestral, with larger genome and more pseudogenes
   - Evidence of recombination barrier between BI and BL complex
   - Proposal of new subspecies: *B. longum subsp. X* (BX, later named *B. longum subsp. leicesterensis*)

2. **Massive genomic expansion**
   - 4,098 high-quality genomes from 48 countries (2,875 MAGs + 1,223 isolates)
   - ~15-fold expansion over previous BIL studies
   - 12-17× increase in LMIC representation
   - 115 novel hybrid (Illumina-Nanopore) isolate genomes

3. **Extreme biogeographic stratification**
   - *B. infantis*: Highly prevalent in LMICs, scarce in Western industrialized populations
   - *B. longum*: Dominates in HICs; depleted in LMICs
   - BS subspecies: Infant-associated clade (*B. longum subsp. iuvenis*) in South Asia and Africa

4. **Geographically adapted metabolic specializations**
   - BI strains adapted to local diets: plant glycans (East Africa), breast milk substrates, urea/B vitamins
   - HMO-utilization genes highly conserved in BI globally
   - BX subspecies: Preferential starch metabolism

5. **Practical implications for probiotics**
   - Current commercial BI strains poorly represent global diversity
   - Probiotic-derived strains cluster together phylogenetically, distinct from natural circulating strains
   - Provides framework for **geographically tailored infant probiotics**

## Datasets

**Genomic Collection:**
- 4,098 genomes from 48 countries
  - MAGs: 2,875 (CheckM >90% complete, contamination <5%)
  - Isolates: 1,223 (115 newly sequenced, hybrid Illumina-Nanopore)
- Genome size: 2.40 Mb mean, GC content 59.9%
- Core genome: 825 genes
- Pangenome: 16,978 genes

**Cohort Sources:**
- **Baby Biome Study (BBS)**: UK healthy newborns (1,624 samples)
- **CHAIN Network**: 6 LMICs (1,278 hospitalized + 300 community children)
  - Countries: Bangladesh, Burkina Faso, Kenya, Malawi, Pakistan, Uganda

**Public Repositories:**
- ELGG (Early-Life Gut Genomes): ~32,000 early-life MAGs
- UHGG (Unified Human Gastrointestinal Genome): ~200,000 MAGs
- GTDB release 214, PATRIC, IMG

**Quality Control:**
- CheckM2 + GUNC for completeness/contamination/chimerism
- MDMcleaner for MAG decontamination
- Final dataset median completeness: 99.91% (MAGs), 99.98% (isolates)

## Experimental Procedure

1. **Metagenomic assembly and binning**
   - SPAdes → MEGAHIT assembly pipeline
   - MetaBAT2, MaxBin2, CONCOCT binning
   - metaWRAP refinement pipeline

2. **Phylogenomic analysis**
   - Core-genome alignment with Panaroo
   - Recombination filtering with fastGEAR
   - IQ-TREE maximum-likelihood phylogeny
   - FastANI for whole-genome ANI

3. **Population structure**
   - fastBAPS for substructure
   - PopPUNK for strain clustering
   - ClonalFrameML for recombination analysis

4. **Functional annotation**
   - KEGG orthologs with KOfam_scan
   - CAZyme analysis with run_dbCAN
   - eggNOG-mapper for COG IDs

5. **Metabolism-targeted analysis**
   - tBLASTx for HMO utilization loci
   - Manually curated metabolic pathway database
   - Pseudogene analysis with tBLASTn

6. **Strain cultivation**
   - Bifidobacterium Selective Media
  - Anaerobic cultivation
   - Hybrid Illumina-Nanopore sequencing with Dragonflye assembly

7. **Primer design**
   - MAFFT alignment
   - MFEprimer for specificity checking
   - Primer-BLAST validation

## Key Findings

### Taxonomy
| Clade | N | Classification | Key Features |
|-------|---|----------------|--------------|
| *B. infantis* (BI) | 1,395 | **Ancestral species** | Largest genome, most pseudogenes, recombination barrier |
| *B. longum subsp. longum* (BL) | 2,481 | Subspecies | Dominates HICs |
| *B. longum subsp. suis/suillum* (BS) | 165 | Subspecies | Infant-associated and animal clades |
| *B. longum subsp. X* (BX) | 57 | **Novel subspecies** | Starch metabolism, multi-niche distribution |

### ANI Distances (Species Delineation)
- BI ↔ BL complex: 95.8% (below species threshold)
- Within BL complex: 96.2% (above subspecies threshold)
- Intra-BI/BL/BS: >97% ANI
- Intra-BX: >99% ANI

### Geographic Distribution
- **BI in non-industrialized countries**: Highly prevalent, diverse
- **BI in industrialized countries**: Rarely detected
- **BL pattern**: Opposite distribution (HIC-enriched)
- **BS**: Weaning-associated in LMICs

### Metabolic Specializations
| Species | Enriched Functions | Depleted Functions |
|---------|-------------------|-------------------|
| BI | HMO utilization (GH95, GH29, GH33), urea, B vitamin synthesis | Plant glycan degradation |
| BL | Plant polysaccharides (GH127, GH27, GH51, GH43_26) | HMO utilization loci |
| BX | Starch degradation (GH13_14, GH13_32) | N-glycans |
| BS | Transitionary: mixed capabilities | - |

### Probiotic Strain Analysis
- Probiotic-derived BI strains cluster phylogenetically
- 25 of 27 probiotic BI genomes in 3 closely related PopPUNK strains
- Natural circulating BI far more diverse than commercial strains

### PCR Primers Designed
- Novel subspecies-specific markers for BI, BL, BS, BX
- >98% specificity, <1% in non-target genomes
- Validated in silico across all 4,098 genomes

## Sample and Metadata

| Cohort | Samples | Age Range | Countries |
|--------|---------|-----------|-----------|
| BBS | 1,624 | Neonates/infants | UK |
| CHAIN | 1,578 | Infants (admission/discharge) | BD, BF, KE, MW, PK, UG |
| Public | 4,730 early-life | Varied | Multinational |

## Key Implications

1. **Probiotics should be geographically matched**
   - Commercial strains from HIC donors may engraft poorly in LMIC infants
   - Locally isolated strains likely better adapted to local diets and microbiota

2. **Precision microbiome therapeutics**
   - Framework for selecting strains based on geographic origin
   - Consideration of local diet (breast milk composition, complementary foods)

3. **Regulatory considerations**
   - FDA warnings about BI products in preterm infants
   - Need for careful strain evaluation before commercialization

4. **Evolutionary biology**
   - BIL complex undergoing speciation via sympatric adaptation
   - Human lifestyle transitions (industrialization) driving ecological shifts

---

**Source:** Cell 2026;189:1-20; DOI: https://doi.org/10.1016/j.cell.2026.01.007

**Data Availability:**
- Genomes: NCBI (MAGs), SeqCode (BX subspecies registration)
- Code: https://github.com/sanger-pathogens/generate_mags
