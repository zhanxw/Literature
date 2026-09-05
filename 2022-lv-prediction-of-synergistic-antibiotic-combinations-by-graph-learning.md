# Paper Summary

### Authors

Ji Lv, Guixia Liu, Yuan Ju, Ying Sun, and Weiying Guo

### Journal

*Frontiers in Pharmacology*, Volume 13, Article 849006

### Publication Date

March 8, 2022

### DOI

[10.3389/fphar.2022.849006](https://doi.org/10.3389/fphar.2022.849006)

## Keywords

- Antibiotic combination
- Antimicrobial resistance
- Graph learning
- Bacterial infection
- Synergy effect
- Network pharmacology
- Protein–protein interaction network

## Main Idea

The paper presents an interpretable graph-learning framework for predicting synergistic antibiotic pairs. Instead of representing each drug with thousands of chemical or chemogenomic features, the method propagates known antibiotic targets through an *Escherichia coli* protein–protein interaction (PPI) network to construct a drug action-propagating module (DAPM). Network proximity between two DAPMs is then converted into an affinity matrix for graph-regularized prediction.

The central empirical observation is that synergistic antibiotics tend to perturb overlapping—but not completely identical—network neighborhoods. Completely separated modules are usually non-synergistic, whereas identical modules tend to be additive. This topology supplies both a low-dimensional predictive feature and a mechanistic explanation for predicted combinations.

## Evidence Supporting the Main Idea

- **Network-scale evidence:** The authors constructed an *E. coli* PPI network containing 4,020 proteins and 59,496 interactions. Direct target distance alone did not distinguish the interaction classes reliably: 92.3% of antibiotic pairs did not share a target, and adjacent targets occurred among synergistic as well as additive or antagonistic pairs (Supplementary Figure S1).
- **Propagated drug-action modules:** Network propagation expanded drugs with typically only one or two annotated targets into DAPMs averaging approximately 13 nodes. This revealed pathway-level overlap that was not apparent from direct target comparisons (Figure 1 and Results).
- **Topology–phenotype relationship:** Among pairs with overlapping but non-identical DAPMs, 87.5% were synergistic, although this enrichment was not statistically significant in the reported permutation test (`p = 0.118`). Among pairs with separated DAPMs, 90.1% were non-synergistic (`p < 10^-4`). Pairs with identical DAPMs were 100% additive in this dataset (Figure 2). These observations support the topology rule, but the overlap result should be interpreted cautiously because of its non-significant p-value and small dataset.
- **Mechanistic example:** Chloramphenicol and erythromycin perturb overlapping 50S-ribosome neighborhoods and were reported to have negative network proximity (`S = -0.97`). Gene-enrichment analysis linked both DAPMs to protein synthesis, consistent with their known synergistic inhibition of the peptidyl-transferase center and nascent-peptide exit tunnel (Figure 3).
- **Additional biological consistency:** Virtual screening around the trimethoprim DAPM recovered sulfamethoxazole, whose DAPM overlaps that of trimethoprim (`S = -0.12`). This agrees with the established sequential blockade of folate synthesis by this drug pair (Supplementary Figure S2A).
- **Ablation evidence:** Randomizing the PPI network worsened model performance, indicating that biological network structure—not merely graph regularization—contributed useful signal (Supplementary Figure S3).
- **Predictive performance:** On the paper's benchmark comparison, the proposed model achieved precision 0.875, recall 0.70, accuracy 0.90, and F1 0.78. The corresponding results were 0.83/0.38/0.86/0.53 for CosynE and 0.30/0.85/0.58/0.44 for INDIGO (precision/recall/accuracy/F1; Table 4).
- **Candidate-pair evidence:** At a prediction threshold of 0.2, the model nominated eight pairs: tetracycline–roxithromycin, roxithromycin–clarithromycin, oxacillin–penicillin G, cefoxitin–penicillin G, roxithromycin–erythromycin, roxithromycin–chloramphenicol, penicillin G–tetracycline, and penicillin G–trimethoprim (Table 3). Five had been classified as synergistic in Mason et al.; two additional roxithromycin pairs had support from a separate study cited by the authors. Penicillin G–trimethoprim was additive in the cited comparison. This is retrospective literature agreement, not prospective experimental validation performed in this paper.

## Main Novelty

- Introduces network proximity between propagated antibiotic-action modules as a compact, mechanism-linked feature for antibiotic-combination prediction.
- Encodes a specific biological rule: partial overlap of drug-perturbed subnetworks favors synergy, complete identity favors additivity, and separation usually indicates a lack of synergy.
- Combines that mechanistic affinity definition with graph regularization, reducing dependence on very high-dimensional Morgan fingerprints or chemogenomic profiles.
- Provides pathway- and target-level explanations for individual predictions rather than treating the predictor as a purely black-box classifier.

## Datasets Used for Evaluation

- **Pairwise antibiotic-interaction dataset:** 91 unique pairwise combinations among 14 antibiotics, measured previously in *E. coli* strain MG1655 and obtained from Chandrasekaran et al. (2016). Interactions were labeled from the experimental α-score as synergistic (`α ≤ -0.25`), additive (`-0.25 < α < 1`), or antagonistic (`α ≥ 1`). Only antibiotics with a known protein or RNA target were retained. The exact counts in each class are not specified in the main paper.
- **Drug-target dataset:** Target annotations for the same 14 antibiotics were assembled from prior literature and DrugBank. The drugs span inhibition of 30S or 50S protein synthesis, DNA gyrase/topoisomerase, folate synthesis, cell-wall synthesis, and nitrofurantoin's multiple mechanisms. Human targets were excluded.
- ***E. coli* PPI network:** STRING v11.5 interactions with confidence score ≥0.7, yielding 59,496 interactions among 4,020 proteins. This network was used for drug-action propagation and the randomized-network ablation.
- **Prediction/validation set:** Three additional antibiotics—kanamycin, penicillin G, and roxithromycin—were paired computationally with the 14 training antibiotics, producing 42 scored pairs in Table 3. Previously published interaction measurements from Mason et al. (2017) and Yilancioglu (2019) were used for retrospective comparison; this paper reports no newly generated wet-lab validation dataset.
- **Benchmark comparison:** The proposed method, CosynE, and INDIGO were compared on the paper's benchmark antibiotic-combination data using precision, recall, accuracy, and F1. The main text does not specify an independent train/test split or cross-validation protocol for Table 4.

## Experimental Procedure

- **Collect interaction labels and targets:** Assemble the 91 *E. coli* MG1655 antibiotic pairs, classify them by α-score, and map the 14 antibiotics to known bacterial protein or RNA targets.
- **Build the molecular network:** Retrieve STRING v11.5 *E. coli* protein interactions, remove edges with confidence below 0.7, and retain the resulting 4,020-node/59,496-edge PPI network.
- **Propagate each drug's action:** Initialize the drug's annotated targets on the PPI network and iteratively propagate influence using `F(t+1) = βA'F(t) + (1-β)F(0)`, with `β = 0.7`. For multitarget drugs, initial weight is divided equally among targets.
- **Define DAPMs:** Retain propagated nodes with score `F* ≥ 0.0065` to create a local drug action-propagating module. The resulting modules contain about 13 nodes on average.
- **Quantify pair relationships:** Compute Jaccard overlap and shortest-path-based network proximity between each pair of DAPMs. Categorize the module relationship as overlapping, separated, or identical.
- **Construct the affinity matrix:** Assign affinity `W(i,j) = 1` when network proximity is between -1 and 0, representing partially overlapping/pharmacologically similar modules, and 0 otherwise. Identical pairs (`S = -1`) are excluded from the affinity relation because they were associated with additivity.
- **Fit graph regularization:** Combine the affinity matrix with known antibiotic-interaction labels in a graph-regularized objective and solve it analytically to obtain predicted pair scores. The model parameter `γ` was fixed at 0.7 after sensitivity analysis.
- **Choose a decision threshold:** Examine thresholds from 0.1 to 0.5; use 0.2 because larger thresholds increased precision but reduced recall and accuracy, with F1 declining above 0.2 (Supplementary Figure S4).
- **Generate candidates:** Score the 42 combinations between the three validation-set antibiotics and the 14 training antibiotics, and nominate eight pairs above the chosen threshold.
- **Evaluate and interpret:** Compare predicted pairs with previously published experimental classifications; benchmark precision, recall, accuracy, and F1 against CosynE and INDIGO; inspect ribosomal and folate-pathway examples; and randomize the PPI network as an ablation test.

## Key Biology Insights

- Antibiotic synergy may be better captured at the pathway-neighborhood level than by exact target sharing. Drugs acting at distinct sites within a common functional module can reinforce one another even when they do not bind the same molecule.
- Partial network overlap and complete target/module identity represent different pharmacological situations. Partial overlap can combine complementary perturbations within one biological process, whereas near-identical action may produce only an additive effect.
- The erythromycin–chloramphenicol example links network overlap to coordinated disruption of 50S-ribosome function and protein synthesis.
- The trimethoprim–sulfamethoxazole recovery shows that propagation can recognize sequential inhibition within folate biosynthesis despite distinct direct enzyme targets.
- Apparent topology–synergy mismatches may reflect measurement variability or incomplete target annotation. The paper notes an α-score replicate correlation of only 0.81 and cites a newly recognized gentamicin binding site as an example of missing biology.

## Implications

The framework offers a computational way to prioritize a manageable subset of antibiotic pairs for experimental testing while retaining a biological explanation for each prediction. It may be especially useful when labeled combinations are scarce and high-dimensional chemical or chemogenomic features would overfit.

The findings remain hypothesis-generating. The analysis is limited to pairwise combinations in one *E. coli* strain, depends strongly on the completeness and accuracy of drug-target annotations and an undirected, unsigned PPI network, and relies mainly on retrospective agreement with published experiments. Future validation should use prospective dose-resolved assays, independent strains and species, directed/signed interaction networks, and evaluation designs that explicitly prevent information leakage.
