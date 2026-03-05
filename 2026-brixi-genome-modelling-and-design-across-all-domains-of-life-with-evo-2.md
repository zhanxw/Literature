# Paper Summary

## Keywords
Evo 2, genomic foundation model, OpenGenome2, long-context DNA language modeling, zero-shot variant effect prediction, BRCA1, mechanistic interpretability, genome generation, chromatin accessibility design

## Main Idea
The paper introduces Evo 2, a fully open biological foundation model trained on genome data spanning bacteria, archaea, eukaryotes, and bacteriophages, to unify prediction and sequence design tasks across DNA, RNA, proteins, and whole genomes. The model scales to 1 million-token context at single-nucleotide resolution and is used for zero-shot mutational effect prediction, human variant prioritization, interpretable feature discovery, and genome-scale sequence generation.

## Evidence Supporting the Main Idea
- Training scale and scope: Evo 2 includes 7B and 40B parameter models, with the 40B model trained on about 9.3 trillion tokens from the OpenGenome2 dataset (over 8.8 trillion nucleotides) across all domains of life.
- Long-context capability: a two-phase training strategy extends context from 8,192 tokens to 1 million tokens; a needle-in-a-haystack evaluation shows effective recall at 1 million-token context.
- Zero-shot biological constraint learning: likelihood shifts for start-codon and other mutations follow known biology; across many species, disruptive mutations (for example, frameshifts, premature stops) have larger negative likelihood impacts than synonymous changes.
- Experimental/benchmark support: Evo 2 likelihoods correlate with deep mutational scanning outcomes across prokaryotic and eukaryotic proteins and multiple ncRNA datasets; for held-out species exon classification, lightweight models on Evo 2 embeddings report AUROC values around 0.91-0.99.
- Human variant prediction: on ClinVar and related evaluations, Evo 2 40B is competitive on coding SNVs and performs strongly on noncoding and non-SNV settings; for BRCA1, supervised models built on Evo 2 embeddings reached high reported test performance (for example AUROC 0.95, AUPRC 0.88).
- Generative evidence: Evo 2 generates mitochondrial, prokaryotic, and eukaryotic genome-scale sequences with improved naturalness/coherence relative to prior baselines, and guided generation produced experimentally validated chromatin accessibility patterns with reported AUROC around 0.92-0.95 in ATAC-seq validations.

## Main Novelty
- A single open genomic foundation model covering all domains of life with single-base resolution and up to 1M-token context.
- Integration of large-scale cross-domain pretraining, long-context midtraining, and StripedHyena 2 architecture for efficient long-range genomic modeling.
- Demonstration that one model supports both predictive genomics (including noncoding clinical variants) and controllable genome design workflows with experimental validation.
- Open release of model parameters/code plus the OpenGenome2 dataset to support downstream research.

## Datasets Used for Evaluation
- OpenGenome2 (training corpus assembled from curated non-redundant sequences spanning bacteria, archaea, eukaryotes, and bacteriophages).
- Deep mutational scanning datasets for proteins and ncRNAs (rRNAs, tRNAs, ribozymes).
- Human clinical and functional variant benchmarks including ClinVar and SpliceVarDB.
- BRCA1 saturation mutagenesis variant effect data (coding and noncoding, including splice-related analyses).
- DART-eval tasks for regulatory variant effects (for example caQTL/dsQTL comparisons).
- Chromatin accessibility design validation datasets from ATAC-seq experiments in mESCs and human cell lines (HEK293T, K562).

## Experimental Procedure
1. Build OpenGenome2 by curating and deduplicating multi-domain genomic sequence data.
2. Train Evo 2 7B and 40B with phase 1 short-context pretraining (8,192 tokens) and phase 2 long-context midtraining up to 1,000,000 tokens.
3. Evaluate zero-shot mutational effect prediction by scoring likelihood changes under sequence perturbations across coding and noncoding contexts in multiple species.
4. Benchmark against existing models/conservation baselines on protein/RNA fitness datasets, exon classification, gene essentiality prediction, and human clinical variant tasks (including BRCA1).
5. Perform mechanistic interpretability analyses (for example sparse autoencoders) to identify biologically meaningful learned features.
6. Test generative performance by producing mitochondrial/prokaryotic/eukaryotic sequences and validating properties with annotation/structure analyses.
7. Run inference-time guided design for target chromatin accessibility profiles using external predictors, then experimentally validate selected designs with ATAC-seq.
