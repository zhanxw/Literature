# Paper Summary

**Title:** Multimodal profiling of lung granulomas in macaques reveals cellular correlates of tuberculosis control

**Source:** [Published article](https://doi.org/10.1016/j.immuni.2022.04.004); [full-text PDF read for this summary](https://discovery.ucl.ac.uk/id/eprint/10183814/1/1-s2.0-S1074761322001753-main.pdf).

### Authors

Hannah P. Gideon, Travis K. Hughes, Constantine N. Tzouanas, et al. Senior authors: JoAnne L. Flynn, Sarah M. Fortune, and Alex K. Shalek.

### Journal

Immunity, 55(5), 827–846.e10.

### Publication Date

May 10, 2022; published online April 27, 2022.

### DOI

[10.1016/j.immuni.2022.04.004](https://doi.org/10.1016/j.immuni.2022.04.004)

## Keywords

Tuberculosis; granuloma; cynomolgus macaque; single-cell RNA sequencing; PET-CT; bacterial control; T1–T17 cells; cytotoxic T cells; stromal cells; type 2 immunity.

## Main Idea

Individual tuberculosis granulomas within the same host have distinct cellular ecosystems associated with their bacterial burden and apparent time of formation. Low-burden lesions are enriched for particular T/NK-cell states, whereas high-burden lesions favor stromal, plasma-cell, mast-cell, and tissue-repair programs. Integrating longitudinal imaging with endpoint microbiology and single-cell RNA sequencing identifies candidate correlates of local control, rather than proving that any one cell population causes bacterial clearance.

## Evidence Supporting the Main Idea

- **Lesions differ within hosts (Figure 1).** The principal analysis includes 26 granulomas from four macaques at 10 weeks, with 109,584 cells. Thirteen low-burden and 13 high-burden lesions had median log10 CFU values of 2.2 and 3.6, respectively. Cumulative bacterial chromosome equivalents did not differ significantly between groups, while the CFU/CEQ ratio was lower in low-burden lesions, consistent with greater bacterial killing.
- **Apparent formation time is strongly associated with burden (Figure 1).** All high-burden lesions were detectable by four weeks; 11 of 13 low-burden lesions first became detectable at 10 weeks. Detection time correlated inversely with CFU (Spearman rho = −0.82). Imaging detection is not the precise biological time of lesion initiation.
- **Cellular composition tracks control (Figure 2).** Plasma cells, mast cells, endothelial cells, and fibroblasts correlated positively with burden, while T/NK cells correlated negatively. The respective reported FDR-adjusted values were 0.00021, 0.016, 0.0087, 0.036, and 0.023. These are lesion-level associations nested within four animals.
- **Specific T-cell states matter more than a generic inflammatory label (Figures 3–4).** Analysis of 41,222 T/NK cells identified 13 subclusters. A deeper analysis of 9,234 T1–T17 cells identified four states; selected states expressing type 1/type 17-associated or stem-like programs associated with low burden. The T1–T17 designation reflects transcriptional features including CCR6, CXCR3, and ROR-family regulators; IL17A and IL17F were not detected. Not every IFNG/TNF-expressing state correlated with control.
- **Cytotoxic-cell evidence depends on the analysis (Figure 3).** A conventional CD8 cytotoxic state had a strong association in the Dirichlet model but a correlation FDR value of 0.074. It should not be described as significant under every test.
- **Earlier lesions resemble less-controlled ecosystems (Figure 5).** Six additional granulomas collected at four weeks contained 10,007 profiled cells. Their states more closely resembled the early-detected, high-burden 10-week lesions than the late-detected lesions. This cross-sectional comparison does not track individual cells over time.
- **Communication networks provide mechanistic hypotheses (Figure 6).** Of 2,899 significant inferred interactions, 1,837 were stronger in high-burden and 1,062 in low-burden granulomas. High-burden networks emphasized type 2 immunity and wound repair, while low-burden networks emphasized different chemokine and costimulatory relationships. Ligand–receptor inference is not direct evidence of signaling or cell contact.

## Main Novelty

The study links individual lesion histories and viable bacterial measurements to cellular states within the same lesions. This makes it possible to study why granulomas within one animal differ, instead of treating a whole lung or host as one homogeneous disease state. Its principal contribution is multimodal lesion-level resolution; the dissociated single-cell data do not themselves preserve cellular coordinates.

## Datasets Used for Evaluation

| Dataset | Contents and sample size | Role and access |
|---|---|---|
| Main 10-week macaque granuloma cohort | 26 granulomas, four animals, 109,584 cells; longitudinal PET-CT plus CFU/CEQ | Discovery of composition and state correlates; [GSE200151](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE200151), [SCP257](https://singlecell.broadinstitute.org/single_cell/study/SCP257) |
| Four-week macaque single-cell cohort | Six granulomas, two animals, 10,007 cells | Earlier-stage comparison; [SCP1749](https://singlecell.broadinstitute.org/single_cell/study/SCP1749), within the study's GEO resource |
| Independent histology cohort | 87 granulomas from 16 macaques at 10–12 weeks | Tests lesion morphology and necrosis against lesion history |
| Independent bulk RNA-seq cohort | 12 granulomas: six high- and six low-burden; animal count: Not specified in paper | Orthogonal support for transcriptional programs |
| Flow-cytometry and immunohistochemistry validation | NHP tissues and human/NHP staining supporting selected cellular identities; complete assay-specific cohort sizes: Not specified in paper | Orthogonal validation; this summary does not infer sizes from representative panels |

The last row summarizes supporting assays rather than a new public accession. Supplementary tables should be consulted when constructing a specimen-by-assay manifest; this summary is not a substitute for that manifest.

## Experimental Procedure

- Follow experimentally infected macaques with serial PET-CT and identify individually traceable lesions.
- At the terminal sampling time, measure lesion CFU and bacterial chromosome equivalents, separating viable burden from a cumulative bacterial DNA measure.
- Generate single-cell transcriptomes from lesion tissue, perform quality control, and annotate broad populations and finer cellular states.
- Associate lesion composition and transcriptional programs with burden using correlation and compositional models; examine selected states with orthogonal assays.
- Compare the principal 10-week cohort with earlier lesions and independent bulk/histological cohorts.
- Infer ligand–receptor networks and compare networks between burden groups to nominate candidate cellular interactions.
- Interpret candidates as hypotheses requiring prospective validation and perturbation.

## Key Biology Insights

Bacterial control appears to depend on the composition and state of local immune ecosystems. Abundant inflammatory or antibody-associated cells need not indicate successful control: plasma-cell abundance was positively associated with bacterial burden in this setting. Type 1/type 17-associated and selected cytotoxic or stem-like T-cell programs may provide more specific candidate correlates.

Stromal and repair programs may participate in a permissive lesion environment, but they could also arise as consequences of tissue damage and persistent infection. Timing, lesion history, and host context are therefore essential to interpretation.

## Implications

For spatial host–microbe analyses, this dataset supplies a reference for cell annotation and lesion-level burden-associated signatures. It cannot provide direct spatial validation of cell neighborhoods because its main transcriptomic assay is dissociative. Species differences, the four-animal discovery cohort, dissociation bias, and confounding between detection time and burden limit generalization.

An appropriate follow-up is to test whether these signatures reproduce in independently sampled human lesions, preserving donor-level replication and separately measuring microbial RNA, viable burden, and tissue damage. Neither bacterial RNA nor plasma-cell enrichment should be treated as a universal surrogate for protection.
