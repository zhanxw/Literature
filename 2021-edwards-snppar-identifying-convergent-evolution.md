# Paper Summary

### Authors
David J. Edwards, Sebastián Duchene, Bernard Pope, and Kathryn E. Holt.

### Journal
Microbial Genomics

### Publication Date
24 December 2021

### DOI
[10.1099/mgen.0.000694](https://doi.org/10.1099/mgen.0.000694)

## Keywords
SNPPar; homoplasy; convergent evolution; parallel evolution; ancestral state reconstruction; bacterial whole-genome sequencing; positive selection; antibiotic resistance; phylogenetics.

## Main Idea
SNPPar is a Python tool for efficiently detecting and annotating homoplasic SNPs in large microbial whole-genome alignments. It combines fast monophyly tests with ancestral state reconstruction (ASR), primarily through TreeTime, and reports mutation events on phylogenetic branches together with codon-, gene-, and mutation-type annotations. The output supports analysis of parallel, convergent, and revertant evolution as potential signatures of positive selection.

## Evidence Supporting the Main Idea
- In 120 simulated *Mycobacterium tuberculosis* alignments, SNPPar produced zero false positives in every test; 89% of tests had zero false negatives.
- Homoplasy-type classification was highly accurate, with fewer than 1% incorrect calls in the largest simulated dataset.
- A simulated alignment of approximately 64,000 genome-wide SNPs from 2,000 *M. tuberculosis* genomes was analyzed in about 23 minutes using approximately 2.6 GB RAM on a laptop.
- Only 1.25% of SNP sites required ASR in that benchmark; the ASR step took approximately 23 seconds and 0.4 GB RAM.
- Analysis of 68 *Elizabethkingia anophelis* outbreak genomes recovered the previously reported parallel nonsense mutation in *wzc*.
- Analysis of 114 *Burkholderia dolosa* isolates recovered all 20 previously reported homoplasic SNP sites, including parallel mutations in antibiotic-resistance-associated *gyrA*, *bla1*, and *rpl4*.
- In 2,000 *M. tuberculosis* genomes, SNPPar identified 2,879 homoplasic mutation events affecting 461 genes; highly ranked genes included known resistance targets *rpsL*, *katG*, *pncA*, *rpoB*, and *embB*.

## Main Novelty
SNPPar automates the complete path from large SNP alignments to interpretable mutation-event lists: it identifies homoplasies, distinguishes parallel/convergent/revertant events, maps them to branches, and annotates their coding effects. This goes beyond tools that only report homoplasic sites or perform ASR without detailed evolutionary interpretation.

## Datasets Used for Evaluation
- **Simulated *M. tuberculosis* datasets:** 120 alignments representing local and global sampling scenarios, used to measure sensitivity, specificity, and homoplasy-type classification.
- **Simulated large alignment:** approximately 64,000 SNPs from 2,000 *M. tuberculosis* genomes, used to benchmark runtime and memory.
- ***Elizabethkingia anophelis* outbreak dataset:** 369 SNP sites from 68 outbreak genomes, used to compare results with a previous homoplasy study.
- ***Burkholderia dolosa* dataset:** 511 SNPs from 114 serial isolates from chronically infected cystic-fibrosis patients, analyzed across three chromosomes to test recovery of within-host adaptive mutations.
- ***M. tuberculosis* Global L124 dataset:** 63,065 SNPs from 2,000 genomes plus an outgroup, used to explore gene-level signals of positive selection and computational performance.

## Experimental Procedure
- Provide SNPPar with a Newick phylogenetic tree, an annotated GenBank reference genome, and SNP alignment data.
- Sort SNPs using singleton and monophyly tests; send non-monophyletic, multiallelic, or selected ambiguous sites to ASR.
- Reconstruct ancestral states with TreeTime by default, with FastML available as an alternative.
- Collate mutation events, including genomic coordinate, ancestral-to-derived substitution, and affected tree branch.
- Annotate coding effects using inferred codons and reference-genome CDS features.
- Classify repeated events as parallel, convergent, divergent, or revertant homoplasy.
- Compare simulated calls with known truth and reanalyze published bacterial datasets.
- Summarize events at nucleotide, codon, and gene levels to identify candidate adaptive evolution and resistance-associated loci.

## Key Biology Insights
- Repeated independent mutations can reveal strong selection for clinically important traits such as antibiotic resistance and virulence.
- In *B. dolosa*, repeated nonsynonymous mutations in *gyrA*, *bla1*, and *rpl4* were consistent with selection during chronic infection and antibiotic exposure.
- In *M. tuberculosis*, homoplasies concentrated in established drug-resistance genes, including *katG* codon 315 and multiple sites in *pncA*.
- SNPPar distinguishes nucleotide-level convergence from codon- or gene-level convergence, allowing functionally similar outcomes produced by different mutations to be analyzed together.

## Implications
SNPPar enables reproducible, scalable surveillance of bacterial adaptive evolution from growing whole-genome datasets. It can support investigation of resistance emergence, pathogen adaptation, and vaccine or drug target durability. Results depend on the quality of the input alignment and phylogeny: recombination should be filtered when independent mutation events are the intended interpretation, phylogenetic uncertainty should be considered, and an outgroup is important because ASR cannot reliably resolve events immediately below the root. The code is available at [github.com/d-j-e/SNPPar](https://github.com/d-j-e/SNPPar), with validation data and protocols at [github.com/d-j-e/SNPPar_test](https://github.com/d-j-e/SNPPar_test).

**Source:** Edwards et al., *Microbial Genomics* (2021), DOI [10.1099/mgen.0.000694](https://doi.org/10.1099/mgen.0.000694). Full text: [PMC8767352](https://pmc.ncbi.nlm.nih.gov/articles/PMC8767352/).
