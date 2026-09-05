# Paper Summary

### Authors

Dongkwan Shin, Jonghoon Lee, Jeong-Ryeol Gong, and Kwang-Hyun Cho

### Journal

*Nature Communications*, Volume 8, Article 1270

### Publication Date

November 2, 2017

### DOI

[10.1038/s41467-017-01171-6](https://doi.org/10.1038/s41467-017-01171-6)

## Keywords

Not specified in paper. Relevant concepts include colorectal cancer, somatic mutations, network propagation, protein–protein interaction networks, cooperative mutation effects, percolation transition, cancer hallmarks, driver mutations, passenger mutations, and tumor evolution.

## Main Idea

The paper proposes that somatic mutations cooperate at the molecular-network level during colorectal tumorigenesis. Each mutation's influence is diffused through a patient-specific protein–protein interaction (PPI) network, producing a local mutation-propagating module. As mutations accumulate, some modules connect into a giant cluster (GC) that covers a substantial part of the network. Because genes in this cluster are enriched for coordinated cancer phenotypes, the authors call the mature structure a giant percolated cluster (GPC).

The authors argue that colorectal cancer evolution resembles a percolation transition: dispersed mutation effects remain partly disconnected until a mutation links them into a large connected structure associated with multiple cancer hallmarks. Simulated mutation-ordering rules further suggest that the commonly reported sequence of colorectal driver mutations can delay module overlap early but ultimately produce a sharp increase in GPC size. This is a computational model of tumor evolution derived from cross-sectional tumors, not direct longitudinal observation of a transition within patients.

## Evidence Supporting the Main Idea

- **Large connected mutation-effect regions:** In 191 TCGA colorectal tumors, the largest propagated cluster typically covered approximately 20–40% of a 10,968-gene patient-specific network, despite an average of only about 20–40 retained mutations per patient (Figure 1b). This indicates that network diffusion greatly extends the apparent joint influence of the mutations.
- **Nonrandom topology:** Patient GCs were significantly larger than clusters generated from 1,000 random mutation sets matched to each patient's mutation count (Figure 1c). The effect persisted over multiple influence thresholds and was particularly evident when cancer-related or driver genes were examined (Supplementary Figures 1 and 2).
- **Cross-cohort and pan-cancer consistency:** Larger-than-random GCs were also observed in an independent DFCI colorectal cohort (`n = 526`) and in eight TCGA solid-tumor types—BLCA, BRCA, HNSC, KIRC, LUAD, LUSC, PAAD, and STAD (Supplementary Figure 3). The main article does not report the sample size of each additional TCGA cohort.
- **Module-level cooperation:** Mutated genes had higher network degree and shorter pairwise distances than random nodes (Figure 2a,b). For most patients, 55–70% of sampled mutation-module pairs were classified as synergistic, whereas only 10–20% directly overlapped (Figure 2d). Here, “synergy” is a network-geometric definition: the joint connected module is larger than the union of the two individual modules; it is not an experimentally measured genetic interaction.
- **Co-occurring driver pairs:** Among 382 mapped driver genes, the authors identified 479 significantly co-occurring mutation pairs and 14 mutually exclusive pairs. Co-occurring pairs were enriched for overlapped and/or synergistic propagated modules, with nearly half being non-overlapping but network-synergistic (Figure 2e).
- **Recovery of established colorectal subtypes:** Hallmark enrichment within each patient's GC, followed by factor analysis and k-means clustering, produced four clusters strongly associated with the four consensus molecular subtypes: Cluster 1–CMS2, Cluster 2–CMS4, Cluster 3–CMS1, and Cluster 4–CMS3 (Figure 4a–c). The corresponding factors represented proliferation/Myc, angiogenesis/metastasis, immune response, and metabolism.
- **Tumor-stage associations:** Twelve selected hallmark gene sets separated three clusters enriched for stages 1, 2, and 3 (Figure 4d–g). Stage-associated signals included DNA repair in stage 1; WNT/β-catenin, Notch, and apical junction in stage 2; and unfolded-protein response and p53 pathway in stage 3. Two other clusters comprising 48 patients were not significantly associated with stage, so the separation was incomplete.
- **MSI/MSS biology:** Immune scores derived from GPC hallmark enrichment differed significantly between microsatellite-instable and microsatellite-stable tumors and agreed directionally with established immune-infiltration and tumor-purity scores (Supplementary Figure 14).
- **Mutation-order simulations:** Applying three mutation-selection rules to 129 patients generated 3,834 possible sequences. Rules that minimized early overlap recovered the familiar ordering in which APC occurs early, KRAS precedes later drivers, and TP53 occurs late; examples included APC → KRAS → PIK3CA → TP53 and APC → KRAS → SMAD4 → TP53 (Figure 5d–g).
- **Simulated percolation behavior:** In the illustrated patient, a commonly observed driver sequence produced a sudden rise in GPC size, while a rule that always maximized cooperation enlarged the cluster earlier and more gradually (Figure 5h). Similar behavior in patients with few driver mutations supported the authors' interpretation that passenger mutations can also help connect the network (Supplementary Figures 18 and 19).
- **Tumor-heterogeneity sensitivity:** In a small multiregion analysis, the bulk GPC exceeded the union of subclone GPCs by 23% for the more heterogeneous CRC2 tumor versus 15% for CRC3 (Supplementary Figure 20). This result is illustrative because only two tumors were analyzed.

## Main Novelty

- Recasts the combined consequences of somatic mutations as a percolation problem on a molecular interaction network.
- Defines mutation-propagating modules, a largest connected GC, and a phenotype-associated GPC at the individual-patient level.
- Integrates each patient's expression profile into PPI edge weights before propagating that patient's mutations, making the network context patient specific.
- Connects network geometry to recognizable biological states by recovering colorectal consensus molecular subtypes, tumor-stage-associated pathways, and MSI/MSS immune differences.
- Models how competing pressures—minimizing early overlap while preserving or later maximizing connectivity—could generate common driver-mutation orders and an abrupt network transition.
- Highlights a possible collective role for passenger mutations, whose propagated effects may connect pathways dominated by canonical drivers.

## Datasets Used for Evaluation

- **TCGA COADREAD primary cohort:** Firehose data included somatic mutations for 223 colorectal tumors and RNA-seq expression for 263. Tumors with 300 or more retained mutations were excluded because their propagated clusters nearly saturated the network, leaving 198; 191 tumors had both mutation and expression data and formed the primary analysis set. Clinical annotations included tumor stage, consensus molecular subtype, and MSI/MSS status.
- **DFCI colorectal cohort:** Somatic mutation profiles from 526 patients obtained through cBioPortal. Because patient-level expression was unavailable, the authors used the average TCGA colorectal expression profile to construct a shared colon-cancer-weighted network. This cohort supported external testing of above-random GC size but not fully patient-specific propagation.
- **Additional TCGA cancers:** Paired RNA-seq and somatic-mutation data for bladder urothelial carcinoma, breast invasive carcinoma, head and neck squamous cell carcinoma, kidney renal clear cell carcinoma, lung adenocarcinoma, lung squamous cell carcinoma, pancreatic adenocarcinoma, and stomach adenocarcinoma. Per-cancer sample sizes are not specified in the main paper.
- **Multiregion colorectal sequencing:** Published whole-exome mutation profiles from five colorectal tumors. Two tumors, CRC2 and CRC3, each containing five sampled subclones, were selected for an illustrative heterogeneity analysis.
- **Human PPI network:** A STRING v9.0-derived network initially containing 12,233 proteins; its largest connected component had 12,071. Intersecting it with the paired colorectal molecular data produced the final 10,968-gene analysis network.
- **Gene reference sets:** 1,687 network-mapped cancer-related genes from a 2,102-gene compilation and 382 network-mapped driver genes from a published list of 418. Driver genes represented approximately 5–10% of retained mutations per patient; the broader cancer-gene set represented approximately 20–25%.
- **Phenotype reference sets:** Fifty MSigDB hallmark gene sets were used for enrichment and factor analysis. Published CMS labels, tumor stages, MSI/MSS status, immune scores, leukocyte scores, ESTIMATE, ABSOLUTE, consensus purity estimates, and histologic estimates were used for biological comparisons.

## Experimental Procedure

- **Curate somatic variants:** Lift TCGA colorectal coordinates to hg19, annotate variants with ANNOVAR, and retain nonsynonymous variants supported as damaging by at least two of SIFT, PolyPhen-2 HVAR, MutationTaster, MutationAssessor, and CADD, plus specified stop-gain and frameshift classes.
- **Select tumors:** Exclude TCGA colorectal tumors with at least 300 retained mutations and keep the 191 cases with matched mutation, expression, and clinical information.
- **Construct patient-specific networks:** Begin with the STRING-derived PPI network and weight each interaction between genes `i` and `j` by the product of their expression values, `E(i)E(j)`, within each patient.
- **Propagate mutation influence:** Encode each patient's mutations as binary seeds and perform random walk with restart on the degree-normalized network using diffusion parameter `α = 0.7`.
- **Define modules and clusters:** At a chosen influence threshold—commonly `V = 0.001`—retain the network neighborhood affected by each mutation as a mutation-propagating module. Identify connected modules and define the largest as the GC/GPC.
- **Test nonrandomness:** For each patient, compare observed GC size with 1,000 random mutation profiles matched for mutation count. Repeat across thresholds, cancer/driver-only mutation subsets, DFCI colorectal tumors, and eight other cancer types.
- **Quantify pair relationships:** Measure module overlap with the Jaccard index and define network synergy as the size of the joint connected module divided by the union of the two independent modules. Compare patient mutation pairs and 479 statistically co-occurring driver pairs with matched random pairs.
- **Annotate cancer phenotypes:** Test each patient's GPC against 50 MSigDB hallmark sets using hypergeometric enrichment, producing a 191 × 50 matrix of standardized `-log(p)` values.
- **Recover molecular subtypes:** Reduce hallmark scores with factor analysis (`k = 5` selected using Kaiser and parallel-analysis criteria), cluster factor scores with k-means, and test cluster enrichment for published CMS classes.
- **Analyze tumor stage and MSI:** Use minimum-redundancy maximum-relevance feature selection and k-means clustering to identify stage-associated hallmark patterns; construct hallmark-based immune scores and compare MSI with MSS tumors.
- **Simulate mutation accumulation:** In 129 tumors with more than two driver mutations and at most 65 total mutations, generate mutation orders under three rules: minimize topological overlap, maximize connected-module size, or minimize connected-module size subject to existing overlap. Compare the inferred ordering of APC, KRAS, PIK3CA, SMAD4, and TP53 and track GPC size as mutations accumulate.
- **Assess heterogeneity:** Compare GPCs from individual subclones with the GPC inferred from pooled bulk mutations in two multiregion colorectal tumors.

## Key Biology Insights

- The biological consequence of a tumor's mutations may depend on their collective network placement, not simply on mutation count or the identity of the most prominent driver.
- Co-occurring mutations often affect distinct but connectable signaling neighborhoods. Limited direct overlap can avoid functional redundancy, while network connectivity allows their effects to converge.
- Passenger mutations may contribute collectively by extending or linking driver-centered perturbation modules, even if no single passenger mutation has a strong autonomous phenotype.
- GPC hallmark patterns recapitulated core colorectal phenotypes: immune activation in CMS1, canonical/Myc-associated proliferation in CMS2, metabolism in CMS3, and angiogenesis/mesenchymal programs in CMS4.
- Stage-linked GPC signals are consistent with a proposed progression from genomic instability and repair defects, through proliferative WNT/Notch programs, to stress-response and metastatic programs. These are cross-sectional associations and do not establish a universal temporal sequence.
- Intratumor heterogeneity can inflate the apparent network cooperation inferred from bulk sequencing because mutations residing in different subclones may be modeled as if they coexist in one cell.

## Implications

The study offers a systems-level framework for interpreting heterogeneous mutation profiles and suggests that disrupting key connectors in a patient's GPC—or targeting multiple hallmark programs represented within it—could inspire individualized combination therapies. The framework may also help stratify tumors when patients share few exact mutations but converge on similar network regions.

The results are hypothesis-generating rather than clinically validated. Mutation trajectories were reconstructed by ordering mutations already present in cross-sectional tumors, so the paper did not directly observe percolation during tumor evolution. Network “synergy” is a mathematical property, not experimental epistasis; patient-specific edge weights rely on the unvalidated assumption that interaction strength scales with the product of bulk RNA expression; and conclusions depend on PPI coverage, influence thresholds, pathogenicity filters, and clustering choices. Excluding hypermutated tumors may particularly affect MSI-related inference, and the two-tumor subclone analysis is too small for generalization. Prospective longitudinal sequencing, single-cell or spatial data, perturbation experiments, and independent outcome prediction would be needed to establish causal or therapeutic utility.
