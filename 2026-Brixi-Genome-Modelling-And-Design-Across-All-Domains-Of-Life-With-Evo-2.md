# Paper Summary

## Keywords
- Genomic foundation model
- Evo 2
- Long-context DNA language model
- Variant effect prediction
- BRCA1/BRCA2
- Mechanistic interpretability
- Sparse autoencoder (SAE)
- Genome-scale sequence generation
- Chromatin accessibility design
- OpenGenome2

## Main Idea
- Evo 2 is a fully open genomic foundation model (7B and 40B variants) trained on OpenGenome2 across bacteria, archaea, eukaryotes, and bacteriophages.
- The model combines broad phylogenetic coverage with long-context modeling (up to 1 million tokens) to support both:
- Zero-shot prediction tasks (mutation effects, clinical variants, gene essentiality, regulatory tasks).
- Generative design tasks (organelle/prokaryotic/eukaryotic sequence generation and controllable chromatin-accessibility design).
- Core claim: one sequence model can capture biologically meaningful structure across modalities (DNA, RNA, protein) and across domains of life, then be used for practical prediction and design workflows.

## Evidence Supporting the Main Idea
- Scale and training setup:
- 40B model trained on about 9.3T tokens (paper text also describes >8.8T nucleotides in OpenGenome2); 7B model trained on about 2.4T tokens.
- Two-stage training: short-context pretraining (8,192 tokens) + midtraining context extension to 1M tokens.
- Long-context quality:
- Needle-in-a-haystack synthetic test shows effective retrieval at 1M context.
- Zero-shot biology signals:
- Mutation likelihoods track known constraints: stronger penalties for nonsynonymous/frameshift/premature-stop mutations than synonymous changes; stronger effects in functional RNA loci (tRNA/rRNA, etc.).
- DMS benchmarking across prokaryotic proteins, eukaryotic proteins, and ncRNAs shows competitive zero-shot fitness correlation.
- Human variant prediction:
- ClinVar evaluation includes coding and noncoding SNVs and non-SNVs; Evo 2 is particularly strong on non-SNV classes.
- SpliceVarDB: Evo 2 40B/7B ranked top among unsupervised methods on exonic and intronic splice variants.
- BRCA1 saturation mutagenesis benchmark: strong coding and noncoding performance; supervised head on Evo 2 embeddings reaches AUROC 0.95 and AUPRC 0.88 on held-out BRCA1 SNVs.
- Regulatory benchmark (DART-eval): Evo 2 40B outperforms other unsupervised DNA language models but remains below dedicated supervised sequence-to-function predictors.
- Mechanistic interpretability (figure-backed):
- SAE features align with recognizable biology (prophage-associated regions, ORFs/intergenic/tRNA/rRNA, exon-intron boundaries, TF motif-like promoter features).
- Reported motif recovery from human promoter-enriched motifs is substantially higher than a classical motif-discovery baseline (HOMER).
- Generative evidence (figure-backed):
- Mitochondrial generation: >250 unique 16 kb sequences with expected gene category counts and preserved synteny patterns.
- Prokaryotic genome generation (M. genitalium scale, ~580 kb): ten long generations; nearly 70% of called genes with significant Pfam hits (vs 18% for referenced Evo 1 baseline in paper figure).
- Yeast chromosome-scale generation: produces gene/promoter/tRNA/intron-like annotations with improved realism versus prior model generation.
- Experimental design evidence:
- Inference-time-guided generation with Enformer+Borzoi achieved designed chromatin-accessibility patterns.
- Mouse mESC validation reports AUROCs around 0.92-0.95 for Morse-style designed patterns.
- Human cell-line tests (HEK293T/K562) show successful same-pattern and differential-pattern designs, including cases with >2-fold differential accessibility.

## Main Novelty
- Single open model spanning all domains of life at very large scale with 1M-token context.
- Joint demonstration of:
- Broad zero-shot predictive performance (including clinically relevant human variant tasks).
- Mechanistic interpretability at genome feature level via SAE analysis.
- Genome-scale generation and experimentally validated regulatory design.
- Open release of model weights, training/inference code, and OpenGenome2 dataset, enabling reproducibility and extension.

## Datasets Used for Evaluation
- OpenGenome2 (training dataset):
- Content: curated genomic sequences across bacteria, archaea, eukaryotes, bacteriophages.
- Scale: described as >8.8 trillion nucleotides (and 9.3T training tokens for Evo 2 40B).
- ClinVar:
- Content: human clinical variants (pathogenic/benign annotations).
- Sample sizes reported in figure text include:
- Coding: 8,889 SNVs and 1,236 non-SNVs.
- Noncoding: 34,761 SNVs and 3,894 non-SNVs.
- SpliceVarDB:
- Content: experimentally validated splice-altering variants.
- Sample sizes: exonic n=1,181; intronic n=3,769.
- BRCA1 saturation mutagenesis dataset:
- Content: functional effects of BRCA1 coding and noncoding variants.
- Sample sizes reported in figure text: coding SNVs n=2,077; noncoding SNVs n=1,125.
- BRCA2 functional variant dataset:
- Content: experimentally measured BRCA2 variant effects.
- Sample size: Not specified in paper excerpted figure text.
- DART-eval:
- Content: regulatory genomics benchmark tasks (including caQTL and dsQTL).
- Sample size: Not specified in paper excerpted figure text.
- Protein/RNA fitness benchmarks (DMS):
- Content: deep mutational scanning datasets.
- Coverage reported: nine prokaryotic protein datasets, six eukaryotic protein datasets, seven ncRNA datasets.
- Per-dataset sample sizes: Not specified in paper text excerpt.
- Chromatin accessibility experimental datasets:
- Content: ATAC-seq on designed sequences in mESC, HEK293T, K562.
- Sample sizes reported:
- HEK293T: 5 designs.
- K562: 31 designs.
- Differential two-cell-line setting: 24 designs evaluated for fold-change outcomes.

## Experimental Procedure
- Model construction and training:
- Build Evo 2 on StripedHyena 2 architecture (7B, 40B variants).
- Pretrain on weighted genomic windows at short context (8,192).
- Midtrain with staged context extension to 1M tokens.
- Exclude eukaryotic-infecting viral genomes for biosafety mitigation.
- Zero-shot prediction workflow:
- Score sequence likelihood before and after mutation.
- Use likelihood delta as variant/mutation effect score.
- Benchmark on coding/noncoding, SNV/non-SNV, splice, gene essentiality, and regulatory tasks.
- Supervised readout workflow (BRCA1 example):
- Extract Evo 2 embeddings across layers.
- Train lightweight classifier (ridge regression) on BRCA1 labels.
- Select best layer/window setup and evaluate on held-out test data.
- Mechanistic interpretability workflow:
- Train Batch-TopK SAE on Evo 2 internal activations.
- Perform contrastive feature search against genomic annotations.
- Validate discovered features against known motif/annotation resources.
- Genome-scale generation workflow:
- Prompt with organism-specific seed context.
- Autoregressively sample long sequences (mitochondrial/prokaryotic/eukaryotic scales).
- Annotate generated sequences (for example with MitoZ/Prodigal) and compare with natural-sequence statistics.
- Chromatin design workflow:
- Use Evo 2 as generator.
- Apply inference-time beam-search guidance using Enformer+Borzoi predicted accessibility against target peak patterns.
- Synthesize selected designs, integrate into mouse or human cells, and measure accessibility using ATAC-seq.
- Main achievements:
- Demonstrated broad zero-shot predictive generalization.
- Demonstrated interpretable latent biological features.
- Demonstrated experimental validation of designed chromatin-accessibility profiles.

## Key Biology Insights
- A single sequence likelihood model can recover known evolutionary/functional constraints across DNA, RNA, and proteins.
- Model-internal features capture biologically meaningful units from mobile elements to exon-intron boundaries and TF-motif-like promoter signals.
- Long-context genomic modeling supports generation that better preserves multi-scale genome statistics and structural coherence.
- Inference-time coupling of a general generator with task-specific predictors can produce experimentally measurable regulatory behavior.

## Implications
- Provides a reusable open foundation for genome interpretation and design, especially where labeled data are limited.
- Suggests a practical pipeline: general genomic FM for proposal generation + specialized predictors/assays for task-specific optimization.
- Enables faster iteration in variant interpretation and regulatory design, but does not yet guarantee fully functional/replication-competent genome synthesis.
- Highlights the importance of biosafety-oriented data curation and explicit risk evaluation in open biological model release.
