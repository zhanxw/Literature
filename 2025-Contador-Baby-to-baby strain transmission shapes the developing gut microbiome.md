# Baby-to-baby strain transmission shapes the developing gut microbiome

**DOI:** https://doi.org/10.1038/s41586-025-09983-z

**Published:** Nature, 2025

**Authors:** microTOUCH-baby consortium (Corresponding: Nicola Segata)

---

## Main Idea

This paper presents the **microTOUCH-baby study**, a strain-resolved longitudinal metagenomic investigation of gut microbiome transmission in 43 infants attending nursery for the first time (around 10 months old). The study reveals that **baby-to-baby microbiome strain transmission in nursery settings is extensive and quantitatively more important than previously thought**—after just 3 months, nursery peers contributed more strains to infant microbiomes (28.4%) than family members (20.0%).

## Main Novelty

1. **First comprehensive strain-level tracking of horizontal microbiome transmission in infants outside the household**
   - Previous studies focused primarily on vertical (mother-to-infant) transmission
   - Demonstrates that intra-generational transmission among peers rivals or exceeds inter-generational family transmission

2. **Dense longitudinal sampling design**
   - 1,013 metagenomic samples from 134 volunteers (43 babies, 39 mothers, 30 fathers, 7 siblings, 5 pets, 10 educators)
   - Weekly sampling of babies during nursery attendance
   - Continuous through first term, second term, and summer break

3. **Quantitative transmission network reconstruction**
   - Puppy-to-puppy strain transmission rates: 20.2% by end of first term, 33.3% by end of school year
   - Tracked individual strain transmission chains (e.g., *Akkermansia muciniphila* spreading from baby → baby → parents)
   - Identified "outbreaker" strains reaching >50% prevalence within nurseries

4. **Impact factors on transmission**
   - Siblings significantly increase strain-sharing (~56% SSR at T01) and reduce nursery acquisition
   - Antibiotics affect babies more severely than adults (70.2% strain retention vs 88.4% in adults)

## Datasets

**Cohort:**
- 43 babies (median age at entry: 10 months)
- 39 mothers, 30 fathers
- 7 co-living siblings
- 5 pets
- 10 nursery educators
- 3 public nurseries in Trento, Italy

**Samples:**
- 1,013 stool samples metagenomically sequenced
- Average sequencing depth: 15.61 Gbp
- Timepoints: T01 (before nursery), T02-T15 (weekly during first term), TA (end of year), TB (after summer)

**Analysis:**
- MetaPhlAn 4 for species-level profiling (SGB resolution)
- StrainPhlAn 4 for strain-level phylogenies (311 known SGBs + 201 unknown SGBs)
- Strain-sharing defined by genetic distance below species-specific thresholds
- CRISPR array validation for transmission confirmation

## Experimental Procedure

1. **Study design:**
   - Prospective cohort with dense longitudinal sampling
   - Babies attending nursery ~8 hours/weekday
   - Two classes per nursery, different educators
   - "Settling-in period" (first 2 weeks) with limited attendance

2. **Microbiome profiling:**
   - DNA extraction and shotgun metagenomic sequencing
   - SGB (Species-level Genome Bin) taxonomic profiling
   - StrainPhlAn 4 phylogenetic reconstruction
   - Strain-sharing event identification (same strain in different samples)

3. **Transmission analysis:**
   - Strain-sharing rates (SSR) computed as shared strains / common species
   - Within-individual strain-sharing: 99% likelihood of ≥1 strain
   - Between-family strain-sharing at T01: ~46% likelihood
   - Tracked nursery group clustering vs. family clustering

4. **Key experiments:**
   - Mother-baby transmission validation (50% median SSR baseline)
   - A. muciniphila transmission chain tracing (baby→baby→mother→father)
   - Outbreaker strain identification (8 strains reaching ≥50% prevalence)
   - Antibiotic intervention analysis (7 amoxicillin, 13+clavulanic acid, etc.)

## Key Findings

| Metric | Value |
|--------|-------|
| Strain-sharing rate (SSR) at T01 | 2.5 strains per baby pair |
| SSR at T15 (end first term) | 7.2-8.8 strains per baby pair (new nursery-only) |
| SSR same group vs. different nursery at T15 | 20.2% vs 4.6% |
| SSR by end of school year (TA) | 33.3% median |
| Nursery-acquired strains at T15 | 28.4% (vs 20.0% family-acquired) |
| Baby strain replacement rate | 44.4% over 5 months |
| Antibiotic strain retention (babies) | 70.2% vs 90.6% control |

## Most Transmissible Species

**High nursery transmission:**
- *Bifidobacterium longum subsp. infantis* (88% SSR baby-baby) — specialized breast-fed baby colonizer
- *Bifidobacterium breve* — health-promoting infant species
- *Streptococcus gallolyticus*, *Bifidobacterium pseudocatenulatum* — outbreaker strains

**High family transmission:**
- *Bifidobacterium caccae*, *B. bifidum*, *B. pseudocatenulatum* (mother-baby)
- *Alistipes finegoldii*, *Bacteroides ovatus*, *Roseburia intestinalis* (sibling-baby)
- *Clostridium* spp., *Sutterella wadsworthensis* (father-baby)

## Implications

- Social peer interactions during the "first 1,000 days" are critical for microbiome development
- Nursery attendance may provide protective microbial colonization beyond family sources
- Antibiotic resistance is more severe in infants due to higher strain turnover
- Microbiome-based interventions targeting nursery settings could be powerful for early-life health

---

**Source:** Nature 2025; DOI: https://doi.org/10.1038/s41586-025-09983-z
