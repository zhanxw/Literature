# Paper Summary

### Authors
- Felix Wong et al.

### Journal
- Nature

### Publication Date
- 2024

### DOI
- https://doi.org/10.1038/s41586-023-06887-8

## Keywords
- antibiotics
- explainable AI
- graph neural networks
- MRSA
- VRE

## Main Idea
- The paper introduces an explainable deep-learning workflow to discover antibiotic structural classes using substructure rationales.

## Evidence Supporting the Main Idea
- Measured antibiotic activity and cytotoxicity for 39,312 compounds.
- Applied model predictions to 12,076,365 compounds.
- Empirically tested 283 prioritized compounds.
- Identified a structural class active against MRSA and vancomycin-resistant enterococci, with reduced resistance liability and in vivo efficacy in mouse infection models.

## Main Novelty
- Connects black-box prediction to actionable chemical substructure explanations for antibiotic discovery.

## Datasets Used for Evaluation
- Training/evaluation measurements for 39,312 compounds.
- In silico screened set of 12,076,365 compounds.
- Experimental validation subset of 283 compounds.

## Experimental Procedure
- Train ensembles of graph neural networks on activity/toxicity labels.
- Use explainable graph algorithms to extract substructure rationales.
- Prioritize compounds with high predicted activity and low predicted toxicity.
- Validate in vitro and in mouse skin/thigh infection models.

## Key Biology Insights
- Structural motifs associated with selective antibacterial activity can be computationally identified and experimentally confirmed.

## Implications
- Supports interpretable ML-guided antibiotic class discovery at ultra-large chemical scale.
