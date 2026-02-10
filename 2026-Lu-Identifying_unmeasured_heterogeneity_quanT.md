# Identifying unmeasured heterogeneity in microbiome data via quantile thresholding (QuanT)

**Authors:** Jiuyao Lu, Glen A. Satten, Katie A. Meyer, Lenore J. Launer, Wodan Ling, Ni Zhao  
**Journal:** Microbiome  
**Year:** 2026  
**DOI:** 10.1186/s40168-025-02282-9

---

## Main Idea

Microbiome data suffer from both measured (e.g., batch effects) and unmeasured technical heterogeneity due to differential experimental designs and processing. Existing methods like SVA and RUV were developed for microarray/RNA-seq data and cannot accommodate microbiome-specific characteristics like **sparsity** and **over-dispersion**.

This paper introduces **QuanT (Quantile Thresholding)**, a novel non-parametric approach specifically tailored for identifying unmeasured heterogeneity in microbiome data.

---

## Key Novelty

QuanT applies **quantile regression across multiple quantile levels** to threshold microbiome abundance data and uncover latent heterogeneity using thresholded binary residual matrices. The method:

1. Uses quantile regression to model abundance distributions
2. Creates binary residual matrices at multiple quantile thresholds
3. Identifies latent heterogeneity patterns through SVD on these residual matrices
4. Produces **Quantile Surrogate Variables (QSVs)** for downstream analyses

Unlike SVA/RUV which assume Gaussian distributions, QuanT handles the zero-inflated, over-dispersed nature of microbiome count data without distributional assumptions.

---

## Datasets Used

The paper validates QuanT using:

1. **Synthetic datasets** - Generated using MIDASim simulator
2. **CARDIA (Coronary Artery Risk Development in Young Adults)** - Longitudinal multi-center study with cardiovascular health outcomes
3. **HIVRC (HIV Microbiome Re-analysis Consortium)** - Gut microbiome data from HIV patients and controls
4. **CRC (Colorectal Cancer)** - Multi-cohort data for disease classification
5. **IBDMDB (Inflammatory Bowel Disease Multi-omics Database)** - IBD patient samples
6. **MOMS-PI (Multi-Omic Microbiome Study: Pregnancy Initiative)** - Vaginal microbiome data

---

## Experimental Procedure

### Simulation Studies
- Generate synthetic microbiome data with known heterogeneity patterns
- Compare QuanT against SVA, RUVreg, RestrictedSVA, and raw uncorrected data
- Evaluate heterogeneity detection accuracy and false discovery rate control

### Real Data Applications
1. **Prediction Analysis** - Assess classification accuracy for disease prediction
2. **Differential Abundance Testing** - Compare detection of differentially abundant taxa
3. **Community-level Diversity Analysis** - Evaluate impact on alpha-diversity measures

### Metrics
- ROC-AUC for disease prediction
- Number of differentially abundant taxa detected
- Principal Coordinate Analysis (PCoA) for batch visualization
- Kolmogorov-Smirnov and Anderson-Darling tests

---

## Key Results

QuanT demonstrates **superior performance** in:
- Capturing and mitigating unmeasured heterogeneity
- Improving downstream prediction analysis accuracy
- Enhancing differential abundance testing by reducing false positives
- Better control of community-level diversity evaluations

Particularly effective for multi-center studies and meta-analyses.

---

## Conclusion

QuanT is a valuable tool for comprehensive identification of unmeasured heterogeneity in microbiome research. Its non-parametric approach is specifically designed for the unique characteristics of microbiome abundance data.

---

## Abbreviations

| Abbreviation | Full Name |
|--------------|-----------|
| SVA | Surrogate Variable Analysis |
| RUV | Remove Unwanted Variation |
| SVD | Singular Value Decomposition |
| QSV | Quantile Surrogate Variables |
| VOI | Variable of Interest |
| CARDIA | Coronary Artery Risk Development in Young Adults |
| CVD | Cardiovascular Disease |
| ROC-AUC | Area Under Receiver Operating Characteristic Curve |
| PCoA | Principal Coordinate Analysis |
| HIVRC | HIV Re-analysis Consortium |
| CRC | Colorectal Cancer |
| IBDMDB | Inflammatory Bowel Disease Multi-omics Database |
| MOMS-PI | Multi-Omic Microbiome Study: Pregnancy Initiative |
| DM | Dirichlet-Multinomial |

---

## Citation

Lu, J., Satten, G.A., Meyer, K.A., Launer, L.J., Ling, W., Zhao, N. Identifying unmeasured heterogeneity in microbiome data via quantile thresholding (QuanT). *Microbiome* (2026). https://doi.org/10.1186/s40168-025-02282-9
