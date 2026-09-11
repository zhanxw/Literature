# Paper Summary

### Authors

Xu Shi, Yuqi Zhai, Xianshi Yu, Xiaoou Li, Brian L. Hazlehurst, Denis B. Nyongesa, Daniel S. Sapp, Brian D. Williamson, David S. Carrell, Luesa Healy, Kara L. Cushing-Haugen, Jenna Wong, Shirley V. Wang, James S. Floyd, Kathleen Shattuck, Samuel McGown, Sarah Alam, José J. Hernández-Muñoz, Jie Li, Yong Ma, Danijela Stojanovic, Sudha R. Raman, Sharon E. Davis, Tianxi Cai, Jennifer C. Nelson, and Patrick J. Heagerty.

### Journal

Bioinformatics 42(3), btag107 (2026)

### Publication Date

28 February 2026 (published); 2 March 2026 (online record)

### DOI

10.1093/bioinformatics/btag107

## Keywords

Electronic health records; data harmonization; common data model; coding heterogeneity; code embeddings; federated data networks; FDA Sentinel; healthcare data quality; privacy-preserving statistics.

## Main Idea

Mapping electronic health record (EHR) data to a common data model and coding system does not guarantee that healthcare systems use the codes in the same way. This paper presents an end-to-end, summary-level framework to detect cross-site coding heterogeneity, learn mappings between site-specific medical codes, and validate whether harmonization reduces residual site information. The framework combines adjusted code-frequency comparisons, group-level association tests, code embeddings, embedding-space alignment, similarity-based mapping, and site-classification validation. Applied to two FDA Sentinel partner systems, it exposed substantial coding differences and improved comparability without requiring individual-level data to be exchanged.

## Evidence Supporting the Main Idea

- The diabetes cohort contained 138,706 patients: 74,475 from Kaiser Permanente Washington (KPWA) and 64,231 from Kaiser Permanente Northwest (KPNW), with a mean follow-up of 4.5 years. The two populations had broadly similar demographics and chronic-condition prevalence (Table 1).
- Among 65,935 unique medical codes, adjusted comparisons found significant differences for 8,348 codes (13%). A total of 4,086 codes had a KPWA:KPNW frequency ratio above 5, while 2,744 had a ratio below one-fifth.
- At the grouped-code level, the burden test detected differences in 828 of 2,523 phecode/CPT groups (33%), and SKAT detected differences in 994 groups (39%). More than 125 groups differed by at least five-fold (Fig. 2).
- KPWA used more granular codes in some settings, whereas KPNW used more local and other codes that were not directly represented in common ontologies. Coding differences also varied over time, especially around the 2015 ICD-9/ICD-10 transition and the 2019–2020 period.
- For the cataract example, rotation-based embedding alignment followed by directional similarity (RADS) mapped more-specific KPWA codes to corresponding less-specific KPNW codes. It captured clinically plausible relationships such as right/left-eye-specific cataract codes mapping to an unspecified-eye code (Fig. 3).
- A logistic-regression classifier predicting healthcare-system site from cataract-related codes had cross-validated AUC 0.715 (95% CI 0.709–0.720) before harmonization and 0.586 (0.580–0.592) after RADS mapping. Projection-based and regression-similarity alternatives reduced AUC further to 0.556 and 0.533, respectively.
- Clinical and informatics review supported the interpretation that observed cataract differences reflected coding practices and care-delivery structure: external providers generated 19.76% of KPWA optometry codes and 46.82% of KPWA ophthalmology codes, compared with 2.57% and 0.49% at KPNW.

## Main Novelty

The main contribution is an integrated harmonization pipeline designed for federated networks in which sites share summary-level information rather than patient records. It combines heterogeneity detection, code-embedding construction, embedding-space alignment, code mapping, and empirical validation in one workflow. The site-classification test provides a practical way to assess mapping quality when comprehensive ground-truth code correspondences are unavailable.

## Datasets Used for Evaluation

- **FDA Sentinel diabetes cohort:** Dynamic cohorts were assembled from 2011–2022 at KPWA and KPNW. Eligibility required age 50 or older, at least nine months of enrollment in the eligibility year, diabetes identified using diagnoses, laboratory measurements or medication use, and at least one month of observed data in the following study year. The final analysis included 74,475 KPWA patients and 64,231 KPNW patients (138,706 total). It was used for population comparison and genome-wide-style code heterogeneity testing.
- **Structured EHR code inventory:** The cohort contained 65,935 unique codes: 11,950 ICD-9, 36,538 ICD-10, 7,749 CPT, 59 LOINC, 3,174 HCPCS, 2,100 local, 3,654 other, and 711 revenue codes. KPWA contributed 53,004 unique codes used 57,938,353 times; KPNW contributed 49,761 used 55,876,254 times. These data supported frequency-ratio analysis and embedding construction.
- **Embedding and cataract-mapping subset:** The mapping analysis used 80,379 eligible KPWA patients and 68,484 KPNW patients because it did not require nine months of total follow-up in a qualifying year. It focused on 17 non-rare KPWA cataract codes and 15 KPNW cataract codes for detailed mapping and validation.
- **Clinical review set:** Clinicians and informaticians reviewed mappings for myocardial infarction, heart failure, diabetes, hypertension and cataracts. This was a qualitative validation set; the paper does not specify a separate patient sample size for the review.

## Experimental Procedure

- Map both health systems’ EHR data to the Sentinel Common Data Model and standard coding systems, then assemble comparable annual diabetes cohorts.
- Compare code endorsement frequencies per person-time using adjusted weighted two-sample t-tests; adjust for age, sex, insulin use and Elixhauser comorbidity index and apply Bonferroni correction.
- Aggregate ICD and CPT codes into clinical groups and apply burden tests and SKAT to detect group-level heterogeneity. Summary-level implementations preserve the results of individual-level analyses while limiting data sharing.
- Build site-specific code embeddings from code co-occurrence patterns. Align the embedding spaces using either projection-based alignment (PA) or rotation-based alignment (RA).
- Map KPWA codes to KPNW codes with either cosine/directional similarity or adjusted regression similarity, using top-K matches or a cross-validated similarity threshold. The primary method, RADS, uses rotation alignment plus directional similarity.
- Validate mappings by training a site classifier from cataract-related codes. Effective harmonization should make site prediction approach chance, with AUC near 0.5.
- Compare RADS with PADS and RARS sensitivity analyses, inspect code-frequency refinements, and obtain clinical/informatics review of selected disease groups.

## Key Biology Insights

This is a clinical-informatics rather than a biological study. Its key domain insights are:

- A common data model standardizes schema and terminology but does not standardize local coding behavior, documentation workflows, reimbursement incentives or care-delivery patterns.
- Code substitution and coding granularity can imitate genuine differences in disease burden or treatment, creating measurement error and threatening model portability.
- SKAT is useful when codes within a clinical group change in different directions, while the burden test is more appropriate when effects are assumed to share a direction.
- Code embeddings can recover clinically meaningful relationships from co-occurrence patterns, but mapping direction and reference-site choice affect the result.
- The method should use a PMI-style embedding construction rather than blindly importing NLP preprocessing: zeroing common codes can remove clinically important events such as HbA1c testing.

## Implications

Cross-site EHR studies should treat coding harmonization as a data-quality step before pooled analyses, model transfer or safety surveillance. The proposed workflow is compatible with privacy-preserving distributed networks and could be automated for periodic monitoring as coding practices change. However, reduced site predictability is only a diagnostic signal: residual site information may reflect real population or care differences as well as coding artifacts. The study used two related healthcare systems and one diabetes cohort, mapped KPWA toward KPNW in one direction, and lacked publicly shareable patient-level data or universal ground-truth mappings. Broader validation across more heterogeneous sites, conditions, time periods and bidirectional mappings is needed before treating the learned correspondences as clinically definitive.
