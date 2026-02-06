# Antibiotic Resistance Microbiology Dataset (ARMD): A Resource for Antimicrobial Resistance from EHRs

**Authors:** Fateme Nateghi Haredasht, Fatemeh Amrollahi, Manoj V. Maddali, Nicholas Marshall, Stephen P. Ma, Lauren N. Cooper, Andrew O. Johnson, Ziming Wei, Richard J. Medford, Sanjat Kanjilal, Niaz Banaei, Stanley Deresinski, Mary K. Goldstein, Steven M. Asch, Amy Chang, Jonathan H. Chen

**Publication:** Scientific Data 12, 1299 (2025)
**DOI:** https://doi.org/10.1038/s41597-025-05649-7
**Dataset URL:** https://doi.org/10.5061/DRYAD.JQ2BVQ8KP

---

## Main Idea

This paper introduces the **Antimicrobial Resistance Microbiology Dataset (ARMD)**, a comprehensive dataset derived from Electronic Health Records (EHRs) at Stanford Health Care. The dataset combines microbiological culture data, antibiotic susceptibility results, patient demographics, clinical history, and treatment exposures spanning 1999-2024. ARMD addresses the critical global health threat of antimicrobial resistance (AMR) which was associated with nearly 5 million deaths worldwide in 2019.

ARMD bridges laboratory and clinical data to enable both broad surveillance and detailed patient-level analyses. It captures over **280,000 unique patients** with **751,075 microbiological culture records**, representing one of the largest publicly available EHR-derived resources for AMR research.

---

## Main Novelty

1. **Comprehensive Integration**: Unlike existing resources focusing on either genetic determinants (e.g., NDARO, CARD) or population-level surveillance (e.g., NARMS Now), ARMD integrates laboratory microbiology data with rich clinical context including demographics, comorbidities, medication exposures, and socioeconomic factors.

2. **Longitudinal Real-World Data**: The 25-year longitudinal nature (1999-2024) enables temporal trend analysis and captures dynamics of resistance development, including prior antibiotic exposures.

3. **Inclusion of Negative Cultures**: Unlike most datasets that only include positive cultures, ARMD includes records of both positive and negative cultures, serving as valuable indicators for assessing disease severity and understanding patterns of microbial clearance.

4. **Implied Susceptibility Rules**: The dataset incorporates predefined rules to infer antibiotic susceptibility for drugs not directly tested, based on CLSI standards and established microbiological principles.

5. **Multi-dimensional Clinical Context**: Includes the Area Deprivation Index (ADI) for socioeconomic analysis, Elixhauser Comorbidity Index, nursing home visit history, laboratory values, and vital signs.

---

## Main Datasets Used for Evaluation

### Primary Dataset:
- **Source:** Stanford Health Care EHR system (Epic)
- **Time Period:** December 1999 - February 2024
- **Total Cultures:** 751,075 records
- **Unique Patients:** 283,715

### Culture Type Distribution:
| Culture Type | Percentage | Count |
|-------------|------------|-------|
| Urine | 50.0% | ~375,500 |
| Blood | 38.8% | ~291,400 |
| Respiratory | 11.3% | ~84,800 |

### Patient Demographics:
- **Mean Age:** 56.7 years
- **Female Patients:** 66.9% (189,864)
- **Male Patients:** 33.0% (93,763)

### Key Data Tables:
1. Microbiology Cultures - Culture type, organism identification, antibiotic susceptibility
2. Patient Demographics - Age bins, sex, ADI scores
3. Clinical Encounters - Ward information (ICU, ED, inpatient, outpatient)
4. Antibiotic Exposures - Prior antibiotic use with timing relative to cultures
5. Laboratory Values - WBC, lactate, creatinine, hemoglobin, procalcitonin
6. Vital Signs - Heart rate, BP, temperature, respiratory rate
7. Comorbidities - Elixhauser Index, AHRQ CCSR classifications
8. Implied Susceptibility - Derived antibiotic relationships
9. Nursing Home Visits - Up to 90 days prior to culture

---

## Experimental Procedure/Methodology

### Data Acquisition
**EHR System:** Epic at Stanford Health Care
**Data Pipeline:** Chronicles (operational DB) -> Clarity (Oracle relational DB) -> STARR (BigQuery data lake)

**Microbiological Testing:**
- Organism ID: MALDI-TOF mass spectrometry (Bruker Biotyper)
- Susceptibility Testing:
  - Blood/Urine: Vitek2 instrument (bioMérieux)
  - Respiratory: MicroScan WalkAway system (Beckman Coulter)
- MIC Interpretation: Clinical & Laboratory Standards Institute (CLSI) breakpoints

### Inclusion/Exclusion Criteria
- **Included:** Adult patients (≥18 years) with urine, blood, or respiratory cultures
- **Excluded:** Fungal, viral, parasitic cultures; repeated cultures within 2-week period

### Data Standardization & Processing
1. Nomenclature Standardization:
   - Organism and antibiotic names standardized
   - Intrinsic resistance determined using CLSI standards
   - Implied susceptibility inferred using Stanford protocols

2. De-identification (Safe Harbor Method per HIPAA):
   - Ages converted to bins (18-24, 25-34, etc.)
   - Patients ≥89 grouped into "90+" category
   - Sex anonymized as binary (0/1)
   - Temporal jittering applied to all dates
   - Clinical text anonymized using TiDE algorithm

3. Variable Processing:
   - Laboratory metrics summarized (median, Q25, Q75, first/last values)
   - Comorbidities mapped to Elixhauser Index and AHRQ CCSR

### Ethical Considerations
- IRB Approval: Stanford University IRB #70466
- Consent Waiver: 45 CFR 164.512(i)(2)(ii) for de-identified data
- Privacy Oversight: Reviewed by Stanford Privacy Office and Hospital Compliance Office
