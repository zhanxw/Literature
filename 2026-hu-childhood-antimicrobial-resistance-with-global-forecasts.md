# Paper Summary

### Authors
- Yanhong Jessika Hu, Hong Qiu, Joseph I. Harwell, and Penelope A. Bryant

### Journal
- JAMA Pediatrics

### Publication Date
- July 20, 2026 (online publication; funding disclosure corrected August 17, 2026)

### DOI
- https://doi.org/10.1001/jamapediatrics.2026.2808

## Keywords
- pediatric antimicrobial resistance
- WHO priority pathogens
- AWaRe antibiotics
- carbapenem resistance
- cephalosporin resistance
- global surveillance
- intensive care
- sepsis
- generalized additive models
- AMR forecasting

## Main Idea
- This multinational surveillance analysis shows that antimicrobial resistance (AMR) in bacterial isolates from children increased across all world regions from 2004 to 2022, with the fastest and most clinically concerning growth in lower-resource settings, intensive care units, sepsis and respiratory infections, and Gram-negative pathogens.
- If historical trajectories continue, resistance to Watch and Reserve antibiotics is expected to keep rising through 2035. The most severe projections concern carbapenem resistance in *Klebsiella* species and especially *Acinetobacter baumannii*, threatening empiric treatment options for severe childhood infection.

## Evidence Supporting the Main Idea
- **Large pediatric surveillance base:** The study analyzed 106,581 isolates from 106,581 children aged 0 to 18 years in 82 countries over 19 years. Children aged 0 to 2 years contributed 47% of isolates; 27% came from intensive care units (ICUs), and the most common clinical sources were sputum, skin or wounds, and blood (Figure 1).
- **Resistance across the AWaRe hierarchy:** Across pathogens and years, mean resistance to at least one antibiotic in a category was 36% for Access drugs, 22% for Watch drugs, and approximately 13% for Reserve drugs. Category-level resistance increased in every region, even though trajectories varied by pathogen and age (Figure 2).
- **Rapid escalation in high-risk care:** In ICUs, Watch resistance rose from 15% (517/3,564) to 33% (2,910/8,748), while Reserve resistance rose from 9% (69/765) to 32% (1,765/5,520). Among ICU isolates from children aged 0 to 2 years, Watch resistance rose from 12% to 32%.
- **Severe infection syndromes were heavily affected:** Watch resistance increased from 15% to 30% among isolates assigned to sepsis or bloodstream infection and from 12% to 29% among respiratory infection isolates. Reserve resistance rose from 3% to 26% in sepsis and from 9% to 30% in respiratory infection.
- **Resource inequity widened:** Higher- and lower-resource regions began with broadly similar category-level resistance in 2004. By 2022, lower-resource regions had substantially higher resistance than higher-resource regions for Access (47% vs 29%), Watch (48% vs 24%), and Reserve antibiotics (37% vs 25%).
- **Gram-negative pathogens drove the most alarming changes:** *A. baumannii* exceeded 55% resistance in every AWaRe category in 2022. *Klebsiella* species showed particularly rapid increases in third- or fourth-generation cephalosporin and carbapenem resistance, including marked growth in Southeast Asia, Eastern Europe, and the Eastern Mediterranean (Figures 2 and 3).
- **The annualized-rate analysis supports the trend:** Overall annualized resistance increases were significant for cephalosporins in *Escherichia coli* (0.69 percentage points/year) and *Klebsiella* species (1.29 points/year), and for carbapenems in *Klebsiella* (0.72 points/year) and *A. baumannii* (1.74 points/year). Regional effects were heterogeneous; for example, *Klebsiella* carbapenem resistance increased by 3.32 points/year in Southeast Asia (Figure 3).
- **Forecasts indicate further erosion of last-line options:** By 2035, carbapenem resistance was projected to reach 35% (95% uncertainty interval [UI], 29%-40%) in *Klebsiella* and 82% (95% UI, 77%-85%) in *A. baumannii*. Projected cephalosporin resistance reached 56% in *E. coli*, 70% in *Klebsiella*, 71% in *Enterobacter cloacae*, and 83% in *A. baumannii*. Figure 4 visualizes the broad geographic spread expected for carbapenem resistance.

## Main Novelty
- Provides one of the largest child-specific, multinational phenotypic AMR analyses, spanning 82 countries and nearly two decades rather than extrapolating pediatric patterns from adult surveillance.
- Integrates three clinically useful views of resistance: WHO priority pathogens, the WHO AWaRe antibiotic framework, and pediatric subgroups defined by age, clinical setting, infection syndrome, geography, and national resource level.
- Combines historical trend estimation with spatiotemporal forecasts through 2035, including uncertainty intervals, to identify where pediatric empiric therapy is most likely to become unreliable.
- Translates the results into the public-facing **AMR in Kids** visualization platform, intended to make geographically stratified pediatric resistance data more accessible to clinicians, researchers, and policy makers.

## Datasets Used for Evaluation
- **Pfizer Antimicrobial Testing Leadership and Surveillance (ATLAS) dataset:** Deidentified pediatric bacterial isolates collected from January 2004 through December 2022. The data are publicly accessible through Vivli under access ID 00010421 (previously 00009059).
- **Study cohort:** 106,581 isolates from 106,581 children in 82 countries, with samples from blood, cerebrospinal fluid, urine, sterile-site fluids, sputum, skin or wounds, and stool.
- **Reference frameworks, not independent patient datasets:** The 2024 WHO bacterial priority-pathogen list defined organisms of interest; the WHO AWaRe classification grouped antibiotics; WHO regions defined geography; and World Bank income groups were collapsed into higher- and lower-resource strata.
- *Salmonella* species, *Mycobacterium tuberculosis*, and *Shigella* species were excluded because of low isolate counts, while *Neisseria gonorrhoeae* was excluded because of limited pediatric relevance.

## Experimental Procedure
1. Select ATLAS isolates from children aged 0 to 18 years and retain WHO 2024 critical-, high-, and medium-priority bacterial pathogens meeting eligibility criteria.
2. Use centralized minimum inhibitory concentration and susceptibility results interpreted with CLSI or EUCAST breakpoints. Combine intermediate and resistant calls as resistant.
3. Group tested antibiotics into WHO Access, Watch, and Reserve categories. Define category-level resistance pragmatically as resistance to at least one tested antibiotic in that category; confirm robustness with a sensitivity definition based on the median count of resistant antibiotics (95% agreement).
4. Assign isolates to pediatric age bands (0-2, 3-12, and 13-18 years), clinical settings, nine geographic regions, higher- or lower-resource strata, and 10 infection syndromes derived from specimen source, treatment site, age, ICD-10 codes, and published AMR-burden methods.
5. Estimate pathogen-antibiotic resistance by location and year using a two-stage spatiotemporal model. Remove extreme distributional outliers representing less than 0.05% of observations and exclude subgroup cells with fewer than 10 isolates.
6. Test temporal patterns with Cochran-Armitage tests for linear trends and quadratic binomial regression when nonlinear models fit better; require both *P* < .05 and an effect-size threshold above 0.001.
7. For third- or fourth-generation cephalosporins and carbapenems, aggregate resistance into 3-year intervals, fit weighted linear regressions, and estimate annualized rates of change with bias-corrected 95% confidence intervals from 1,000 nonparametric bootstrap replicates.
8. Forecast resistance to 2035 using binomial generalized additive models adjusted for age group and region. Derive 95% UIs from 500 simulation draws; sex was omitted after preliminary analyses found no meaningful difference.

## Key Biology Insights
- The worsening pediatric AMR signal is primarily a Gram-negative problem. Rising cephalosporin and carbapenem resistance in *Klebsiella*, *E. coli*, *E. cloacae*, *Serratia marcescens*, and *A. baumannii* progressively removes major empiric and rescue-treatment options for sepsis and pneumonia.
- *A. baumannii* is biologically and clinically distinct in the dataset: resistance was already high across the AWaRe spectrum and was projected to become extremely high for cephalosporins and carbapenems across many regions. Its environmental persistence and facility-associated transmission make the ICU pattern especially concerning.
- The *Klebsiella* and *E. coli* trajectories are consistent with global expansion of mobile extended-spectrum beta-lactamase and carbapenemase determinants, while cephalosporin resistance in *E. cloacae* and *S. marcescens* can also reflect AmpC-related biology. These mechanisms are biologically plausible interpretations, not findings directly tested by this phenotypic dataset.
- Declining Access resistance in *Staphylococcus aureus* in most regions contrasts with the escalation in Gram-negative organisms, showing that a single global AMR trend cannot represent all pathogen-drug combinations.
- Because the study contains no genomic or molecular data, it cannot distinguish clonal expansion, horizontal gene transfer, antibiotic-selection pressure, infection-control failure, or changes in sampled populations as the cause of an observed resistance trajectory.

## Implications
- Pediatric empiric-treatment guidelines need timely local or regional resistance data. Global AWaRe recommendations may be poorly matched to settings where first-line Access drugs already fail frequently and Watch or Reserve options are also losing activity.
- The sharp ICU, young-child, sepsis, and respiratory-infection signals support prioritizing antimicrobial stewardship, rapid diagnostics, laboratory capacity, infection prevention, and access to child-appropriate formulations in these groups.
- Lower-resource regions face a double burden: faster resistance growth and fewer diagnostic, therapeutic, and infection-control alternatives. Surveillance expansion and equitable access to effective antibiotics should therefore be paired rather than treated as separate policy goals.
- The 2035 estimates are scenario forecasts, not certainties. They assume that historical trends continue and cannot anticipate changes in prescribing, vaccination, diagnostics, stewardship, conflict, health-system disruption, or introduction of new drugs.
- Important limitations constrain interpretation: ATLAS is not population-based; participating sites and isolate-submission practices changed across locations and years; the analysis lacks population denominators, incidence rates, clinical outcomes, antibiotic exposures, and molecular mechanisms; and aggregating resistance as “at least one drug in an AWaRe category” can hide clinically important drug-level differences.
- The study is therefore strongest as a large, standardized warning signal and planning tool. It does not estimate a child's individual treatment-failure risk or prove that the projected changes are causal.
