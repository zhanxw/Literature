# Paper Summary

### Authors
Jesse Zhang, Airol A. Ubas, Valentine Svensson, Nicole Thomas, Vishvak Subramanyam, Christopher Carpenter, Aidan Winters, Richard de Borja, Noam Teyssier, Neha Thakar, Umair Khan, Pooja V. Akella, Harper J. Green, John D. Thompson, Vuong Tran, Joseph Pangallo, Efthymia Papalexi, Ajay Sapre, Hoai Nguyen, Oliver Sanderson, Maria Nigos, Olivia Kaplan, Sarah Schroeder, Bryan Hariadi, Simone Marrujo, Crina Curca, Alec Salvino, Guillermo Gallareta Olivares, Ryan Koehler, Alexander Rosenberg, Charles Roco, Chiara Ricci-Tam, Matthew G. Jones, Alexander Dobin, Brian S. Plosky, Danielle E. Lyons, Daniele Merico, Nima Alidoust, Hani Goodarzi, Johnny Yu

### Journal
Cell, Volume 189, Issue 19, pages 5945–5961.e8

### Publication Date
September 17, 2026

### DOI
[10.1016/j.cell.2026.08.035](https://doi.org/10.1016/j.cell.2026.08.035)

## Keywords
Single-cell RNA sequencing; drug perturbation; cancer cell lines; pharmacology; Mosaic; transcriptomic phenotypes; mechanism of action; drug resistance; virtual cell; AI-ready atlas

## Main Idea
The authors introduce Tahoe-100M, a large single-cell perturbation atlas generated with the Mosaic platform. It contains more than 100 million transcriptomes from 50 multiplexed cancer cell lines exposed to about 1,100 drug-dose conditions. The atlas combines molecular readouts with inferred cellular phenotypes—including survival, cell-cycle arrest, and transcriptomic heterogeneity—to map context-dependent drug responses and provide a resource for predictive models of cell state.

## Evidence Supporting the Main Idea
- Fourteen 96-well plates produced about 153 million profiled cells; after filtering, 100.6 million cells passed minimal filters and 95.6 million passed the full filters used for downstream analyses. The median coverage was 1,287 cells per cell-line–drug–dose condition.
- The final analysis covered 47 cell lines, 379 drugs, 1,135 drug-dose combinations, and 52,886 unique cell-line–drug–dose combinations. The cell lines represented 13 organs of origin and included common cancer alterations such as TP53, KRAS, and CDKN2A.
- The Mosaic design used pooled “cell villages,” SNP-based demultiplexing, and matched DMSO controls. Matched replicate pseudobulk profiles had median Pearson correlation 0.975, while cells separated by cell-line identity rather than plate in the scVI embedding, supporting low plate-related batch effects.
- Drug responses were heterogeneous and context dependent. Examples included selective colorectal vulnerability to JAK/STAT inhibition (β = −0.12, qBH = 4.5 × 10−7) and distinct G1 versus G2/M arrest profiles among nominally related CDK inhibitors.
- Integrating six phenotypic modalities with similarity network fusion produced four robust drug clusters organized mainly by response magnitude and arrest type, rather than by annotated target mechanism.
- Pathway-level Vision scores classified mechanisms of action with F1 > 0.7 for roughly half of drug classes. Elimusertib, annotated as an ATR inhibitor, clustered with MEK inhibitors and suppressed ERK phosphorylation, revealing a likely dominant MEK-like activity.
- An unbiased pathway screen identified compounds including elimusertib and TAK-901 as candidates for immunomodulatory activity. Follow-up assays showed increased MHC class I protein in CFPAC-1 cells and increased surface MHC class I across additional cancer cell lines.
- Adagrasib responses bifurcated into cell-death and adaptive-survival states; the latter showed ER stress and unfolded-protein-response signatures. The authors explicitly describe this result as hypothesis-generating because it was not independently replicated across biological replicate plates.

## Main Novelty
The work scales pooled, genetically resolved single-cell pharmacology to atlas size while retaining deep per-condition coverage. Its central innovation is the unified use of cellular phenotypes and pathway-level molecular phenotypes: this allows drugs to be grouped by convergent biological consequences, mechanisms to be classified from transcriptional responses, and off-target or previously unannotated activities to be discovered.

## Datasets Used for Evaluation
- **Tahoe-100M:** 100.6 million minimally filtered cells and 95.6 million fully filtered cells from 50 starting cancer cell lines; downstream analyses retained 47 lines, 379 drugs, 1,135 drug-dose combinations, and 52,886 unique conditions. It was used for atlas construction, phenotype analysis, MOA classification, drug similarity, and discovery analyses.
- **Cancer Cell Line Encyclopedia and DepMap:** Existing genomic and dependency annotations for the selected cancer cell lines; used to characterize lineage, mutations, and context for interpreting drug responses.
- **Replicate plates 6 and 14:** Matched Mosaic experiments; used to assess reproducibility, batch mixing, and the relationship between cell number and signature concordance.
- **CFPAC-1 and additional cancer cell lines:** Follow-up validation models; used to test drug-induced MHC class I protein and surface-expression changes.
- **MSigDB Hallmark, KEGG, and GO collections:** Gene-set resources used for enrichment analysis of heterogeneous adagrasib response states.

## Experimental Procedure
- Pool genetically distinct cancer cell lines into spheroid “cell villages,” seed 14 plates, and expose wells to small molecules or DMSO controls for 24 hours.
- Dissociate and fix spheroids; generate combinatorially barcoded scRNA-seq libraries with Parse GigaLab; sequence approximately 1.4 trillion raw reads.
- Assign cells to their cell-line origins using SNP-based deconvolution, apply quality filters, and compare treated wells with composition-matched DMSO controls.
- Train scVI embeddings and evaluate plate integration, cell-line preservation, and replicate concordance; sample cells for visualization because the complete atlas is too large to plot directly.
- Derive survival, G1/G2-M arrest, Augur perturbation, Gini occupancy heterogeneity, and transcriptomic heterogeneity measures from single-cell profiles.
- Aggregate six phenotypic modalities across 47 lines at 5.0 μM, fuse drug-similarity networks, and use Leiden clustering to identify convergent response groups.
- Compute pathway activities with Vision; test MOA associations with UMAP/PERMANOVA, classify MOAs with an SVM using 80/20 splits and repeated cross-validation, and use pathway similarity to identify unexpected drug activities.
- Validate selected hypotheses experimentally using western blot and flow cytometry for MHC class I, and western blot for ERK phosphorylation.

## Key Biology Insights
- Drug response is strongly shaped by lineage and genetic context; the same MOA can produce selective vulnerability, resistance, or different cytostatic outcomes across cancer models.
- Cellular consequence is not reducible to target annotation. Drugs with unrelated targets can converge on strong transcriptomic responses or shared cell-cycle checkpoints.
- Molecular phenotypes can expose pharmacology hidden by nominal annotations, as illustrated by elimusertib’s MEK-like response and ERK suppression.
- Single-cell resolution reveals divergent fates within a treated population, including a possible adaptive-survival state linked to ER stress and unfolded-protein response after KRAS G12C inhibition.
- The atlas supports discovery of immunomodulatory activity, including candidate compounds that increase MHC class I expression and could potentially improve tumor immune visibility.

## Implications
Tahoe-100M is an open, structured resource for learning drug-induced cell-state transitions and evaluating AI models on held-out compounds or cell lines. Its factorial design enables tests of generalization to unseen perturbations and contexts, while its single-cell measurements support modeling response distributions and heterogeneity. Biological interpretation should remain bounded: the data use immortalized cancer cell lines, one pooled culture context, small molecules at limited doses, and a single time point. Several inferred phenotypes have only moderate replicate reproducibility and should be confirmed with orthogonal assays. Random condition splits may overestimate predictive performance; whole-compound and whole-cell-line holdouts are more informative.
