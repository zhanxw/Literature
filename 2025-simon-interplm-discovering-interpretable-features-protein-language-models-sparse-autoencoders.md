# Paper Summary

### Authors
- Elana Simon
- James Zou

### Journal
- Nature Methods

### Publication Date
- 2025

### DOI
- https://doi.org/10.1038/s41592-025-02836-7

## Keywords
- protein language model
- interpretability
- sparse autoencoder
- ESM-2

## Main Idea
- The paper introduces InterPLM, a sparse-autoencoder framework to extract interpretable biological features from protein language model representations.

## Evidence Supporting the Main Idea
- Training SAEs on ESM-2 embeddings reveals thousands of interpretable features, including motifs, domains, and binding-site patterns.
- Reports that single neurons are less concept-aligned, consistent with superposition.
- Larger PLMs capture more interpretable concepts.
- Demonstrates practical utility for missing annotation detection and controllable sequence generation.

## Main Novelty
- A mechanistic interpretation pipeline for PLMs with automated LLM-based feature description/validation and downstream steering applications.

## Datasets Used for Evaluation
- ESM-2 embedding corpora from protein sequences.
- Functional/structural annotation resources for interpretability validation (exact sample sizes not specified in extracted text).

## Experimental Procedure
- Train sparse autoencoders on PLM latent embeddings.
- Quantify feature interpretability and concept alignment.
- Compare across model scales.
- Use automated LLM-assisted interpretation and validate against annotations.
- Apply features to annotation recovery and generation steering tasks.

## Key Biology Insights
- PLM representations encode reusable biological concepts in distributed, decomposable form.

## Implications
- Improves trust, diagnosis, and controllability of PLM-based protein science workflows.
