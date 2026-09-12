# Paper Summary

### Authors

Zhi-Luo Deng, Nasim Safaei, and Alice Carolyn McHardy

### Journal

Cell

### Publication Date

September 11, 2026 (available online)

### DOI

10.1016/j.cell.2026.08.024

## Keywords

Metagenomics; taxonomic profiling; genome coverage; breadth of coverage; abundance estimation; expectation-maximization; low-biomass microbiomes; contamination detection; viruses

## Main Idea

Metax is a cross-domain taxonomic profiler that combines read-to-reference homology with genome-coverage evidence. It uses observed breadth/depth of coverage and chunk-level coverage to estimate whether a taxon is genuinely present, then applies an expectation-maximization (EM) procedure to resolve multi-mapped reads and refine abundance estimates. The coverage model is intended to suppress signals caused by contaminated or misassembled reference genomes, conserved genes/mobile elements, and reagent-derived (âkitomeâ) DNA.

## Evidence Supporting the Main Idea

- In a simulated, taxonomically diverse gut benchmark, Metax produced the lowest species-level BrayâCurtis distance (0.39 Â± 0.066) and abundance-rank error (0.21 Â± 0.019) among the compared profilers; it profiled a 2-Gb sample in about 8 minutes using 55 GB peak memory (Fig. 2a; Supplementary Fig. 1).
- In simulated ascites and cerebrospinal-fluid communities containing bacteria, fungi, and viruses, Metax maintained the strongest F-scores across 1,000 to 1,000,000 microbial reads and identified all simulated bacterial, fungal, and viral taxa. Its gains over competing methods were especially large at 1,000 reads per sample (Fig. 2bâe).
- On the CAMI II marine short- and long-read datasets, Metax achieved the best species-level abundance ranking, with an abundance-rank error of 0.12 (Fig. 3aâb).
- On 41 lower-respiratory-infection long-read samples, including 34 pathogen-positive and 7 pathogen-negative samples, Metax identified all 34 confirmed pathogens and produced no false positives: 100% sensitivity and specificity. The pathogen was ranked first in 30/34 positive samples (Fig. 3câd).
- In the CAMI II pathogen-detection sample, Metax identified Crimean-Congo hemorrhagic fever virus and ranked it first at 28.16% abundance; several competing methods missed it or assigned it very low abundance (Fig. 3e).
- Observed-to-expected breadth ratios (OEBRs) near 1 were almost exclusively associated with true positives in the marine benchmark, whereas extreme OEBRs were enriched for false positives (Fig. 4a).
- In a controlled contamination benchmark, human fragments of 1â16 kb were inserted into 50 bacterial/archaeal reference genomes. Metax detected the resulting contamination-driven false positives across host-read depths from 30,000 to 3 million and flagged them using coverage-based statistics (Fig. 4fâh).
- In 317 oral metagenomic samples from 91 subjects, Metax detected viral community differences between healthy sites and peri-implantitis sites. A random-forest classifier based on Metax profiles reached mean AUC 0.94 in 10-fold cross-validation and best-model AUC 0.98 (Fig. 6dâg).

## Main Novelty

The main novelty is the integration of genome-coverage likelihoods with homology-based profiling and EM abundance refinement in one cross-domain workflow. The resulting OEBR and chunk-coverage statistics provide interpretable evidence for distinguishing genuine taxa from localized or contaminated matches, including taxa from bacteria, archaea, fungi, eukaryotes, and viruses.

## Datasets Used for Evaluation

- **Simulated multi-domain gut metagenomes:** 10 communities derived from published human-gut abundance profiles, containing bacteria, archaea, fungi, viruses, and 0.002% human DNA. Reads were simulated with CAMISIM to evaluate cross-domain accuracy.
- **Simulated clinical communities:** 10 ascites and 10 cerebrospinal-fluid communities. Ascites communities contained 3 bacterial, 1 fungal, and 2 viral species; CSF communities contained 3 bacterial, 2 fungal, and 2 viral species. Four sequencing-depth conditions (1k, 10k, 100k, and 1M microbial reads) were generated with ART.
- **CAMI II marine benchmark:** short- and long-read metagenomes representing complex microbial communities, with approximately 5 Gb of each read type per sample; used for comparison with established profilers.
- **CAMI II pathogen-detection sample:** an Illumina RNA-sequencing sample from a patient with Crimean-Congo hemorrhagic fever; used to test pathogen detection and abundance ranking.
- **Lower-respiratory-infection (LRI) cohort:** 41 Oxford Nanopore long-read metagenomes, including 34 pathogen-positive and 7 pathogen-negative samples confirmed by culture and/or PCR; used to assess clinical sensitivity and specificity.
- **Controlled reference-contamination benchmark:** 50 complete bacterial/archaeal genomes, each spiked with human T2T fragments of 1, 2, 4, 8, or 16 kb; GIAB human whole-genome reads were subsampled to 30k, 100k, 300k, 1M, and 3M reads to test false-positive detection.
- **Tumor and control microbiome datasets:** published gut cohorts from Crohnâs disease and type 1 diabetes, plus melanoma/NSCLC-adenocarcinoma and pancreatic-cancer plasma datasets; used to compare genuine coverage patterns with reagent- and reference-derived signals.
- **Oral microbiome cohort:** 317 subgingival-plaque samples from 91 subjects: 77 healthy, 111 mucositis, and 129 peri-implantitis samples. Used for cross-domain profiling, differential abundance, and disease classification.

## Experimental Procedure

- Align reads to a taxonomically annotated reference genome database with Modular Aligner, filtering alignments by identity and mapped-length/fraction thresholds.
- Calculate genome breadth, depth, and chunk breadth of coverage; classify candidate species according to whether they have exclusively mapped reads.
- Assign uniquely mapped reads directly, use EM iterations to fractionally assign multi-mapped reads, and use lowest-common-ancestor assignment for reads without exclusive species matches.
- Estimate expected breadth from depth under a random-fragment-sampling model and calculate presence probabilities and OEBR-based evidence for artifactual signals.
- Filter final profiles using coverage-based statistics; the reported default filter removes taxa with OEBR < 0.75 or > 1.5 together with presence-test p < 1e-5.
- Compare Metax with marker-gene, k-mer, and alignment-based profilers using F-score, BrayâCurtis distance, weighted UniFrac error, diversity difference, and the newly defined abundance-rank error.
- Apply the method to contamination controls, clinical pathogen datasets, tumor datasets, and the oral cohort; use differential-abundance analysis and random-forest classification for the oral disease comparison.

## Key Biology Insights

- Genome coverage uniformity is a useful biological and technical diagnostic: genuine taxa tend to have coverage close to the breadth expected from their estimated depth, while localized matches often do not.
- Tumor plasma datasets showed coverage patterns inconsistent with genuine microbial communities. Across the analyzed tumor samples, the only confidently retained species was the spike-in control, supporting a major contribution from kitome and reference-assembly artifacts to apparent tumor-microbiome signals.
- The oral cohort contained detectable viral contributions, including Redondoviridae and Papillomaviridae. Redondoviridae occurred in 73/317 samples (23%), and Papillomaviridae in 54/317 (17%); viral and bacterial signatures contributed to separation of healthy and peri-implantitis sites.
- Metax recovered disease-associated oral signatures across multiple taxonomic domains, including established bacterial disease complexes, and detected a candidate oral protist signal together with putative host bacteria in a subset of samples.

## Implications

Metax provides an interpretable way to improve species-level profiling when sequencing is shallow, microbial biomass is low, host DNA dominates, or the community includes viruses and other non-bacterial taxa. Its coverage diagnostics can also help audit reference databases for contamination or misassembly. The findings support use in microbiome research and clinical metagenomics, but the reported performance depends on reference-database quality, alignment thresholds, and the simulated or cohort-specific evaluation designs. The authors identify strain-resolved models, RNA-virus profiling, and database-scale reference-quality screening as future directions.

Sources: Cell article, https://doi.org/10.1016/j.cell.2026.08.024; corresponding bioRxiv preprint, https://doi.org/10.64898/2025.12.04.692287; Metax implementation, https://github.com/hzi-bifo/Metax.
