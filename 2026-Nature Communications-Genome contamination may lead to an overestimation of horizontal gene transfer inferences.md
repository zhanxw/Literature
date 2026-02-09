# Genome contamination may lead to an overestimation of horizontal gene transfer inferences

**Authors:** Nature Communications (Comment/Reply article - Arising from Ellabaan et al. 2021)  
**Journal:** Nature Communications  
**Year:** 2026  
**DOI:** 10.1038/s41467-026-69064-1  
**Article Type:** Matters Arising (Critical Commentary/Response)

---

## Main Idea

This paper is a critical re-assessment of a 2021 Nature Communications study by Ellabaan et al. that proposed an in silico approach to predict new bacterial hosts for antibiotic resistance genes (ARGs) using mobile genetic elements (MGEs). The authors identify that **genome contamination in the sequence data led to overestimation of horizontal gene transfer (HGT) events** in the original study. Out of 34 proposed transfer events in Ellabaan et al., **30 were incorrectly assigned due to contamination**, raising major concerns about the reliability of HGT prediction methods that do not adequately account for contamination.

## Main Novelty

1. **Systematic Contamination Analysis**: The authors examined all 182 SRA (Sequence Read Archive) runs used in Ellabaan et al.'s "confirmation" analysis and found widespread contamination:
   - **67% of Enterobacteriaceae** runs (41/62)
   - **91% of Staphylococcaceae** runs (88/97)  
   - **22% of Streptococcaceae** runs (5/23)

2. **Cross-Phylum Contamination Discovery**: 66% of contaminated genomes (88/134) harbored **cross-phylum contamination** (>5% abundance of two or three distinct phyla), with 28% showing taxonomic mismatch (>95% abundance of a different family than reported in SRA metadata).

3. **ARG Contig Validation**: Demonstrated that ARG-containing contigs consistently fell within the sequencing depth range of **contaminating bacteria** rather than the expected host taxa, strongly suggesting these ARGs originated from contaminants.

4. **IS1 Element Reanalysis**: Found that IS1 (a major contributor to predicted inter-phyla ARG dissemination) was incorrectly assigned in most non-Proteobacterial genomes, with only **4 Firmicutes families** showing confident HGT vs. 12 families claimed in original study.

5. **Limited Natural HGT Confirmation**: Only **4 ARGs** (erm(F), erm(T), tet(H), tet(W)) could be confirmed as natural horizontal transfers in Enterobacteriaceae out of 8 proposed; all Staphylococcaceae and Streptococcaceae "transfers" were artifacts.

## Main Datasets Used for Evaluation

1. **SRA Datasets**: All 182 SRA runs from Ellabaan et al.'s confirmation analysis:
   - 62 Enterobacteriaceae
   - 97 Staphylococcaceae  
   - 23 Streptococcaceae

2. **Reference Genomes**: Non-Proteobacterial reference genomes where IS1 was detected (19 genomes), with detailed analysis of 8 having raw read availability.

3. **Contamination Standards**: Established >5% abundance threshold for contamination detection using MetaPhlAn 4.0.2.

## Experimental Procedure

### Data Collection and Preprocessing
1. **SRA Download**: Retrieved all 182 SRA runs from NCBI Sequence Read Archive using accession numbers from original study
2. **Quality Filtering**: Applied Trimmomatic v0.38 with permissive parameters (LEADING:20, TRAILING:20, SLIDINGWINDOW:15:20)

### Taxonomic Analysis
1. **MetaPhlAn 4.0.2**: Performed taxonomic assignment of filtered reads using mpa_vJun23_CHOCOPhlAnSGB_202403 database
   - Excluded shared DNA materials (e.g., plasmids)
   - Identified expected vs. contaminating taxa

2. **Kraken v2.1.2**: Used for contig-level taxonomic assignment with bacteria database (February 2022)

### Assembly and ARG Detection
1. **De novo Assembly**: Assembled reads using same procedure as original study
2. **BLAST Analysis**: Queried assemblies for predicted ARGs and MGEs with **90% sequence similarity threshold**
3. **Contig Analysis**: Examined sequencing depth, length, and taxonomic assignment of ARG-bearing contigs

### Contamination Classification
- Standard contamination threshold: **>5% abundance** of quality-filtered reads assigned to different family than SRA metadata
- Cross-phylum contamination: >5% abundance of two/three distinct phyla
- Taxonomic mismatch: >95% abundance of family different from metadata

### IS1 Reanalysis
1. Sequencing depth analysis through raw read mapping
2. Taxonomic assignment of all contigs using Kraken 2
3. Comparison of IS1-carrying contig depth to expected taxon vs. contaminant ranges

## Key Findings

### Staphylococcaceae Case Study (ERR212931)
- Original claim: Inter-phyla transfer of catI (chloramphenicol resistance) + IS1 from Gammaproteobacteria
- **Reality Check**: ARG-MGE contig (19,125 bp) also contained tet(C), assigned to **Acinetobacter**
- Sequencing depth: **31×** (matching Acinetobacter contigs) vs. <15× for Staphylococcaceae contigs
- **Conclusion**: Contig originated from contaminating Acinetobacter, not Staphylococcus

### General Pattern
- In **all contaminated SRA runs**, ARG-carrying contigs matched sequencing depth of **contaminating bacteria**
- Even "contamination-free" assemblies (by standard threshold) sometimes contained contigs from contaminants sufficient for assembly

### Streptococcaceae Exception
- 13 contamination-free assemblies showed real chromosomal integration of ant(9)-Ia
- However, all isolates originated from **same clone with laboratory-inserted marker gene** (in vitro directed integration)
- Metadata confusion between natural vs. engineered HGT

### Revised IS1 Host Range
- **Original claim**: 3 phyla, 12 families with future inter-phylum dissemination via IS1
- **Corrected**: Only 4 Firmicutes families with confident HGT
- Most "detections" were from contamination or isolates with incorrect metadata

## Implications

1. **HGT Prediction Reliability**: Existing database contamination substantially affects reliability of computational HGT prediction methods

2. **Quality Control Standards**: Highlights the critical importance of:
   - Contamination screening (e.g., AllTheBacteria, FCS-GX)
   - Raw read re-analysis rather than relying solely on assembled genomes
   - Metadata verification for laboratory-modified strains

3. **Methodological Recommendations**:
   - Systematic contamination checking mandatory for HGT studies
   - Sequencing depth analysis of contigs to verify taxonomic origin
   - Use of long-read sequencing to reduce assembly artifacts (though multicopy plasmids from contaminants still a concern)

4. **Regulatory Implications**: Calls for careful contamination assessment in risk assessment frameworks for ARG dissemination

## Conclusion

This study demonstrates that contamination in public genome databases is a major confounding factor for HGT inference. The elegant approach proposed by Ellabaan et al. (using ARG-MGE pairs to predict future dissemination networks) is fundamentally limited by data quality issues. Without rigorous contamination controls, computational predictions of ARG spread may lead to **substantial overestimation of HGT events** and misidentification of bacterial hosts, ultimately undermining risk assessment efforts for antimicrobial resistance dissemination.

The key message: **"Genome contamination may lead to an overestimation of horizontal gene transfer inferences"** — robust quality control and contamination checking must be integrated into HGT prediction workflows.

---

*Keywords: horizontal gene transfer, genome contamination, antibiotic resistance genes, mobile genetic elements, sequence quality control, metagenomics, antimicrobial resistance*
