---
title: "FDA-Authorized AI/ML Tool for Sepsis Prediction: Development and Validation"
url: "https://www.rama.mahidol.ac.th/ceb/sites/default/files/public/pdf/Repository/DSCI/AIoa2400867.pdf"
date: 2024-11-27
tags:
  - ai
  - healthcare
  - sepsis
  - fda-approved
  - machine-learning
  - clinical-validation
authors:
  - Bhargava, A.
  - López-Espina, C.
  - Schmalz, L.
  - et al.
  - Shapiro, N.I. (corresponding)
journal: "NEJM AI 2024;1(12)"
doi: "10.1056/AIoa2400867"
---

# FDA-Authorized AI/ML Tool for Sepsis Prediction: Development and Validation

**Source:** [NEJM AI](https://www.rama.mahidol.ac.th/ceb/sites/default/files/public/pdf/Repository/DSCI/AIoa2400867.pdf)  
**Published:** November 27, 2024  
**DOI:** 10.1056/AIoa2400867

---

## Main Idea

Sepsis is a life-threatening condition caused by a dysregulated immune response to infection, requiring prompt treatment to improve patient outcomes. However, its heterogeneous presentation makes early detection challenging. This study presents the **Sepsis ImmunoScore**, the first FDA-authorized AI/ML software designed to identify hospitalized patients at risk of sepsis within 24 hours using machine learning analysis of routine clinical data.

---

## Keywords

- Sepsis prediction
- FDA-authorized AI diagnostic
- Machine learning in healthcare
- Risk stratification
- Clinical validation
- Sepsis-3 criteria
- Electronic medical record integration

---

## Main Novelty

1. **First FDA-Authorized AI Sepsis Tool**: The Sepsis ImmunoScore received FDA marketing authorization (de novo pathway) in April 2024, becoming the first AI-based diagnostic tool specifically authorized for sepsis.

2. **Supervised Random Forest Model**: Developed using a calibrated random forest algorithm that predicts sepsis probability within 24 hours using 22 routine clinical parameters.

3. **Four-Tier Risk Stratification**: Categorizes patients into Low, Medium, High, and Very High risk levels with corresponding likelihood ratios (0.1, 0.5, 2.1, 8.3) that strongly correlate with adverse outcomes.

4. **Real-World Integration**: Designed for integration with electronic medical records (EMR) using data available in routine clinical workflows.

---

## Main Datasets Used for Evaluation

### Study Population
**Total Participants**: 3,457 hospitalized adult patients (≥18 years) with suspected infection (indicated by blood culture order)

**Three Cohorts**:
| Cohort | Size | Purpose | Sepsis Rate |
|--------|------|---------|-------------|
| Derivation | n=2,366 | Algorithm development | 32% |
| Internal Validation | n=393 | Same hospitals, second set | 28% |
| External Validation | n=698 | Different hospitals | 22% |

### Study Sites (5 US Institutions)
- Beth Israel Deaconess Medical Center — Boston, MA
- OSF Saint Francis Medical Center — Peoria, IL
- Jesse Brown VA Medical Center — Chicago, IL
- Mercy Health — St. Louis, MO
- William Beaumont University Hospital — Royal Oak, MI
- Carle Foundation Hospital — Urbana, IL

### Enrollment Period
April 2017 to July 2022

---

## Experimental Procedure

### Primary Endpoint
- **Sepsis presence** (Sepsis-3 criteria: suspected infection + SOFA score ≥2 from baseline) within 24 hours of test initiation

### Secondary Endpoints
- In-hospital mortality
- Length of hospital stay
- ICU admission within 24 hours
- Mechanical ventilation use within 24 hours
- Vasopressors use within 24 hours

### Input Parameters (22 Features)

**Demographics**: Age, Sex, Race/Ethnicity

**Vital Signs**: 
- Systolic/diastolic blood pressure
- Heart rate, Respiratory rate
- Inspired oxygen percentage

**Laboratory Tests**:
- White blood cells, Platelets
- Hemoglobin, Hematocrit
- Creatinine, Blood urea nitrogen
- Glucose, Sodium, Potassium
- Albumin, Bilirubin
- Lactate, CRP, Procalcitonin

### Model Development

**Algorithm**: Supervised, calibrated random forest model

**Training**: 3 repeats of 5-fold cross-validation on derivation cohort

**Missing Data**: Imputed using bagged trees

**Calibration**: Out-of-bag predictions calibrated to Sepsis-3 probability

**Risk Categories**: Four thresholds identified during development

### Performance Results

**AUROC (Diagnostic Accuracy)**:
- Derivation: **0.85** (95% CI: 0.83–0.87)
- Internal Validation: **0.80** (95% CI: 0.74–0.86)
- External Validation: **0.81** (95% CI: 0.77–0.86)

**Risk Category Performance (External Validation)**:

| Risk Level | Mortality Rate | ICU Admission | Mechanical Ventilation | Vasopressors |
|------------|---------------|---------------|------------------------|--------------|
| Low | 0.0% | Reference | Reference | Reference |
| Medium | 1.9% | ↑ | ↑ | ↑ |
| High | 8.7% | ↑↑ | ↑↑ | ↑↑ |
| Very High | 18.2% | ↑↑↑ | ↑↑↑ | ↑↑↑ |

### Feature Importance
Interventional SHAP values calculated to assess feature importance in the random forest model.

### Statistical Analysis
- Stratum-specific likelihood ratios (SSLRs)
- Predictive values (PVs)
- Cochran-Armitage trend test for monotonic relationship
- AUROC with binomial approximation (95% CI)
- R statistical software version 4.2.1

---

## Key Findings

1. **High Accuracy**: AUROC ~0.80–0.85 across all cohorts, demonstrating consistent diagnostic performance

2. **Strong Risk Stratification**: Clear monotonic relationship between risk categories and adverse outcomes

3. **Mortality Prediction**: In-hospital mortality ranged from 0% (low risk) to 18.2% (very high risk)

4. **Clinical Utility**: Risk scores predicted multiple critical care metrics (ICU transfer, mechanical ventilation, vasopressors)

---

## Notes

- **First of its kind**: As of publication, the first and only FDA-authorized AI diagnostic for sepsis
- **Clinical workflow integration**: Uses data routinely available in Electronic Medical Records
- **Validation approach**: Prospective, multicenter study with both internal and external validation
- **Sample size**: Study powered for AUROC precision with 735+ subjects; enrolled 3,457 total
- **Outcome definition**: Sepsis-3 criteria with expert clinical adjudication for validation cohorts
- **Funding**: Defense Threat Reduction Agency and others
- **Ethics**: Approved under waiver of informed consent (except OSF site)

---

## Citation
```
Bhargava A, López-Espina C, Schmalz L, et al. FDA-Authorized AI/ML Tool for Sepsis Prediction: Development and Validation. NEJM AI. 2024;1(12):AIoa2400867. doi:10.1056/AIoa2400867
```
