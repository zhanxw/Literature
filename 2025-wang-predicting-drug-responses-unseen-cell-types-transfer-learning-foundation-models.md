# Paper Summary
### Authors
- Yixuan Wang et al.

### Journal
- Nature Computational Science

### Publication Date
- 2025 (accepted September 3, 2025)

### DOI
- 10.1038/s43588-025-00887-6

## Keywords
- Drug repurposing
- Single-cell perturbation
- Foundation models
- Transfer learning
- Zero-shot prediction

## Main Idea
- The paper proposes CRISP, a foundation-model-based framework for predicting drug perturbation responses in unseen cell types at single-cell resolution.

## Evidence Supporting the Main Idea
- The authors report systematic evaluation under increasingly difficult scenarios, including unseen cell types and cross-platform transfer.
- CRISP is reported to outperform comparator methods in generalizability and predictive performance.
- A zero-shot case study predicts sorafenib effects from solid tumor data to chronic myeloid leukemia, with predicted CXCR4-related mechanisms aligned with independent evidence.

## Main Novelty
- Cell-type-specific transfer learning built on foundation models for perturbation prediction in previously unseen cellular contexts.

## Datasets Used for Evaluation
- Single-cell perturbation transcriptomic datasets for control-to-perturbed state prediction.
- Cross-platform and unseen-cell-type benchmark settings.
- Exact dataset names/sample sizes: Not specified in extracted text.

## Experimental Procedure
- Encode single-cell expression with foundation-model representations.
- Learn cell-type-specific mappings from control to perturbation response.
- Evaluate in-distribution and out-of-distribution settings (including zero-shot transfer).
- Assess downstream drug-repurposing hypotheses using pathway-level interpretation.

## Key Biology Insights
- Transferable expression representations can recover plausible therapeutic mechanisms in new disease-cell contexts.

## Implications
- Could reduce experimental burden for repurposing screens and improve precision-therapy hypothesis generation.
