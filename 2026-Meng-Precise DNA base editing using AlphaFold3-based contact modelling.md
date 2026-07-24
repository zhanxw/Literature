# Precise DNA base editing using AlphaFold3-based contact modelling

**Authors:** Haowei Meng, Zhixin Lei, Yongchang Yan, et al.
**Journal:** Nature (2026)
**DOI:** 10.1038/s41586-026-10794-z

## Summary

### Main Idea
The paper introduces **ContactSeek**, an artificial-intelligence-driven framework designed to enhance the specificity of genome editors (such as base editors). The core concept is to use **AlphaFold3 (AF3)-predicted contact probability (CP)** rather than just 3D structural coordinates to identify residues that differentiate between on-target and off-target interactions. By correlating these AF3 predictions with experimental off-target data, the authors can pinpoint "specificity-determining residues" and engineer variants with significantly reduced off-target effects.

### Novelty
The primary novelty lies in the use of **contact probability** as a more sensitive metric than predicted static structures for detecting differential interactions between on- and off-target complexes. ContactSeek integrates structural predictions (AF3) with functional data (sequencing-based off-target signals) to establish a paradigm for precision genome editing tool improvement.

### Experimental Procedure
1. **Off-Target Mapping:** The authors mapped genome-wide off-targets using techniques like dI-profiling and Detect-seq.
2. **AF3 Prediction:** Off-target DNA sequences were fed into AlphaFold3 to generate contact probability (CP) matrices for both on-target and off-target complexes.
3. **$\Delta$CP Analysis:** Difference in CP ($\Delta$CP = off-target - on-target) was analyzed. If a residue's interaction changes significantly between target and off-target, it is likely involved in specificity.
4. **Identifying CCRs:** The framework identified **Consensus Contact Regions (CCRs)**—neighboring residues with consistent contact changes—and pinpointed key residues within them.
5. **Variant Engineering & Validation:** 
    - For ABEs: Identified the **K1020D** mutation in Cas9 and optimized TadA8e deaminase.
    - For CBEs: Generalized the approach to Cas12a, identifying mutations like **R284E** and **H29D**.
6. **Evaluation:** Validated using targeted amplicon sequencing, genome-wide profiling (dI-profiling/Detect-seq), orthogonal R-loop assays, and RNA-sequencing for transcriptomic off-targets.

### Key Findings & Evidence
- **Cas9 K1020D Improvement:** The Cas9(K1020D)-TadA8e variant showed massive reductions in total off-target signals (83% at HEK4 site and 69% at ABEsite16) compared to standard ABE8e, while maintaining similar on-target editing rates.
- **Deaminase Optimization:** ContactSeek successfully identified key residues in the TadA8e deaminase to improve its specificity via structural/functional integration.
- **Generalizability:** The framework was effectively applied to Cas12a-based CBEs, where the variant Cas12a(R284E)-A3A(H29D) showed significant off-target reduction (up to 95%).
- **Performance:** The best developed variants outperformed several existing high-fidelity adenine base editors.

## Conclusion
ContactSeek provides a scalable, AI-driven workflow to improve genome editor specificity by leveraging AlphaFold3's protein-nucleic acid interaction predictions. It moves beyond "guessing" mutations toward a structured approach based on contact probabilities.
