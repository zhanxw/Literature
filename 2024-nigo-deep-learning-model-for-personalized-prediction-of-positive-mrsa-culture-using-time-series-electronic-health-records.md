# Paper Summary

### Authors

- Masayuki Nigo, Laila Rasmy, Bingyu Mao, Bijun Sai Kannadath, Ziqian Xie, and Degui Zhi

### Journal

- Nature Communications, volume 15, article 2024

### Publication Date

- March 6, 2024

### DOI

- https://doi.org/10.1038/s41467-024-46211-0

## Keywords

- methicillin-resistant *Staphylococcus aureus* (MRSA)
- electronic health records
- time-series prediction
- recurrent neural network
- gated recurrent unit
- antimicrobial stewardship
- empirical antibiotic therapy
- external validation
- MIMIC-IV
- personalized risk stratification

## Main Idea

- The study develops PyTorch_EHR, a gated recurrent unit (GRU) recurrent neural network that uses the sequence and timing of routinely collected categorical EHR events to predict whether a patient will have an MRSA-positive culture within two weeks of an index culture.
- In retrospective internal and external evaluations, PyTorch_EHR discriminated MRSA-positive events better than logistic regression (LR) and Light Gradient-Boosting Machine (LGBM), while predefined high- and low-risk strata suggested potential opportunities to start MRSA-active therapy earlier or avoid unnecessary therapy.
- The model predicts culture positivity rather than proven clinical infection. Its proposed treatment benefits are retrospective counterfactual estimates, not evidence that model-guided care improves patient outcomes.

## Evidence Supporting the Main Idea

- **Overall discrimination (Table 4 and Supplementary Figure 5):** In the Memorial Hermann Hospital System (MHHS) test data, PyTorch_EHR achieved an AUROC of 0.911 (95% CI, 0.900-0.916), compared with 0.892 (0.885-0.899) for LGBM and 0.857 (0.849-0.865) for LR. In MIMIC-IV, the corresponding AUROCs were 0.859 (0.849-0.869), 0.838 (0.823-0.849), and 0.816 (0.804-0.828).
- **External transfer:** Fine-tuning an MHHS-pretrained PyTorch_EHR model on MIMIC-IV produced an AUROC of 0.860 (0.850-0.871), essentially matching the model trained and tested within MIMIC-IV (0.859). This supports transportability after local mapping and fine-tuning, but not plug-and-play deployment without adaptation.
- **Clinically relevant subgroups (Table 4):** PyTorch_EHR retained moderate-to-good discrimination in sepsis, bacteremia, pneumonia, and skin/soft-tissue infection. AUROCs ranged from 0.804 to 0.879 in MHHS and from 0.783 to 0.819 in MIMIC-IV; not every comparison with LGBM was statistically significant.
- **Time-to-event separation (Figure 1):** Model-defined high- and low-risk groups showed clearly separated cumulative incidence curves over the two-week prediction window. MRSA-positive culture incidence in the high-risk group reached 61.2% in MHHS and approximately 18.2% in MIMIC-IV. The lower external incidence reflects the much lower MRSA prevalence in MIMIC-IV.
- **Value of longitudinal history (Supplementary Figures 4 and 10):** PyTorch_EHR performance improved and surpassed LR and LGBM more clearly among patients with repeated index events and longer observable histories. LGBM performed better for the first MHHS event, indicating that the deep model's advantage depends partly on accumulated longitudinal information.
- **Rule-out performance (Supplementary Table 4):** At study-selected low-risk thresholds, PyTorch_EHR had 95.0% sensitivity and 98.6% negative predictive value (NPV) in MHHS, and 90.0% sensitivity and 99.8% NPV in MIMIC-IV. The very high MIMIC-IV NPV should be interpreted in light of the low prevalence of positive events.
- **Rule-in performance (Supplementary Table 4):** At high-risk thresholds chosen for 95% specificity in MHHS and 99% specificity in MIMIC-IV, sensitivities were 48.1% and 19.3%, and positive predictive values were 65.6% and 22.4%, respectively. High-risk predictions therefore enriched for MRSA but missed many positives, especially in MIMIC-IV.
- **Potential stewardship impact (Table 5):** Among true-negative low-risk events, clinicians administered MRSA-specific agents in 1,505 of 6,975 MHHS events and 1,069 of 45,533 MIMIC-IV events, representing 7,949 and 1,397 potentially avoidable doses. Conversely, 98 MHHS and 108 MIMIC-IV low-risk events were false negatives, including 23 and 27 events in which clinicians did administer MRSA-specific therapy.
- **Potential earlier treatment (Table 5):** Among high-risk events, 497 of 1,437 in MHHS and 189 of 957 in MIMIC-IV were true positives that had not received empirical MRSA-specific therapy. However, model-guided treatment of all untreated high-risk events could also expose 227 and 671 false-positive events, respectively, to unnecessary MRSA-specific agents.
- **MRSA bacteremia enrichment (Table 5):** MRSA bacteremia occurred in 31.8% of high-risk versus 0.5% of low-risk MHHS events and 7.3% versus 0.04% of corresponding MIMIC-IV events. Yet sensitivity for MRSA bacteremia was only 50% in MIMIC-IV, and LGBM produced a larger estimated net benefit for that external bacteremia analysis.
- **Patient-level explanation (Supplementary Figures 7-9):** Integrated gradients highlighted MRSA-related admission diagnoses, including cutaneous abscesses, and visualized the day-specific contribution of events for individual predictions. The authors caution that these contributions explain model output and should not be interpreted as causal or population-level risk factors.

## Main Novelty

- Uses a broad set of routinely available structured EHR categories and preserves the timing of events rather than reducing history to a small list of static risk factors or arbitrary look-back windows.
- Predicts any MRSA-positive culture arising over a clinically motivated two-week window, rather than limiting the target to the index culture or to one infection syndrome such as pneumonia.
- Evaluates the same model across two geographically distinct health systems with substantially different patient mix, feature density, and MRSA prevalence.
- Connects discrimination metrics to retrospective estimates of antibiotic starts, avoided MRSA-active doses, missed cases, and bacteremia detection, making the clinical tradeoffs more explicit than AUROC alone.
- Provides patient-level temporal attributions through integrated gradients and releases the PyTorch_EHR/MRSA source code for further evaluation.

## Datasets Used for Evaluation

- **Memorial Hermann Hospital System (MHHS), Houston, Texas:** Retrospective EHR data from January 2018 through April 2021 for adults aged 18 years or older with at least one bacterial culture. The Results report 26,233 unique eligible patients and 56,233 index-culture events. Descriptive MRSA and non-MRSA group memberships were 8,164 and 22,393 patients, respectively; patients could appear in both groups at different times. This dataset was used for model development, internal testing, comparison with LR and LGBM, and clinical-impact analyses.
- **MIMIC-IV version 2.1, Boston, Massachusetts:** Deidentified EHR data from a tertiary academic medical center, used for external validation. The Results report 152,979 unique eligible patients and 393,713 index-culture events; descriptive group memberships were 4,107 MRSA and 152,006 non-MRSA patients, with possible overlap across time. MIMIC-IV was used both to train a local model and to fine-tune and test the MHHS-pretrained model.
- **Test-set sizes inferred from the reported confusion matrices:** 11,922 events in MHHS (1,960 MRSA-positive and 9,962 MRSA-negative) and 78,548 events in MIMIC-IV (1,106 positive and 77,442 negative). The full datasets were divided 70:10:20 for training, validation, and testing.
- **Input content:** Demographics; encounter setting and duration; ICD-9/10 diagnoses; CPT procedures; administered antimicrobials and routes; approximately 150 infectious-disease-related tests; culture orders, sources, and prior results; organism identities; and susceptibility results known by the index time. Admission-diagnosis strings were unavailable in MIMIC-IV.
- **Access:** MIMIC-IV v2.1 is available through PhysioNet after a data-use agreement. MHHS data are not public because of sensitivity and require author contact plus institutional approval.

## Experimental Procedure

1. Identify adult patients with bacterial cultures in MHHS and MIMIC-IV and define each eligible first culture in a two-week window as an index event. Label an event positive when an MRSA-positive culture occurs during that window; allow a patient to contribute multiple temporally distinct events.
2. Extract structured events occurring before or known by the index time. Include a laboratory order if placed by the index time but exclude results reported later, thereby reducing label leakage; for MIMIC-IV, use diagnosis and procedure codes only from prior encounters because those codes are aggregated at encounter level.
3. Clean and map source-specific data into shared categorical features. Generalize care locations to categories such as emergency department and intensive care, and restrict MIMIC-IV inputs to features that can be mapped to MHHS.
4. Represent each patient trajectory as embedded clinical events plus the elapsed days between visits. Train PyTorch_EHR with a GRU recurrent neural network to predict MRSA-positive culture within two weeks.
5. Construct LR and LGBM comparators using, for each feature, its prior occurrence count and time since its most recent occurrence. Standardize numeric inputs and optimize hyperparameters for all models with Optuna.
6. Split each dataset 70:10:20 into training, validation, and test partitions. Evaluate a model trained within each dataset and, for MIMIC-IV, a version initialized from the MHHS model and fine-tuned locally.
7. Compare AUROCs and 95% confidence intervals; use the DeLong test to assess pairwise AUROC differences. Repeat evaluation in sepsis, bacteremia, pneumonia, and skin/soft-tissue infection subgroups and according to the number of repeated index events.
8. Use a GRU-modified DeepSurv architecture to model the cumulative incidence of MRSA-positive cultures over the two-week window.
9. Define high- and low-risk thresholds according to prespecified operating points: 95% specificity and 95% sensitivity in MHHS, and 99% specificity and 90% sensitivity in MIMIC-IV because of stronger class imbalance.
10. Compare model strata with actual culture outcomes and clinicians' empirical MRSA-active prescribing. Estimate potential earlier treatment, avoidable therapy, delayed therapy, and performance specifically for MRSA bacteremia.
11. Apply integrated gradients to clinical events and their timing, summarize frequent feature contributions, and manually review patient-level temporal explanations in 10 example patients.

## Key Biology Insights

- MRSA-positive events were associated with clinical patterns consistent with invasive or tissue-based staphylococcal disease: bacteremia and skin/soft-tissue infection were more common in MRSA than non-MRSA groups in both datasets.
- The model's high-risk strata were strongly enriched for MRSA bacteremia, suggesting that longitudinal EHR patterns contain information related not only to culture positivity but also to severe invasive disease. This is an association within retrospective data, not proof that the model detects biological virulence or infection severity directly.
- Prior organisms, culture sources, susceptibility findings, antibiotic exposures, diagnoses, and care settings jointly encode host vulnerability, colonization history, healthcare exposure, and antimicrobial selection pressure. PyTorch_EHR can combine their timing without requiring a single fixed look-back period.
- The study does not include pathogen genomes, resistance genes, strain typing, host biomarkers, vital signs, or basic laboratory values. It therefore cannot identify the molecular mechanism of methicillin resistance, distinguish acquisition from endogenous infection, or establish causal biological risk factors.
- A positive MRSA culture may represent infection, colonization, or contamination depending on source and context. The bacteremia analysis offers a more specific infection endpoint, but the primary target remains culture positivity from any source.

## Implications

- A locally validated time-series EHR model could support empirical antibiotic decisions by identifying low-risk patients in whom MRSA-specific therapy may be withheld or stopped and high-risk patients who may benefit from earlier coverage.
- The operating threshold must reflect local MRSA prevalence and the relative harm of missed infection versus unnecessary treatment. External results show that excellent NPV can coexist with low PPV and low sensitivity in a highly imbalanced population.
- The model should augment rather than replace clinical judgment: it predicts culture positivity, does not identify the culture source, and omitted important variables such as long-term-care residence, vital signs, and routine laboratory measurements.
- Reported clinical benefits are simulated from retrospective prescriptions and culture outcomes. Prospective impact studies are needed to determine whether model-guided decisions reduce antibiotic exposure, nephrotoxicity, *Clostridioides difficile* infection, treatment delay, length of stay, or mortality.
- Generalizability remains incomplete despite validation in two US regions. Deployment would require local feature mapping, calibration, threshold selection, workflow integration, monitoring for data drift and subgroup performance, and validation in populations such as immunocompromised patients.
- The deep model's advantage was greatest when richer longitudinal histories were available; in sparse first-event histories, a simpler boosted-tree model may perform as well or better and may be easier to implement and interpret.
