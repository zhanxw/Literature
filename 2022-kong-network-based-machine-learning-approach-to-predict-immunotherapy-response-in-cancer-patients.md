# Paper Summary

### Authors

JungHo Kong, Doyeon Ha, Juhun Lee, Inhae Kim, Minhyuk Park, Sin-Hyeog Im, Kunyoo Shin, and Sanguk Kim

### Journal

*Nature Communications*, Volume 13, Article 3703

### Publication Date

June 28, 2022

### DOI

[10.1038/s41467-022-31535-6](https://doi.org/10.1038/s41467-022-31535-6)

## Keywords

Not specified in paper. Relevant concepts include immune checkpoint inhibitors, immunotherapy response, network medicine, protein–protein interaction networks, transcriptomic biomarkers, logistic regression, tumor microenvironment, and tumor mutation burden.

## Main Idea

The paper introduces NetBio, a network-guided machine-learning framework for predicting whether a cancer patient will respond to immune checkpoint inhibitor (ICI) therapy. NetBio begins with the molecular target of an ICI—PD-1, PD-L1, or CTLA-4—propagates influence through a human protein–protein interaction (PPI) network, and identifies Reactome pathways enriched among the 200 proteins closest to that target in network space. Patient-specific expression scores for these target-proximal pathways are then used as features in an L2-regularized logistic-regression model.

The study's main claim is that biologically informed pathway features generalize more consistently than expression of the ICI targets themselves, standard tumor-microenvironment markers, purely data-driven pathway selection, and several published response-prediction methods. The approach was tested within cohorts and across independent cohorts spanning melanoma, metastatic gastric cancer, and bladder cancer.

## Evidence Supporting the Main Idea

- **Within-cohort response prediction:** Leave-one-out cross-validation (LOOCV) produced statistically significant NetBio response classifications in all four eligible primary cohorts: Gide and Liu melanoma, Kim gastric cancer, and IMvigor210 bladder cancer (Figure 2a–d). Target-gene expression was predictive in only the Gide cohort and was inversely predictive in the Liu cohort.
- **Comparison with conventional markers:** Across accuracy and F1 comparisons with individual or combined PD-1, PD-L1, CTLA-4, CD8 T-cell, T-cell-exhaustion, cancer-associated fibroblast, and tumor-associated macrophage markers, NetBio performed better in 71 of 72 LOOCV comparisons (98.6%; Figure 2h–o). In 100 repeated 80%/20% Monte Carlo splits, it was significantly better than or equal to the alternatives in 70 of 72 comparisons (97.2%; Supplementary Figure 3).
- **Survival association:** Patients classified by NetBio as responders had significantly longer overall survival in all three cohorts with survival data—Gide, Kim, and IMvigor210—and NetBio also separated progression-free survival in the Gide and Liu cohorts (Figure 2e–g and Supplementary Figure 1). These are associations from predicted response groups, not randomized evidence that the model improves outcomes.
- **Independent-cohort generalization:** A model trained on the Gide melanoma cohort achieved ROC AUCs of 0.79 in Auslander, 0.72 in Prat, and 0.69 in Riaz (Figure 3). By comparison, PD-1 expression reached at most AUC 0.66 across these tests. Training on Liu instead of Gide also favored NetBio in 23 of 26 comparisons (88.5%; Supplementary Figure 7).
- **Cancer-recurrence prediction:** Models trained on Gide or Liu predicted recurrence in the independent Huang melanoma cohort with AUCs of 0.78 and 0.80, respectively (Supplementary Figure 8). The Huang cohort was very small (`n = 13`), so uncertainty is substantial.
- **Published-method benchmarks:** NetBio was better than EASIER, IMPRES, TIDE, TMEsubtypes, and a deep-neural-network approach in 33 of 34 within-study comparisons (97.1%) and 17 of 18 across-study comparisons (94.4%; Supplementary Figures 10 and 11).
- **Network knowledge versus data-only selection:** Across 11 prediction tasks, NetBio significantly outperformed an equally sized set of Reactome pathways selected solely from the training data (`p = 3.3 × 10^-3`, paired two-sided test; Figure 4). The improvement was especially consistent across cohorts, supporting the interpretation that PPI-guided feature selection reduced overfitting.
- **Immune biology concordance:** NetBio-predicted responders in external TCGA cohorts tended to have greater leukocyte/CD8 T-cell infiltration and fewer M2 macrophages (Figure 5). In melanoma, antigen-presentation pathway expression correlated positively with CD8 T-cell proportion (`r = 0.41`), while FGFR-signaling expression correlated negatively (`r = -0.29`). In IMvigor210, chemokine-receptor and Fcγ-receptor activation pathways increased from immune-desert/excluded tumors to immune-infiltrated tumors (Figure 6).
- **Added value beyond tumor mutation burden:** In atezolizumab-treated bladder cancer, TMB-only predictions separated one-year survival by 18.0 percentage points (60.8% versus 42.8%; `p = 2.0 × 10^-3`). Combining TMB with NetBio increased the separation to 22.3 points (64.4% versus 42.1%) and improved the log-rank result to `p = 2.02 × 10^-4` (Figure 7b,c).
- **Mechanistic candidate:** Higher expression of the Raf-activation pathway characterized high-TMB patients reclassified as nonresponders (`p = 3.39 × 10^-2`). In an external TCGA bladder cohort, high Raf activation was also associated with poorer survival among tumors with low PD-L1 expression and high TMB (`p = 0.025`; Figure 7d–f). This supports Raf activation as a hypothesis-generating resistance marker, not a clinically validated causal mechanism.

## Main Novelty

- Uses the network neighborhood of the actual ICI target to constrain biomarker discovery, directly connecting treatment mechanism to feature selection.
- Represents each patient with pathway-level expression rather than isolated genes, making features more biologically interpretable and less sensitive to individual noisy measurements.
- Demonstrates both within-study and cross-study prediction across multiple cohorts, including stress tests with reduced training sizes.
- Integrates network-derived transcriptomic markers with TMB and shows complementary prognostic information.
- Uses feature coefficients and network topology to generate specific biological hypotheses, including antigen presentation, FGFR signaling, chemokine/Fcγ-receptor activity, and Raf activation.

## Datasets Used for Evaluation

### ICI-treated patient cohorts

The authors curated eight previously published cohorts totaling 729 patients; no new patient data were generated.

- **Gide et al. — melanoma (`n = 91`):** Nivolumab, pembrolizumab, and/or ipilimumab; used for LOOCV and as a training cohort for external melanoma predictions.
- **Liu et al. — melanoma (`n = 121`):** Nivolumab or pembrolizumab; used for LOOCV and as an alternative external-prediction training cohort.
- **Kim et al. — metastatic gastric cancer (`n = 45`):** Pembrolizumab; used for LOOCV and survival analysis.
- **IMvigor210 — bladder cancer (`n = 348`):** Atezolizumab; included RNA sequencing, TMB, tumor-proportion scores, immunohistochemistry-based immune phenotypes, and survival data.
- **Auslander et al. — melanoma (`n = 37`):** Anti-PD-1 and/or anti-CTLA-4; independent test cohort.
- **Prat et al. — melanoma (`n = 25`):** Nivolumab or pembrolizumab; independent test cohort after retaining melanoma samples.
- **Riaz et al. — melanoma (`n = 49`):** Nivolumab; independent test cohort using pretreatment expression samples only.
- **Huang et al. — melanoma (`n = 13`):** Pembrolizumab; recurrence/no-recurrence served as the nonresponse/response endpoint.

For most cohorts, complete or partial RECIST response was labeled as response, while stable or progressive disease was labeled as nonresponse. Some analyses used fewer samples than the nominal cohort totals because response or other required measurements were unavailable; for example, Figure 2 displays 119 Liu and 298 IMvigor210 samples with response labels.

### External biological-validation cohorts

- **TCGA-SKCM — melanoma (`n = 103`):** Expression, mutation, immune-contexture, and clinical data used to assess whether melanoma NetBio predictions recapitulated immune biology.
- **TCGA-STAD — stomach adenocarcinoma (`n = 375`):** Used for gastric-cancer immune-contexture analyses.
- **TCGA-BLCA — bladder cancer (`n = 405`):** Used for immune-contexture analyses and external evaluation of the Raf-activation survival association.

These TCGA patients were not reported as ICI-treated and therefore served as biological/prognostic validation rather than direct treatment-response test sets.

### Knowledge resources

- **Human PPI network:** STRING v11.0 interactions with score >700; the largest connected component contained 16,957 proteins and 420,381 edges.
- **Pathway database:** Reactome pathways obtained through MSigDB; single-sample GSEA produced patient-level pathway normalized enrichment scores.
- **NetBio feature sets:** 472 pathways for Gide, 323 for Liu, 292 for Kim, and 353 for IMvigor210, reflecting the relevant ICI targets and enrichment criteria for each cohort.

## Experimental Procedure

- **Curate and harmonize cohorts:** Obtain pretreatment transcriptomic profiles, treatment information, RECIST response or recurrence labels, and available survival/TMB/IHC measurements from eight published ICI cohorts. Normalize count-based datasets with TMM; use available normalized expression for the remaining cohorts.
- **Build the PPI network:** Retain high-confidence STRING v11.0 interactions (score >700) and select the largest connected component of 16,957 nodes and 420,381 edges.
- **Seed ICI targets:** Map PD-1, PD-L1, and/or CTLA-4 to the PPI network according to the therapy received in each cohort.
- **Run network propagation:** Apply personalized PageRank with the ICI targets as seeds and damping factor 0.85; retain the 200 proteins with the highest influence scores (Figure 1a).
- **Identify NetBio pathways:** Test Reactome pathways for overrepresentation among the 200 target-proximal proteins using a hypergeometric test and Holm–Šidák multiple-testing correction; retain pathways with adjusted `p < 0.01` (Figure 1b).
- **Compute patient features:** Use ssGSEA to calculate a normalized enrichment score for every selected NetBio pathway in each tumor transcriptome. Standardize gene/pathway features within each cohort.
- **Train classifiers:** Fit class-balanced L2-regularized logistic regression to responder/nonresponder labels. Tune `C` from 0.1 to 1.0 using fivefold cross-validation within the training data. Support-vector, random-forest, and deep-neural-network variants were explored in supplementary analyses.
- **Conduct within-study validation:** Apply LOOCV to the four cohorts with >30 samples and at least 10 responders and 10 nonresponders; compare accuracy, F1, response enrichment, overall survival, and progression-free survival with target-gene and tumor-microenvironment marker models.
- **Assess robustness to sample size:** Repeat random 80% training/20% testing splits 100 times and compare NetBio with alternative biomarkers.
- **Conduct external validation:** Train on the full Gide or Liu melanoma cohort and test without cohort mixing on Auslander, Prat, Riaz, or Huang. Evaluate ROC AUC and AUPRC.
- **Benchmark alternatives:** Compare NetBio against equally sized data-driven pathway sets, EASIER, IMPRES, TIDE, TMEsubtypes, and a DNN-based predictor.
- **Interrogate biological plausibility:** Apply trained models to cancer-matched TCGA cohorts and correlate prediction scores with TMB, leukocyte fraction, and inferred immune-cell proportions; compare selected pathways with IMvigor210 IHC immune phenotypes.
- **Integrate multi-omic biomarkers:** Combine NetBio pathway scores with TMB in logistic regression, evaluate response-group survival, inspect reclassified patients, and test the Raf-activation signal in TCGA-BLCA.

## Key Biology Insights

- Proteins and pathways near PD-1, PD-L1, or CTLA-4 in the interactome carry response information not captured by expression of the checkpoint genes alone.
- Predicted sensitivity is consistently associated with an immune-active microenvironment: greater leukocyte and CD8 T-cell presence and lower M2-macrophage abundance.
- Different melanoma cohorts implicated different pathways—class I MHC antigen presentation in Gide and low FGFR signaling in Liu—suggesting multiple routes to CD8 T-cell recruitment rather than one universal expression signature.
- Bladder-cancer NetBio features highlighted chemokine-receptor signaling and Fcγ-receptor activation, which agreed with histologic immune-infiltration categories.
- TMB and the tumor transcriptome provide complementary signals. A high mutation burden can coexist with resistance-associated expression programs, such as elevated Raf activation.
- Models trained within the same cancer type generalized better than a model combining melanoma, gastric, and bladder cohorts, supporting cancer-type-specific ICI-response mechanisms.

## Implications

NetBio provides an interpretable framework for prioritizing pretreatment transcriptomic biomarkers when labeled ICI cohorts are small. Its cross-cohort results suggest that constraining features with drug-target network biology can improve portability relative to data-only feature selection. The framework could also complement established genomic markers such as TMB and help generate experimentally testable resistance mechanisms.

Clinical use would require further validation. All cohorts were retrospective, cohort sizes were modest, treatments and response measurements were heterogeneous, and several comparisons reused public datasets rather than testing a locked model prospectively. The feature sets depend on incomplete PPI and pathway databases, and the paper shows reduced performance with a smaller, higher-confidence network. TCGA analyses demonstrate biological concordance but not ICI-response prediction because those patients were not established treatment cohorts. Prospective multi-center validation, calibration, standardized specimen timing, and explicit testing across ancestry, tumor stage, and assay platforms are needed before clinical deployment.
