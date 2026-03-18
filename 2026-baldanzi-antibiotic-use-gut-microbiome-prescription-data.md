# Paper Summary: Antibiotic use and gut microbiome composition links from individual-level prescription data of 14,979 individuals

### Authors
Gabriel Baldanzi, Anna Larsson, Sergi Sayols-Baixeras, Koen F. Dekkers, Ulf Hammar, Diem Nguyen, Tiscar Graells, Shafqat Ahmad, Camila Gazolla Volpiano, Guillaume Meric, Josef D. Jarhult, Thomas Tangden, Jonas F. Ludvigsson, Lars Lind, Johan Sundstrom, Karl Michaelsson, Johan Arnlov, Beatrice Kennedy, Marju Orho-Melander, and Tove Fall

### Journal
Nature Medicine

### Publication Date
2026 (accepted 11 February 2026; online publication date not specified in PDF)

### DOI
10.1038/s41591-026-04284-y

## Keywords
- antibiotics
- gut microbiome
- shotgun metagenomics
- prescription registry
- clindamycin
- fluoroquinolones
- flucloxacillin
- long-term microbiome disruption

## Main Idea
The study links nationwide individual-level outpatient antibiotic prescription records to fecal shotgun metagenomes from `14,979` adults and shows that oral antibiotic exposure is associated with gut microbiome changes not only within the past year, but also `1-4` and `4-8` years before sampling. The strongest and most persistent associations were concentrated in clindamycin, fluoroquinolones, and flucloxacillin.

## Evidence Supporting the Main Idea
- The analysis combined Swedish prescription-registry data with fecal metagenomes from three population-based cohorts: `SCAPIS` (`n = 8,488`), `SIMPLER` (`n = 4,784`), and `MOS` (`n = 1,707`), for a total of `14,979` individuals.
- Antibiotic exposure was modeled across three windows before fecal sampling: `<1 year`, `1-4 years`, and `4-8 years`, while adjusting for demographic factors, smoking, education, batch effects, BMI, comorbidity burden, polypharmacy, and several non-antibiotic medications.
- Recent exposure had the strongest diversity effects, but significant associations also remained for older exposures. For species richness, each course of clindamycin `<1 year` before sampling was associated with `47` fewer detected species (`q = 2.1 x 10^-17`), while each course of fluoroquinolones and flucloxacillin was associated with `20` and `21` fewer species, respectively.
- Functional regression suggested the fastest recovery in gut microbiome diversity occurred within the first `2` years after antibiotic exposure, with substantially slower recovery afterward.
- In the species-level analysis of `1,340` detectable species, clindamycin, flucloxacillin, and fluoroquinolones accounted for most significant associations (`37.9%`, `25.8%`, and `17.9%` of all `FDR < 5%` associations, respectively).
- Use of these antibiotics `<1 year` before sampling was associated with altered abundance of many species:
  - clindamycin: `296/1,340` species
  - flucloxacillin: `203/1,340` species
  - fluoroquinolones: `172/1,340` species
  - for comparison, penicillin V was associated with only `29` species
- The long-term signal persisted even under a stricter design restricted to people with only one antibiotic course or none in the prior `8` years (`n = 7,664`). A single course of clindamycin, flucloxacillin, or fluoroquinolones `4-8` years before sampling was still associated with `196`, `148`, and `80` species, respectively.
- Negative-control analysis using antibiotic use after fecal sampling showed no association with diversity, supporting the adequacy of confounder adjustment.

## Main Novelty
- Uses registry-grade individual prescription histories rather than self-reported antibiotic exposure.
- Examines long-term microbiome associations at population scale, separating recent from remote antibiotic use over an `8`-year window.
- Shows that even a single outpatient antibiotic course can be associated with detectable microbiome differences years later.

## Datasets Used for Evaluation
- Cohort datasets:
  - `SCAPIS`: `8,488` adults.
  - `SIMPLER`: `4,784` adults.
  - `MOS`: `1,707` adults.
- Exposure dataset:
  - Swedish National Prescribed Drug Register covering outpatient oral antibiotics dispensed since `2005`.
- Microbiome dataset:
  - fecal deep shotgun metagenomic sequencing from all three cohorts.
  - average sequencing depth:
    - `25.3 million` read pairs for SCAPIS Uppsala
    - `26.3 million` read pairs for SCAPIS Malmo and MOS
    - `51 million` read pairs for SIMPLER
- Taxonomic profiling:
  - species abundances generated with `CHAMP` after removal of human reads and mapping to the `Cmbio HMR05` gene catalog.
- Diversity/species analyses:
  - alpha diversity from rarefied species tables
  - species-level modeling on `1,340` species present in more than `2%` of participants

## Experimental Procedure
- Link individual outpatient prescription histories to cohort participants and count oral antibiotic courses in three time windows before fecal sampling.
- Exclude participants with antibiotics in the `30` days before sampling, inflammatory bowel disease, chronic pulmonary disease, and other predefined exclusions.
- Generate fecal shotgun metagenomes, remove host reads, and profile species-level relative abundances.
- Compute alpha diversity metrics including Shannon index, species richness, and inverse Simpson index.
- Fit cohort-specific regression models with extensive confounder adjustment, then combine effect estimates using fixed-effect meta-analysis.
- Repeat analyses by antibiotic class, perform sensitivity analyses with alternative recent-use exclusions and hospitalization exclusions, and use a negative-control exposure after sampling.
- Perform a restricted analysis comparing people with exactly one antibiotic course versus none in the prior `8` years.
- Test associations between antibiotic exposures and the abundance of individual microbial species, and examine age- and sex-specific interactions.

## Key Biology Insights
- Gut microbiome disruption after antibiotics is not limited to the short term; population-level associations can still be detected up to `8` years later.
- Different antibiotic classes leave different microbiome signatures, with clindamycin, flucloxacillin, and fluoroquinolones showing much stronger and broader effects than commonly prescribed penicillin V.
- Long-term changes affect both diversity and the abundance of specific taxa, suggesting persistent ecological shifts rather than only transient reductions in richness.
- The strongest class-specific patterns are consistent with pharmacokinetic and antimicrobial-spectrum differences, including the prominent anaerobe-targeting and biliary-excretion profile of clindamycin.

## Implications
- Antibiotic stewardship may matter not only for resistance control but also for long-term preservation of gut microbiome composition.
- Studies linking antibiotics to cardiometabolic disease, inflammatory bowel disease, or colorectal cancer gain plausibility from these persistent microbiome associations.
- Longitudinal follow-up with repeated microbiome sampling will be needed to separate prolonged recovery from stable ecosystem reconfiguration after exposure.
