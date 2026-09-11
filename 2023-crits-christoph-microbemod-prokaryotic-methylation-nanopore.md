# Paper Summary

### Authors

Alexander Crits-Christoph, Shinyoung Clair Kang, Henry H. Lee, and Nili Ostrov.

### Journal

bioRxiv (preprint; not peer reviewed in the supplied version).

### Publication Date

November 14, 2023.

### DOI

https://doi.org/10.1101/2023.11.13.566931

## Keywords

Nanopore sequencing; Oxford Nanopore R10.4.1; DNA methylation; 5mC; 6mA; restriction-modification systems; bacterial epigenetics; MicrobeMod.

## Main Idea

The authors introduce MicrobeMod, a Python toolkit with two complementary workflows for native Oxford Nanopore R10.4.1 data: `call_methylation` identifies active methylated DNA motifs, while `annotate_rm` detects restriction-modification (R-M) genes and operons. The approach uses only native-DNA sequencing reads, rather than a matched whole-genome-amplified control, and is designed to work at sequencing depths as low as 10×.

## Evidence Supporting the Main Idea

- In four reference *E. coli* datasets, MicrobeMod recovered known Dam (`GATC`), Dcm (`CCWGG`), EcoKI (`AACNNNNNNNGTGC`), M.Osp807II (`GACNNNGTC`), and M.XmnI (`GAANNNNTTC`) methylation motifs. The two heterologous methyltransferase motifs were recovered with more than 98% of genomic sites methylated and no reported false-positive motifs (Figure 2a).
- In the methylation-deficient *E. coli* control, only 13 6mA sites passed the stringent 90% methylation cutoff, corresponding to 0.00028% of the genome, and no 5mC sites were detected (Figure 2a–b).
- Downsampling the benchmark reads showed that more than 90% of expected motif sites remained identifiable at 10× coverage, although 6mA off-target/false-positive sites increased by about 2.5-fold compared with 100× coverage (Figure 2c–d).
- Across 9 strains with existing REBASE data, 15 of 19 detected 6mA motifs exactly matched REBASE and the remaining 4 were close matches (Figure 3a). Two robust 5mC motifs in *Cellulophaga lytica* were not reported by REBASE but agreed with homologous methyltransferase specificities.
- In 31 diverse prokaryotic strains, 93% had at least one detectable 5mC or 6mA motif; 87% had at least one 6mA motif and 29% had at least one 5mC motif (Figure 3b). The authors identified a mean of 2.1 motifs per strain.
- `annotate_rm` identified 26 Type I, 19 Type II, 16 Type IIG, 3 Type III, and 13 Type IV R-M systems across the 31 strains (Figure 4).

## Main Novelty

MicrobeMod integrates modified-base calling, sequence-motif discovery, and R-M gene annotation into one R10.4.1-compatible workflow. Its native-DNA-only design reduces the need for a separate amplified-DNA control, and the study provides publicly available POD5/FASTQ benchmark data spanning reference and previously unexplored prokaryotic methylomes.

## Datasets Used for Evaluation

- **Reference methylation benchmark:** Four *E. coli* datasets: K-12 MG1655, methylation-deficient DH10B (NEB C2925H), DH10B expressing M.XmnI, and DH10B expressing M.Osp807II. They contain known methyltransferase activities and were used to test motif recovery, specificity, and coverage sensitivity. Mean sequencing depths were 47×–304×.
- **Diverse prokaryotic collection:** 31 strains consisting of 30 bacterial strains and one archaeal strain, spanning Bacteroidota, Bacillota, Pseudomonadota, Actinomycetota, and Euryarchaeota. Genome sizes were 2–9.4 Mb and sequencing coverage was 12×–699×, with a mean of 40×. The collection was used to discover methylation motifs and annotate R-M systems.
- **REBASE comparison set:** Nine of the 31 strains had previously published PacBio methylation data in REBASE. These data were used for cross-platform motif concordance.
- **Public resources:** Raw POD5 and FASTQ files for the sequenced strains are provided through AWS S3; assemblies are deposited under NCBI BioProject PRJNA1037563. The toolkit is available at https://github.com/cultivarium/MicrobeMod.

## Experimental Procedure

- Extract genomic DNA from 35 microbial strains and sequence native DNA using Oxford Nanopore R10.4.1 flow cells and V14 chemistry.
- Basecall reads with Dorado models for 5mC and 6mA, assemble genomes with Flye, and optionally correct assemblies using 2×150-bp Illumina reads with PolyPolish.
- Map Dorado-modified reads to the corresponding assemblies and use Modkit to calculate per-site methylation frequencies.
- Filter sites by coverage and methylation fraction; extract 24-bp windows around highly methylated sites and use STREME to discover enriched motifs.
- Determine methylated positions and motif coverage, then report methylation type, motif frequency, and genomic coverage in `call_methylation` output.
- Predict genes with Prodigal, identify R-M-related proteins with DefenseFinder/PFAM HMMs and HMMER, group nearby genes into operons using a 10-gene window, and compare proteins with REBASE homologs using BLASTP.
- Benchmark against known *E. coli* methyltransferases, repeat analyses after downsampling to 10×–100× coverage, and compare 31-strain results with REBASE where available.

## Key Biology Insights

- Active methylation patterns can be recovered from native nanopore reads without a whole-genome-amplified control when suitable modified-base models are available.
- 6mA was more prevalent than 5mC in the sampled organisms, but 5mC appeared in 29% of strains—higher than the prevalence reported in the cited PacBio-based survey.
- Methylation motifs and R-M gene annotations provide complementary evidence for linking active methyltransferases to defense systems, although MicrobeMod does not automatically assign every observed motif to a specific R-M gene.
- The toolkit recovered both palindromic and non-palindromic, short and bipartite motifs, including motifs from non-model methyltransferases.

## Implications

MicrobeMod can help characterize methylomes and anticipate R-M barriers before genetic manipulation of non-model microbes. Its 10×-coverage performance may reduce sequencing requirements for initial strain screening. Important limitations are that the workflow cannot detect 4mC with the all-context models used here, some 6mA calls occurred near the *E. coli* Dcm 5mC motif, motif specificity can be over-resolved when motif occurrences are rare, and performance on genomes with more complex methylomes was not benchmarked.
