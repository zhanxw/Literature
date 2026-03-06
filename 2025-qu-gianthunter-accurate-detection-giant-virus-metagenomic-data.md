# Paper Summary

### Authors
- Fuchuan Qu
- Cheng Peng
- Jiaojiao Guan
- Donglin Wang
- Yanni Sun
- Jiayu Shang

### Journal
- Bioinformatics, ISMB/ECCB 2025 Supplement

### Publication Date
- 2025

### DOI
- https://doi.org/10.1093/bioinformatics/btaf239

## Keywords
- NCLDV
- giant viruses
- metagenomics
- reinforcement learning
- Monte Carlo tree search
- Transformer
- negative sampling
- viral detection

## Main Idea
- The paper presents `GiantHunter`, a tool for identifying nucleocytoplasmic large DNA viruses (NCLDVs) from metagenomic sequences.
- It combines reinforcement-learning-driven hard-negative selection (Monte Carlo tree search, MCTS) with a protein-cluster-based Transformer classifier to improve precision without sacrificing sensitivity.

## Evidence Supporting the Main Idea
- In abstract-level benchmarking, GiantHunter reports about 10% higher F1-score and about 90% lower computational cost than the second-best method.
- Training environment includes 227 complete NCLDV genomes (positive) and 5145 Caudoviricetes genomes (negative) from RefSeq.
- On time-split evaluation (train on pre-2018 genomes, test on post-2018 genomes), GiantHunter is reported to outperform VirSorter2 and ViralRecall across precision, recall, and F1.
- In ablation, MCTS-selected negatives outperform random sampling at equal training steps: precision 0.968 vs 0.956, recall 0.901 vs 0.877, F1 0.933 vs 0.915.
- Runtime benchmark reports about 8 min per 10 000 contigs for GiantHunter vs about 260 (ViralRecall) and 230 (VirSorter2) under the reported CPU setting.
- Yangtze case study: 60 June metagenomic datasets from six cities, with 201 153 candidate NCLDV contigs identified, 298 MAGs retained after completeness filtering (>50%), and 286 MAGs containing at least one NCLDV marker gene.

## Main Novelty
- Formulates NCLDV detection as an RL problem where MCTS navigates a taxonomy-structured negative space to prioritize hard negatives.
- Uses protein-cluster "sentence" representations with a Transformer to capture contextual patterns beyond marker-gene-only detection.
- Demonstrates practical ecological deployment in a riverine metagenomic case study linked to a major environmental perturbation (Three Gorges Dam).

## Datasets Used for Evaluation
- RefSeq-based training/evaluation genomes:
- Positives: 227 complete NCLDV genomes.
- Negatives: 5145 complete Caudoviricetes genomes.
- Test construction includes time-split and low-similarity (max inter-cluster similarity <=30%) settings with contig fragmentation (5-20 kb; OOD includes 3 kb in additional tests).
- OOD evaluation contigs:
- Archaea: 27 105
- Bacteria: 184 962
- Fungi: 46 090
- Plasmids: 48 109
- Real-world case study:
- 211 Yangtze samples collected Jan-Oct 2020; 60 June metagenomic datasets used for analysis across six cities.

## Experimental Procedure
- Build training corpus from RefSeq NCLDV and Caudoviricetes genomes.
- Fragment genomes into contigs for training/testing under time-split and low-similarity protocols.
- Use MCTS (selection, expansion, simulation, backpropagation) to iteratively sample hard negative taxa/contigs.
- Convert contigs to protein-cluster sequences and train Transformer classifier with cross-entropy loss.
- Compare against ViralRecall and VirSorter2 (including customized retrained/reference variants where applicable) using precision, recall, F1, and AUC-ROC.
- Benchmark inference runtime on 10 000 contigs.
- Apply model to Yangtze data: cross-sample assembly (MEGAHIT), candidate contig detection, binning (MetaBAT2), quality filtering (CheckV), marker-gene validation, and diversity analysis.

## Key Biology Insights
- NCLDV diversity varies across Yangtze cities and shows significant upstream/downstream shifts around the Three Gorges Dam.
- The observed diversity drop in the first downstream city and recovery farther downstream is consistent with hydrological/ecological perturbation effects on host communities.
- Many recovered MAGs expand known NCLDV diversity, and marker-only strategies may miss part of this diversity.

## Implications
- GiantHunter provides a faster and more accurate route for NCLDV discovery in large metagenomic projects.
- RL-guided hard-negative mining can improve classifier boundary quality in difficult biological sequence classification tasks.
- The framework may generalize to other hierarchical, highly imbalanced bioinformatics classification problems.
