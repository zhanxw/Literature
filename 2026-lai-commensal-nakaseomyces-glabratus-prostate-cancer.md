# Paper Summary

### Authors

Ping Lai, Lei Liu, Nicolò Pernigoni, Yingxi Du, Daniele Braga, Martina Troiani, Giuseppe Attanasio, Yuxin Li, Pan Song, Emiliano Pasquini, Tanja Rezzonico Jost, Xiaowen Huang, Martino Maddalena, Simone Mosole, Andrea Rinaldi, Giovanna Pecoraro, Martino Pedrani, Aurora Valdata, Nicolò Bancaro, Luisa Maraccani, Alessandra De Giani, Wei Yuan, Lewis Gallagher, Khobe Chandran, Penny Flohr, Pasquale Rescigno, Giuseppe Reitano, Alessandro Morlacco, Fabrizio Dal Moro, Isabella Giacomini, Monica Montopoli, Matteo Brunelli, Serena Pedron, Ricardo Pereira Mestre, Raad Z. Gharaibeh, Christian Jobin, Silke Gillessen Sommer, Johann de Bono, and Andrea Alimonti. Ping Lai and Lei Liu contributed equally.

### Journal

Nature Cancer

### Publication Date

9 September 2026

### DOI

[10.1038/s43018-026-01229-9](https://doi.org/10.1038/s43018-026-01229-9)

## Keywords

Prostate cancer; castration-resistant prostate cancer; androgen-deprivation therapy; gut mycobiota; *Nakaseomyces glabratus*; myeloid-derived suppressor cells; Dectin-2; Activin A; intestinal barrier; tumor microbiome.

## Main Idea

The study proposes a gut-to-tumor mechanism linking androgen deprivation to prostate-cancer progression. In patients with castration-resistant prostate cancer (CRPC), *N. glabratus* was detected in fecal, blood and tumor samples and was associated with poorer overall survival. In castrated mouse models, live oral *N. glabratus* crossed an androgen-sensitive intestinal barrier, localized to prostate tumors, activated Dectin-2–SYK signaling in polymorphonuclear myeloid-derived suppressor cells (PMN-MDSCs), and increased their production of Activin A. Activin A stimulated androgen-receptor-associated tumor programs and accelerated castration-resistant growth. An orally delivered negatively charged intestinal hydrogel reduced fungal translocation, PMN-MDSC accumulation and tumor growth.

## Evidence Supporting the Main Idea

- **Human association:** ITS sequencing found *N. glabratus* in 23.8% of fecal samples from patients with CRPC (21 total) and in none of the hormone-sensitive prostate-cancer samples (10 total). In a separate CRPC metagenomic cohort of 91 patients, its presence was associated with worse overall survival (univariate HR 2.6, 95% CI 1.0–6.5, *P* = 0.042; Kaplan–Meier *P* = 0.035). The association remained after adjustment for age, prior therapies, neutrophil-to-leukocyte ratio, PSA and Gleason score.
- **Clinical detection beyond stool:** PCR detected *N. glabratus* DNA in blood from more prostate-cancer patients than healthy controls and in 2 of 14 fresh-frozen CRPC tumor biopsies. Three primer sets and Sanger sequencing were used to reduce the likelihood of contamination. The authors note that the tumor sample size is too small to establish a survival association.
- **Castration-dependent tumor promotion:** Oral *N. glabratus* accelerated tumor growth and worsened survival in castrated TRAMP-C1 allografts, but not sham-operated mice. It also increased tumor aggressiveness and Ki67 staining in castrated *Pten* conditional-null mice. The effect persisted without antibiotic pretreatment and was not reproduced by oral *Candida albicans*.
- **PMN-MDSC dependence:** *N. glabratus* increased intratumoral CD11b+Ly6G+Ly6C^int PMN-MDSCs and their suppression of T-cell proliferation in mouse and human MDSC assays. Anti-Ly6G depletion reversed the fungal growth-promoting effect.
- **Receptor and pathway evidence:** Dectin-2 loss or knockdown (encoded by *Clec4n*) blocked *N. glabratus*-induced SYK, p38 and ERK activation, reduced *Nos2* and *Arg1* expression, weakened MDSC-mediated T-cell suppression and prevented the tumor-promoting phenotype in bone-marrow-reconstituted mice. Dectin-1 loss did not produce these effects.
- **Activin A mechanism:** RNA-seq, RT–qPCR and ELISA identified *Inhba*/Activin A as a major *N. glabratus*-induced PMN-MDSC product. MDSC-conditioned medium or recombinant Activin A increased growth and androgen-receptor-related gene expression in mouse TRAMP-C1 cells and an AR-positive human organoid; an Activin receptor inhibitor blocked these effects. MDSC-specific reduction of Activin A or pharmacological inhibition reduced tumor growth.
- **Translocation and intervention:** GFP-labelled *N. glabratus* was detected in tumors only after castration and was closer to Ly6G+ than CD3+ cells (19.03 ± 15.33 versus 44.73 ± 23.02 μm). Fluconazole or heat-inactivated fungus eliminated the tumor-promoting effect. An intestinal hydrogel reduced tumor fungal DNA, PMN-MDSCs and tumor growth, but did not block growth when fungus was injected directly into tumors.
- **Barrier mechanism:** Castration increased plasma FITC–dextran and reduced ileal Claudin-1, occludin and MUC2. Dihydrotestosterone partly restored barrier markers and reduced permeability, supporting androgen-dependent intestinal barrier maintenance.

## Main Novelty

This work identifies a specific fungal species and a mechanistic gut-to-tumor route by which androgen deprivation can reshape the prostate-tumor immune microenvironment. It connects intestinal barrier failure, *N. glabratus* translocation, Dectin-2-dependent PMN-MDSC activation and Activin A-mediated endocrine resistance, and provides a barrier-restoring intervention in mouse models.

## Datasets Used for Evaluation

- **Human ITS cohort:** Fecal samples from 10 patients with hormone-sensitive prostate cancer and 21 with CRPC; used to compare fungal prevalence.
- **Human CRPC metagenomic cohort:** 91 fecal/rectal-swab samples; used for fungal profiling and survival analysis.
- **Human blood cohort:** Healthy donors (n = 31) and patients with prostate cancer (n = 102); used for qPCR detection of fungal, *Candida*, *C. albicans* and *N. glabratus* DNA.
- **Human tumor samples:** 14 fresh-frozen CRPC biopsies; used for species-specific PCR and Sanger validation.
- **Mouse prostate-cancer models:** TRAMP-C1 allografts and *Pten*^pc−/− mice, with sham operation or castration and, where specified, antibiotic depletion; used to test tumor growth, survival, immune infiltration and fungal translocation.
- **Mouse microbiome data:** Fecal 16S sequencing from treated TRAMP-C1 mice; used to assess whether the fungal effect was explained by major bacterial-community changes.
- **Cell and organoid systems:** Mouse BM-MDSCs, human MDSCs, TRAMP-C1 and LNCaP cells, and patient-derived organoids MSKPCa8 (AR-positive) and MSKPCa13 (AR-negative); used for receptor, suppression, Activin A and tumor-cell response experiments.
- **Transcriptomic datasets:** New BM-MDSC RNA-seq (GEO GSE311900), previously published prostate-tumor scRNA-seq (GSE272965), the Prostate Cancer Atlas, ICR-RMH, SU2C and Taylor cohorts; used for pathway analysis, receptor expression, *INHBA* expression and clinical outcome associations.

## Experimental Procedure

- Profile human fecal mycobiota by ITS sequencing and shotgun metagenomics, then test clinical associations with survival.
- Detect fungal DNA in human blood and tumor tissue by multi-primer qPCR/PCR, gel electrophoresis and Sanger sequencing.
- Administer live, labelled or heat-inactivated *N. glabratus* to sham-operated or castrated TRAMP-C1 and *Pten*^pc−/− mice; monitor tumor size, histology, Ki67, survival and fungal localization.
- Profile tumor and peripheral immune cells by flow cytometry, deplete PMN-MDSCs with anti-Ly6G, and measure T-cell suppression ex vivo and in vitro.
- Perturb Dectin-1/Dectin-2/Mincle using siRNA, knockout cells and bone-marrow chimeras; measure downstream signaling and immunosuppressive genes.
- Use BM-MDSC RNA-seq, RT–qPCR, ELISA and conditioned-medium experiments to identify Activin A, then test Activin receptor inhibition, recombinant Activin A and MDSC-specific *Inhba* deletion.
- Measure intestinal permeability with FITC–dextran, assess tight-junction proteins by RT–qPCR, immunofluorescence and western blotting, and restore androgen signaling with dihydrotestosterone.
- Test fluconazole and an orally delivered inflammation-targeting hydrogel as interventions against fungal translocation and tumor progression.

## Key Biology Insights

- Androgen signaling contributes to intestinal barrier homeostasis; androgen deprivation can therefore alter tumor biology indirectly through the gut.
- *N. glabratus* is not merely correlated with disease in this model: live fungus must reach the tumor and engage myeloid cells to reproduce the phenotype.
- Dectin-2, rather than Dectin-1, is the dominant fungal-recognition receptor implicated in PMN-MDSC activation, consistent with recognition of mannan-rich fungal cell-wall components.
- PMN-MDSC-derived Activin A provides a link between fungal sensing and reactivation of androgen-receptor-associated transcription in androgen-deprived tumor cells.
- The fungal effect is species- and viability-dependent: *C. albicans* and heat-inactivated *N. glabratus* did not reproduce the same tumor phenotype.
- The authors report important limitations: patient tumor detection was based on a small sample set, animal experiments were not blinded, sample sizes were not prospectively determined, and Lyz2-Cre is not strictly PMN-MDSC-specific.

## Implications

The findings support investigating gut-barrier integrity, fungal burden and Dectin-2–PMN-MDSC–Activin A signaling as components of prostate-cancer endocrine resistance. The intestinal hydrogel and combinations with MDSC inhibitors are plausible preclinical strategies, but the paper does not establish clinical efficacy or safety. Larger patient cohorts and additional mouse models are needed before translating the intervention to patients.

Source: [Nature Cancer article](https://www.nature.com/articles/s43018-026-01229-9). Open-access article under CC BY 4.0.
