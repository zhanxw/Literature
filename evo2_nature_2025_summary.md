# Genome modelling and design across all domains of life with Evo 2

**Source**: [Nature](https://www.nature.com/articles/s41586-026-10176-5) | **Added**: 2025-03-04

## Abstract

Evo 2 is a biological foundation model trained on genomes spanning all domains of life (bacteria, archaea, eukarya, and bacteriophage). It uses a novel StripedHyena 2 architecture to model DNA sequences at scales from molecules to entire genomes, with context lengths up to 1 million base pairs. The model demonstrates capabilities for genome understanding, variant effect prediction, and de novo genome generation across diverse organisms.

## Key Points

- **Scale**: Two model versions (7B and 40B parameters) trained on 2.4T and 9.3T tokens respectively from the OpenGenome2 dataset (8.8+ trillion nucleotides)
- **Architecture**: StripedHyena 2 uses a multi-hybrid convolutional approach with three operator variants (short explicit, medium regularized, long implicit) allowing 3× speedup over Transformers at 1M context
- **Training**: Two-phase approach - initial pretraining at 8,192 tokens focusing on genic regions, then midtraining extending to 1M tokens
- **Biosafety**: Eukaryotic viruses deliberately excluded from training to prevent generation of human viral sequences
- **Generalization**: Works across DNA, RNA, and protein modalities; captures evolutionary constraints without task-specific fine-tuning

## Methodology

### Data
- OpenGenome2: Curated, non-redundant nucleotide sequences from all domains
- Excludes eukaryotic viruses (biosafety)
- Data weighting prioritizes functional genetic elements during pretraining

### Architecture
- StripedHyena 2 multi-hybrid design with input-dependent convolutions
- Combines attention layers with short, medium, and long-range convolutional operators
- Enables variable-distance interaction modeling per layer
- Achieves better loss scaling on DNA than Transformers or StripedHyena 1

### Training
- Phase 1: Pretrain at 8,192 token context learning functional elements
- Phase 2: Midtrain extending to 1M tokens via multi-stage context extension
- "Needle-in-a-haystack" evaluation confirms 1M token recall capability

## Findings

### Mutational Effect Prediction
- Learned constraint correlates with functional importance
- Captures translation initiation signals (Shine-Dalgarno in prokaryotes, Kozak in eukaryotes)
- Distinguishes genetic codes (standard vs. mycoplasma vs. ciliate)
- Zero-shot gene essentiality prediction competitive with Evo 1

### Human Variant Prediction
- **Coding SNVs**: Competitive performance (trails ESM-1b, GPN-MSA, outperforms ESM-2)
- **Coding non-SNVs**: **Best performance** (outperforms all methods including AlphaMissense)
- **Noncoding SNVs**: Ranks first among unsupervised models
- **Noncoding non-SNVs**: **Best performance** overall
- **Splice variants**: First among unsupervised models
- BRCA1/2 variant prediction: best zero-shot performance, supervised classifier achieves AUROC 0.95

### Feature Interpretability (SAEs)
Trained sparse autoencoders reveal interpretable features:
- Prophage/phage DNA and CRISPR spacer regions
- ORFs, intergenic regions, tRNAs, rRNAs
- Protein secondary structure (α-helices, β-sheets)
- Transcription factor binding motifs (70% recall vs 35% for HOMER)
- Exon/intron boundary detection
- Frameshift sensitivity

### Genome Generation
- **Mitochondrial DNA**: Generates correct numbers of CDS, tRNA, rRNA genes maintaining synteny
- **Prokaryotic genomes**: 70% of genes have significant Pfam hits (vs 18% for Evo 1)
- **Eukaryotic chromosomes**: Generates S. cerevisiae chromosome-length sequences with proper gene structure
- Poor performance on human viruses (intentionally excluded from training)

### Chromatin Design
- Demonstrated inference-time guidance using Enformer/Borzoi predictions
- Can design multi-kilobase sequences with specified chromatin accessibility patterns

## Notes

**Significance**: Evo 2 represents a milestone in biological sequence modeling by scaling genomic language models to eukaryotic genomes while maintaining prokaryotic capabilities. The model excels at variant effect prediction for non-SNVs (indels/duplications) where most models fail, and can generate plausible genome-scale sequences.

**Limitations**: 
- Evaluation metrics don't guarantee functional/replication-competent genomes
- Generated sequences lack some essential genes
- Underperforms on distal regulatory variants

**Tags**: #genomics #ai #foundation-model #evo2 #synthetic-biology #variant-prediction
