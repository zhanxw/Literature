# Paper Summary

**Title:** Single-cell and spatial profiling highlights TB-induced myofibroblasts as drivers of lung pathology

**Source:** [Published article](https://doi.org/10.1084/jem.20251067); [full-text PDF read for this summary](https://dspace.mit.edu/server/api/core/bitstreams/6c170498-848a-4901-b4ab-829203f25e33/content).

### Authors

Ian M. Mbano, Nuo Liu, Marc H. Wadsworth II, et al. Senior authors: Paul T. Elkington, Alex K. Shalek, and Alasdair Leslie.

### Journal

Journal of Experimental Medicine, 223(3), e20251067.

### Publication Date

January 5, 2026 (online); March 2026 issue.

### DOI

[10.1084/jem.20251067](https://doi.org/10.1084/jem.20251067)

## Keywords

Tuberculosis; post-tuberculosis lung disease; fibroblasts; myofibroblasts; MMP1; CXCL5; SPP1; macrophages; granuloma cuff; HIV; single-cell RNA sequencing; spatial transcriptomics.

## Main Idea

Human TB lung lesions contain a disease-associated MMP1+CXCL5+ fibroblast state with a myofibroblast-like program. Single-cell analysis, independent spatial profiling, and protein-level observations place this state alongside SPP1+CHI3L1+ macrophages around granuloma boundaries. The authors propose that their interaction contributes to persistent inflammation and remodeling. Although the title uses “drivers,” the main evidence establishes association, localization, and computationally inferred communication; it does not establish necessity or sufficiency through targeted perturbation.

## Evidence Supporting the Main Idea

- **Discovery in clinically relevant but selected tissues (Figures 1–4).** Seq-Well S3 profiling yielded 19,632 cells, 16 broad populations, and 30 subsets from nine TB-diseased and four TB-negative donors. Seven of the nine TB donors and one of the four controls were HIV-positive. The controls were tumor-margin lung tissues. TB donors underwent resection after treatment for disease-related complications.
- **A distinct fibroblast state (Figures 4–5).** Among 1,627 fibroblasts, the authors identify five states, including MMP1+CXCL5+ cells. Integration with the Human Lung Cell Atlas connects these cells with myofibroblast and remodeling programs. Their recovery in the discovery cohort was uneven, with most cells from one donor; this limits donor-general conclusions from single-cell abundance alone.
- **A coherent remodeling module (Figure 5).** Coexpression analysis identified seven modules. Module M1, enriched in the disease-associated fibroblasts, includes MMP1, CA12, CXCL5, CXCL13, TDO2, PDPN, and FAP and implicates extracellular-matrix remodeling, chemotaxis, and wound responses. Here “M1” is a module name, not an M1 macrophage phenotype.
- **Orthogonal and external support (Figures 5–6).** Protein staining supports fibroblast markers in human TB lesions. PDPN+FAP+ fibroblasts were detected in all five flow-cytometry donors and were enriched in more diseased tissue. Independent lymph-node expression data and macaque granuloma datasets support related signatures. In macaques, early timing and high burden covary, so their contributions cannot be separated by this comparison alone.
- **Antigen-response evidence (Figure 6C).** In a reanalyzed tuberculin skin-test dataset, both the fibroblast and SPP1+CHI3L1+ macrophage signatures increased after antigen challenge compared with saline, with stronger responses in active than latent TB. Bulk signatures do not directly measure fibroblast differentiation or prove that the same lung circuit operates in skin.
- **Candidate communication partners (Figures 7–8).** MultiNicheNet and LIANA nominate fibroblasts as major signal senders and receivers and identify macrophage partners. Predicted programs include chemokines, extracellular-matrix ligands, SPP1, and FN1. Interaction counts and expression-based scores are not independent patient-level mechanistic experiments.
- **Spatial replication (Figure 9).** An independent 30-participant Visium cohort places the fibroblast and SPP1+CHI3L1+ macrophage signatures around granuloma cuffs in current and post-TB disease, including HIV-positive and HIV-negative tissues. The signatures correlate spatially, and the SPP1–CD44 axis is nominated at lesion boundaries. Mixed-cell spots and shared regional tissue composition can contribute to these associations.

## Main Novelty

The study brings stromal cells into a human TB framework often dominated by immune-cell analysis. It combines a fibroblast-state definition with independent spatial localization and comparison across lung disease, lymph-node TB, antigen challenge, and macaque infection. Persistence of the signature after microbiological treatment supports studying tissue remodeling as an outcome distinct from bacterial clearance.

## Datasets Used for Evaluation

| Dataset | Contents and sample size | Role and resource |
|---|---|---|
| Human lung Seq-Well S3 discovery | Nine TB donors and four TB-negative tumor-margin controls; 19,632 cells, including 8,313 monocyte/macrophage cells and 1,627 fibroblasts | Cell-state discovery; [SCP3227](https://singlecell.broadinstitute.org/single_cell/study/SCP3227) |
| Independent human lung Visium cohort | 30 participants: 21 current TB (10 HIV-positive, 11 HIV-negative), nine post-TB (five HIV-positive, four HIV-negative) | Spatial replication across disease and HIV strata; SCP3227. Samples include different tissue structures, not 30 equivalent granulomas |
| Human Lung Cell Atlas | The broader atlas contains approximately 2.4 million cells from 49 datasets; this analysis integrated 584,944 reference cells. Fibroblast-focused comparison used 17,500 reference and 1,601 query cells | Reference annotation and disease-state comparison; [HLCA](https://data.humancellatlas.org/hca-bio-networks/lung/atlases/lung-v1-0) |
| Gideon et al. macaque granulomas | Four- and 10-week granuloma single-cell profiles; parent cohorts contain six and 26 granulomas, respectively | Cross-species and burden-associated comparison; [GSE200151](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE200151). These are reused observations, not independent new cohorts for every paper |
| Ganchua/Bromley macaque data | Four-week granuloma and uninvolved-lung profiles; sample size: Not specified in paper | Additional cross-species comparison; cited studies and Table S3 provide provenance |
| Human lymph-node bulk RNA-seq | Parent cohort: 24 adults, comprising seven TB, 10 sarcoidosis, seven normal; the focal TB-versus-control comparison uses seven versus seven | Untreated, HIV-negative tissue validation; [GSE174443](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174443) |
| Pollara et al. tuberculin skin-test bulk transcriptomics | HIV-negative active/latent TB participants, antigen and saline conditions; cohort size and accession: Not specified in paper | In-vivo antigen-response comparison; cited Pollara et al. (2021), Figure 6C |
| Protein-level validation | Fibroblast IHC in two patients; flow cytometry in five patients; macrophage IHC in two independent donors | Orthogonal tissue localization and marker validation; donor sets must not be assumed disjoint or pooled into a total |

For rows without complete metadata, this summary does not reconstruct missing counts from plots. The separately linked source studies and supplementary specimen tables should be checked before data acquisition or pooled analyses.

## Experimental Procedure

- Collect and annotate resected lung tissues, including TB status, treatment context, HIV status, and tissue pathology.
- Generate Seq-Well S3 single-cell profiles, apply quality control, and define broad populations and cellular subsets.
- Compare fibroblast states with HLCA references and identify differential-expression and coexpression programs.
- Evaluate selected programs in independent lymph-node, macaque, and skin-challenge datasets.
- Test marker expression and tissue localization with immunohistochemistry and flow cytometry.
- Use MultiNicheNet and LIANA to nominate signaling relationships, while retaining their status as expression-based predictions.
- Analyze an independent Visium cohort against matched histology, distinguish lesion core, cuff, and surrounding tissue, and compare fibroblast/macrophage spatial signatures.
- Interpret concordant evidence as a basis for targeted validation of the proposed remodeling circuit.

## Key Biology Insights

Fibroblasts may actively organize inflammatory niches through chemokines and matrix-associated signaling, in addition to depositing scar tissue. A fibroblast–SPP1 macrophage neighborhood may link chronic inflammation to structural lung damage. Its presence in post-TB lesions suggests that microbiological treatment and normalization of tissue biology need not coincide.

The results also show why cell abundance and cell state should be analyzed separately. A sparse but transcriptionally active stromal population can contribute prominent inferred signals, and its uneven recovery by dissociation can distort comparisons.

## Implications

For spatial host–microbe studies, prioritize histology-defined lesion boundaries, myofibroblast programs, and SPP1-associated macrophages as candidate neighborhoods. Test whether their association persists after accounting for donor, tissue region, HIV, treatment, and local microbial signal. Use donors as biological replicates and avoid treating thousands of spatial spots as independent patients.

The data support a candidate host-directed therapeutic axis, not an established therapeutic intervention. Key gaps are perturbation evidence, longitudinal persistence, clinical links to lung-function loss, and replication outside surgically selected disease. Distinguishing protective containment from harmful fibrosis is essential before targeting this circuit.
