# Paper Summary

### Authors

- Talal Widatalla, Ashir A. Borah, Samuel H. King, Claudia L. Driscoll, Rafael Rafailov, and Brian L. Hie

### Journal

- Nature Methods, volume 23, pages 1805-1813

### Publication Date

- August 14, 2026 (published online; September 2026 issue)

### DOI

- https://doi.org/10.1038/s41592-026-03137-3

## Keywords

- ProteinDPO
- protein design
- generative protein models
- direct preference optimization
- model alignment
- ESM-IF1
- protein stability
- inverse folding
- hemagglutinin
- H5N1 influenza
- vaccine antigen stabilization
- experimental fitness

## Main Idea

- ProteinDPO adapts direct preference optimization (DPO), originally developed to align language models with human preferences, to align a pretrained structure-conditioned protein language model with experimental protein-stability measurements.
- Starting from ESM-IF1, the method treats a protein backbone as the prompt, candidate amino-acid sequences as responses, and measured stability as preference information. It improves mutation-effect scoring and stable-sequence generation while retaining capabilities learned during unsupervised pretraining better than conventional supervised fine-tuning (SFT).
- The aligned model generalizes beyond the small monomeric proteins used for training to larger proteins, multichain antibodies, protein complexes, and experimental stabilization of trimeric H5 influenza hemagglutinin (HA). This supports the broader concept of aligning biological foundation models to measured fitness, although only stability alignment and a limited set of related tasks were demonstrated.

## Evidence Supporting the Main Idea

- **Leakage-aware training set (Figure 1):** The original Megascale resource contained approximately 1.84 million variants from 479 natural and Rosetta-designed domains. After reliability filtering, removal of unsupported mutation types and duplicates, and FoldSeek structural clustering, the DPO dataset contained about 660,000 stability measurements across 403 domains. The figure reports 609,000 training variants from 379 proteins, 22,000 validation variants from 12 proteins, and 25,000 test variants from 12 proteins.
- **Megascale holdout performance (Figure 2b):** Vanilla ESM-IF1 achieved mean Pearson *R* = 0.55, Spearman rho = 0.53, and AUROC = 0.74 for mutation-associated stability changes. SFT improved modestly to 0.59, 0.57, and 0.76, whereas the paired, ranked, and weighted ProteinDPO variants reached Pearson *R* = 0.72-0.73, Spearman rho = 0.69-0.72, and AUROC = 0.82-0.84.
- **Non-additive double mutations (Figure 2c and Extended Data Table 1):** On 20,202 double mutants, adding separately scored single-mutation effects gave ProteinDPO Pearson *R* = 0.36-0.40 versus 0.41 for ThermoMPNN. Scoring each complete double-mutant sequence raised ProteinDPO to 0.44-0.48, suggesting that whole-sequence likelihood captures some mutation interactions unavailable to an explicitly additive baseline.
- **Out-of-distribution stability benchmarks (Figure 2d,e):** On a homolog-controlled S669 set, ProteinDPO reached Pearson *R* = 0.44-0.47 versus 0.43 for ThermoMPNN. On homolog-free FireProt, ProteinDPO reached approximately 0.60 versus 0.65 for ThermoMPNN. ProteinDPO consistently improved over vanilla ESM-IF1, whereas SFT lost performance outside the Megascale distribution, supporting better retention of generalizable pretrained information but not universal superiority over specialized predictors.
- **Binding and antibody generalization (Figure 3b,c):** Despite being trained only on monomer stability, ProteinDPO modestly improved over vanilla ESM-IF1 on SKEMPIv2 protein-complex binding changes and more clearly on AB-Bind antibody-antigen affinity changes. It also improved Pearson and Spearman correlations by 0.08-0.12 when ranking melting temperatures of 483 diverse antibodies. These gains are small-to-moderate and establish transfer rather than state-of-the-art dominance.
- **Generative stability test (Figure 3d):** For staphylococcal nuclease (PDB 1STN), phosphoglycerate kinase (1PHP), and claudin-15 (4P79), 500 ProteinDPO generations per backbone had substantially lower Rosetta energies than vanilla ESM-IF1, SFT, and the native sequences. ESMFold predictions had pLDDT above 80 and closely matched the target folds. This is an independent computational check, not experimental confirmation of expression or stability.
- **Recovery of known HA biology (Figure 4 and Extended Data Figure 2):** In zero-shot ranking against the A/Vietnam/1203/04 H5 HA prefusion structure, 6 of the top 30 substitutions exactly matched 6 of 8 stabilizing mutations previously reported for other HA subtypes. ProteinDPO also identified H26, K51, and E103, residues implicated in the pH-sensitive conformational switch, without HA examples in its alignment data.
- **Prospective HA stabilization (Figure 4):** Of 30 ProteinDPO-selected single substitutions tested by differential scanning fluorimetry, 19 increased melting temperature by more than 1 degrees C and 7 remained within 1 degrees C of wild type. All tested nine-substitution designs were more stable than wild type; the best improved melting temperature by 17 degrees C, and nine-substitution variants averaged 9.8 degrees C more stable than single-substitution variants. Across all 45 experimental designs, about 80% increased or maintained stability.
- **Preserved antigen-related properties (Figure 5):** Three nine-substitution HA variants retained strong nanomolar or subnanomolar binding to broadly neutralizing antibodies 13D4 and CR6261 despite some mutations being near their epitopes. Circular dichroism spectra indicated retention of native-like secondary structure. These assays support preserved recognition by two antibodies but do not establish full antigenicity or vaccine efficacy.
- **Transfer across two decades of viral evolution (Figure 5b):** Applying the DPO-16 substitutions selected from the 2004 Vietnam HA to 2024 Texas dairy-cattle and British Columbia human H5N1 HAs increased melting temperature by 13 degrees C and 32 degrees C, respectively. This experimental result suggests that the selected substitutions exploit conserved structural features rather than only strain-specific sequence context.

## Main Novelty

- Recasts protein fitness alignment as an offline preference-optimization problem: the native backbone is the context, sequence variants are candidate responses, and experimental biophysical measurements define preferences.
- Introduces and evaluates paired, ranked, and a newly derived weighted DPO objective. Weighted DPO directly uses scalar fitness values through a Boltzmann-like target distribution rather than discarding their magnitude by converting them only to ranks.
- Demonstrates a useful middle ground between unsupervised generation and task-specific regression: one model can both score variants and generate new full sequences while remaining close to the pretrained sequence distribution.
- Shows cross-scale transfer from relative stability measurements on 40-75-residue monomers to proteins up to roughly 394 residues, multichain antibodies and complexes, and a greater-than-500-residue viral antigen assembled as a trimer.
- Couples computational benchmarking to a prospective, experimentally tested H5 HA design campaign and then transfers one multi-mutation design to two recently emerged 2024 H5N1 strains.

## Datasets Used for Evaluation

- **Megascale stability dataset, version 2 (April 20, 2023):** Approximately 1.84 million experimentally characterized sequence variants across 479 domains before curation. The final ProteinDPO corpus contained about 660,000 reliable substitution variants across approximately 403 domains. FoldSeek clusters, rather than individual sequences, were assigned to 90% training, 5% validation, and 5% test splits to reduce structural leakage. The holdout shown in Figure 1 contained approximately 25,000 variants from 12 proteins.
- **ThermoMPNN comparison split:** A Megascale split from Dieckhaus and colleagues was used to train models on the same data and evaluate double mutants fairly. The double-mutation analysis included 20,202 holdout variants.
- **S669:** Experimental stability changes for 669 single mutations across 94 proteins. Four variants containing noncanonical amino acids were removed for ESM-IF1/ProteinDPO evaluation, leaving 665. A Megascale training set purged of S669 homologs was used to limit leakage.
- **FireProt:** A curated database of 3,438 single mutations across 100 proteins. The homolog-free version used here removed proteins related to Megascale, leaving 2,578 variants.
- **SKEMPIv2:** Experimental binding-free-energy changes for mutations at protein-protein interfaces. After excluding structures with noncanonical amino acids, 6,487 variants remained. Because some complexes had very few variants, correlations were calculated across the full dataset rather than averaged per complex.
- **AB-Bind:** Initially 1,101 antibody-antigen variants across 32 complexes with experimental binding-free-energy changes. Removing duplicates, variants with missing mutated residues, and entries lacking an experimental structure yielded 1,011 variants; performance was averaged within antibody-antigen complexes, with 27 complexes represented in the evaluation figure.
- **Antibody thermal-unfolding collection:** 483 melting-temperature measurements from clinical-trial antibodies and human B-cell or long-lived plasma-cell-derived monoclonal antibodies compiled from the Jain and Shehata datasets. Predicted variable-domain structures and sequences were used as model inputs.
- **In silico generative evaluation backbones:** Staphylococcal nuclease (PDB 1STN; 136 residues), phosphoglycerate kinase (PDB 1PHP; 394 residues), and claudin-15 (PDB 4P79; 198 residues). Each model generated 500 sequences per backbone across sampling temperatures for Rosetta and ESMFold evaluation.
- **Experimental H5 HA campaign:** The primary design template was prefusion A/Vietnam/1203/2004 H5N1 HA (PDB 6CFG), with PDB structures 2FK0 and 6CF5 added for ensemble ranking. The study tested 45 single- and multi-substitution designs. Transfer experiments used A/Texas/dairycattle/Texas/24009367011/2024 (GISAID EPI_ISL_19094620; genotype B.3.13) and A/British_Columbia/PHL-2032/2024 (EPI_ISL_19548836; genotype D1.1).

## Experimental Procedure

1. Start with pretrained ESM-IF1, a structure-conditioned autoregressive protein language model, and curate reliable Megascale variants with measured absolute or relative stability.
2. Remove insertions, deletions, and duplicate sequences; cluster native structures with FoldSeek at 50% structural-similarity threshold; and assign whole clusters to train, validation, and test partitions to reduce leakage across related folds.
3. Construct preference examples that share a native backbone. Train three ProteinDPO variants: paired comparisons between more- and less-stable sequences, ranked sets of sequences, and weighted sets that retain scalar stability information. Keep the original ESM-IF1 as the reference distribution through the DPO penalty.
4. Train an SFT control from the same pretrained weights using only variants more stable than their native sequence and a maximum-likelihood objective. Compare all aligned and control models with identical scoring code, differing only in model weights.
5. Evaluate mutation-effect prediction on the structurally separated Megascale test data and homolog-controlled S669 and FireProt datasets using Pearson correlation, Spearman correlation, and AUROC for stabilizing-versus-destabilizing classification. Test full-sequence versus additive scoring on double mutants.
6. Test transfer to related biophysical properties using SKEMPIv2 and AB-Bind binding-affinity changes and melting temperatures from 483 antibodies.
7. Sample 500 sequences for each of three larger backbones using ProteinDPO, vanilla ESM-IF1, and SFT. Estimate independent force-field energies with Rosetta cart_ddg and assess fold preservation and prediction confidence with ESMFold self-consistency and pLDDT.
8. Score all possible single substitutions in the Vietnam 2004 H5 HA sequence, averaging ranks across three experimental structures. Express and screen the top 30 candidates by differential scanning fluorimetry.
9. Remove deleterious substitutions, score combinatorial three-, five-, and nine-substitution variants by whole-sequence likelihood, and experimentally test selected combinations for synergistic stabilization.
10. Generate HA constructs by site-directed mutagenesis, express them in Expi293F cells, and purify His-tagged trimers by cobalt-affinity and size-exclusion chromatography.
11. Measure thermal unfolding from 20 to 95 degrees C in triplicate by differential scanning fluorimetry. Characterize selected variants by circular dichroism and measure binding to head-targeting 13D4 and stem-targeting CR6261 broadly neutralizing antibodies by biolayer interferometry, using an anti-SARS-CoV-2 antibody as a nonbinding control.
12. Introduce the nine substitutions of DPO-16 into the Texas 2024 cattle and British Columbia 2024 human H5N1 sequences and repeat thermal-stability measurements to evaluate transfer across evolved viral genotypes.

## Key Biology Insights

- HA must remain in its metastable prefusion conformation to present desirable vaccine epitopes, yet it naturally undergoes a low-pH-triggered transition during viral entry. Stabilizing H26, K51, and E103 supports the proposed role of this region as a conformational pH switch.
- Many successful substitutions introduced bulky hydrophobic residues such as leucine, tryptophan, tyrosine, or phenylalanine into the helical core, consistent with cavity filling and tighter core packing as stabilizing mechanisms.
- Combining individually acceptable mutations is not reliably additive because residues interact energetically. ProteinDPO's improved full-sequence scoring of double mutants and the strong average performance of nine-substitution HA variants are consistent with partial capture of epistasis, although the experiments did not map individual interaction terms.
- The same DPO-16 substitutions substantially stabilized phylogenetically separated 2024 H5N1 HAs, suggesting that the engineered mechanism acts on conserved structural constraints of the prefusion fold.
- Binding to two broadly neutralizing antibodies and preservation of circular-dichroism spectra indicate that large stability gains can coexist with retention of important epitopes and overall secondary structure. The study did not test the complete antigenic repertoire, receptor binding, fusion activity, or immune responses in animals.
- Generalization from monomer stability to complex binding and antibody melting temperature implies that the aligned model learned features related to shared enthalpic, entropic, packing, and folding constraints. This is a plausible interpretation of transfer performance, not direct identification of a universal biophysical mechanism.

## Implications

- Preference optimization offers a general strategy for adding experimentally measured objectives to biological foundation models without replacing them with narrow regressors. The weighted formulation may be especially useful when experiments yield quantitative fitness rather than only pairwise labels.
- ProteinDPO could reduce experimental search space in protein engineering by ranking and generating candidates that better reflect a target property while retaining structural compatibility learned during pretraining.
- The H5 results point to a rapid-response workflow for stabilizing vaccine antigens from emerging strains: align once on broad stability data, design from available structures, screen a small candidate set, and transfer successful changes to new variants.
- Claims should remain bounded to the evidence. The model did not clearly beat every specialized stability predictor, transfer gains for binding affinity were modest, and Rosetta/ESMFold evaluations are computational proxies rather than wet-lab measurements.
- The experimental validation comprised 45 HA designs and selected biophysical assays. It did not assess yield at manufacturing scale, long-term storage, aggregation, glycosylation, receptor interaction, membrane fusion, immunogenicity, protection, or safety.
- DPO alignment may inherit bias and measurement noise from the fitness dataset. Success for stability does not guarantee success for catalytic activity, specificity, expression, toxicity, or multi-objective design; each new property will require suitable experimental data and independent validation.
- The authors provide source data, open ProteinDPO code, and paired-objective model weights, enabling reproduction and extension to other protein-generative models and experimental objectives.
