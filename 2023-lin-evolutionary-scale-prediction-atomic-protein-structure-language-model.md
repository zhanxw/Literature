# Paper Summary
### Authors
- Zeming Lin et al.

### Journal
- Science

### Publication Date
- 2023 (March 17, 2023)

### DOI
- Not specified in extracted text

## Keywords
- Protein structure prediction
- Language models
- ESM
- Metagenomics
- Structural biology

## Main Idea
- A large protein language model can directly infer atomic-level protein structures from sequence, enabling high-throughput structural prediction.

## Evidence Supporting the Main Idea
- Scaling to 15B parameters produced representations sufficient for atomic-resolution structure prediction.
- The approach is described as achieving about an order-of-magnitude speedup versus prior high-resolution pipelines.
- The model was used to build the ESM Metagenomic Atlas with predictions for over 617 million proteins, including over 225 million high-confidence structures.

## Main Novelty
- Direct sequence-to-atomic-structure inference from a large language model without relying on traditional MSA-heavy workflows.

## Datasets Used for Evaluation
- Evolutionary-scale protein sequence corpora for model training.
- Large metagenomic sequence collection for atlas-scale inference (>617 million sequences).
- Benchmark structure datasets: Not specified in extracted text.

## Experimental Procedure
- Train a large transformer language model on protein sequences.
- Decode atomic-level structure predictions from learned sequence representations.
- Benchmark quality/speed versus existing structure-prediction methods.
- Deploy model at metagenomic scale to generate a public structural atlas.

## Key Biology Insights
- Evolutionary sequence statistics alone encode rich 3D structural constraints that can be extracted by scaled language models.

## Implications
- Enables rapid structural characterization of previously unannotated proteins and accelerates hypothesis generation in protein science.
