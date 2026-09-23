# Paper Summary

### Authors

Zhidian Zhang, Hannah K. Wayment-Steele, Garyk Brixi, Haobo Wang, Dorothee Kern, and Sergey Ovchinnikov.

### Journal

Proceedings of the National Academy of Sciences (PNAS)

### Publication Date

October 28, 2024

### DOI

[10.1073/pnas.2406285121](https://doi.org/10.1073/pnas.2406285121)

## Keywords

Protein language models; ESM-2; ESMFold; protein structure prediction; coevolution; contact prediction; categorical Jacobian; protein isoforms; masked language modeling.

## Main Idea

The authors investigate how the protein language model ESM-2 obtains strong single-sequence structure predictions. Their results support a motif-pairing model: ESM-2 has learned and compressed evolutionary statistics describing dependencies between interacting sequence segments, rather than directly learning the physical process of protein folding or requiring a representation of each complete fold. The model can therefore recover contacts when the relevant local sequence context is revealed, even when most of the protein sequence remains masked.

## Evidence Supporting the Main Idea

- Across 18 previously reported domain-splitting protein isoforms, AlphaFold2, OmegaFold, and ESMFold generally produced models with low RMSD to the corresponding region of the full-length structure, high confidence, and increased spatial aggregation propensity (SAP). For human myoglobin isoform Q8WVH6, the RMSDs were 0.49, 1.01, and 0.81 Å for AlphaFold2, OmegaFold, and ESMFold, respectively, despite exposed hydrophobic residues that make the fragment physically implausible. This argues against treating the models as reliable physics-based predictors for such out-of-distribution sequences.
- The authors introduce a fully unsupervised categorical Jacobian: each residue is changed to each of the 20 amino-acid tokens, and the resulting changes in the model's output logits are used to estimate pairwise couplings. On 1,431 proteins, the ESM-2 3-billion-parameter model achieved mean long-range contact precision at top L/2 of 0.80, versus 0.67 for the inverse-covariance linear model and 0.87 for the supervised ESM-2 Contact Head (Fig. 4 C–D).
- Coupling weights from the categorical Jacobian became more correlated with linear-model couplings as ESM-2 model size increased, indicating that the language model stores recognizable coevolutionary statistics.
- In masking experiments, contacts were recovered much more effectively by unmasking residues flanking the two contacting 11-residue segments than by randomly unmasking the same number of residues. Fifty percent of long-range secondary-structure-element pair contacts were recovered with 22 flanking residues for pairs separated by 50–100 residues and 30 residues for pairs separated by more than 100 residues; flanking unmasking was approximately 2.5 times as effective as random unmasking.
- Contact recovery often showed a step-like transition. A one-residue addition increased recovery by more than 0.5 in 82% of recoverable segment pairs separated by 15 residues, 76% of pairs separated by 50–100 residues, and 64% of pairs separated by more than 100 residues. These abrupt transitions are consistent with the model recognizing learned sequence motifs or motif pairings.

## Main Novelty

The study combines an interpretable, unsupervised categorical-Jacobian analysis with targeted sequence-masking experiments to distinguish among three explanations for pLM structure prediction: learning folding physics, storing a separate coevolution model for each protein family, or storing reusable coevolutionary models for interacting sequence fragments. It provides evidence for the third explanation and supplies a general procedure for extracting and comparing pairwise evolutionary signal from nonlinear protein language models.

## Datasets Used for Evaluation

- **Domain-splitting isoform dataset:** 18 protein isoforms previously identified as cases in which alternative splicing disrupts structured domains. The dataset was used to compare AlphaFold2, OmegaFold, and ESMFold predictions with full-length experimental structures using RMSD, model confidence, and SAP.
- **GREMLIN/PDB_EXP structure dataset:** 2,245 structures from the GREMLIN coevolution-prediction database, initially selected from proteins with more than 1,000 MSA sequences. After filtering similar structures by TM-align score, retaining proteins of length 200–600 amino acids, and excluding structures missing 50 or more residues, 1,431 proteins remained. This dataset was used for contact-precision and coupling-correlation benchmarks.
- **Contact-recovery segment pairs:** From the 1,431-protein benchmark, the authors examined 4,022 pairs of 11-residue segments with centers 15 residues apart, 1,273 secondary-structure-element pairs separated by 50–100 residues, and 304 pairs separated by more than 100 residues. These subsets were used to test how local context and masking affect contact recovery.

## Experimental Procedure

- Curate 18 domain-splitting isoforms and identify their corresponding UniProt full-length proteins and experimental structures.
- Predict isoform structures with AlphaFold2 using ColabFold, OmegaFold, and ESMFold; measure aligned-region RMSD, pLDDT where available, and per-residue SAP.
- Assemble and filter the GREMLIN/PDB_EXP structures and their MSAs to create the 1,431-protein evaluation set.
- Compute inverse-covariance pairwise couplings from filtered MSAs and compare them with couplings obtained from ESM-2 categorical Jacobians.
- Convert coupling tensors into contact maps with average-product correction and evaluate the precision of the top L/2 long-range contacts, where long-range means a sequence separation greater than 24 residues.
- Compare categorical Jacobian contacts with contacts from the supervised ESM-2 Contact Head and assess coupling-weight correlations across ESM-2 model sizes.
- Mask protein sequences except for selected 11-residue segment pairs; progressively unmask flanking residues, or randomly unmask matched numbers of residues, and quantify contact recovery against the fully unmasked prediction.
- Analyze abrupt recovery transitions and estimate the amount of unmasked context needed for motif-pair contact recovery.

## Key Biology Insights

- Strong single-sequence protein-structure predictions do not by themselves demonstrate that a model has learned the physical laws of folding.
- Protein language models can encode evolutionary coupling information implicitly through masked-language-model training, even without an input MSA at inference time.
- Learned dependencies appear to be reusable across sequence contexts and may be organized around interacting motifs rather than only complete protein families.
- High-confidence predictions can still be biologically misleading for alternative isoforms or other out-of-distribution sequences; exposed hydrophobic patches provide a concrete warning sign.
- The authors estimate that storing sparse pairwise statistics for roughly 20,000 protein families of average length 256 would require about 4 billion parameters under an assumption of at most four contacts per position, comparable to the scale at which ESM-2 performance begins to plateau.

## Implications

The work motivates using pLMs as compressed repositories of evolutionary statistics and developing interpretability tools that separate memorized evolutionary information from genuine physical reasoning. The categorical Jacobian offers an unsupervised way to inspect pairwise dependencies in other pLMs. For practical structure or function inference, model confidence should be paired with checks for distribution shift and physical plausibility, especially for isoforms and sequences with limited homologous support. The authors also note that their experiments do not fully exclude learning of complete-fold representations, and the isoform analysis lacks direct experimental measurements of the isoforms' in-vitro structural ensembles.
