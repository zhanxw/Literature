---
title: "Precise DNA base editing using AlphaFold3-based contact modelling"
url: "https://www.nature.com/articles/s41586-026-10794-z"
date: 2026-08-01T18:52:43.604650
tags:
  - genome-editing
  - ai
  - alphafold3
  - biotech
---

# Precise DNA base editing using AlphaFold3-based contact modelling

**Source:** [https://www.nature.com/articles/s41586-026-10794-z](https://www.nature.com/articles/s41586-026-10794-z)
**Created:** 2026-08-01

---

## Abstract
This paper introduces **ContactSeek**, an artificial-intelligence-driven framework designed to enhance the specificity of genome editors by leveraging AlphaFold3 (AF3)-predicted contact probability. Genome editing currently faces a trade-off between activity and specificity, often requiring high labour and resulting in low success rates for precision improvement.

## Key Points
- **AI-Driven Optimization**: Uses AF3-predicted contact probabilities rather than just 3D structures to distinguish between on-target and off-target interactions.
- **Consensus Contact Regions (CCRs)**: Identifies specific residues within the protein that exhibit consistent contact changes when binding to off-target DNA, pinpointing exactly where mutations are needed to increase specificity.
- **Superior Performance**: A developed variant combining mutations in both Cas9 and TadA8e outperformed existing high-fidelity adenine base editors (ABEs).
- **Generalizability**: The framework was successfully generalized to improve Cas12a-based cytosine base editors (CBEs) as well.

## Methodology
The researchers mapped genome-wide off-targets for Cas9–TadA adenine base editors and fed these sequences into AF3. They found that contact probability was a more sensitive metric than traditional structural analysis for detecting differential interactions. By correlating this data with sequencing-based off-target signals, they identified CCRs and specificity-determining residues. Validation was performed via targeted amplicon sequencing, genome-wide profiling, R-loop assays, and RNA-sequencing.

## Findings/Results
The study successfully created high-precision base editors with significantly reduced off-target effects without sacrificing on-target efficiency. The results establish a new paradigm for improving CRISPR tools by integrating structural predictions (AI) with functional genomic data.

## Notes
The work highlights the transition from "trial-and-error" directed evolution to an AI-informed design process, reducing the reliance on exhaustive laboratory screening.

