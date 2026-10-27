# Paper Summary

### Authors
Jianglin Zhang, Sarah O. Oladejo, Xianda Ma, Junjie Ma, Dingjiacheng Jia, Wenchao Yu, Samskrathi Sharma, Cassie L. Behrendt, Regis Stentz, Simon R. Carding, Qihao Wu, and Zheng Kuang.

### Journal
Cell Host & Microbe

### Publication Date
22 October 2026 (available online)

### DOI
10.1016/j.chom.2026.09.021

## Keywords

Gut microbiota; circadian rhythms; HDAC3; inositol phosphates; intestinal epithelial cells; nutrient absorption; malnutrition; growth stunting; obesity; epigenetic regulation.

## Main Idea

The study identifies a microbiota–feeding–epigenetic pathway in which *Bacteroides thetaiotaomicron* (Bt) converts feeding-associated signals into rhythmic intestinal metabolism. Bt’s inositol phosphatase Minpp produces inositol triphosphate (InsP3), which promotes HDAC3–NCoR complex formation in intestinal epithelial cells. HDAC3 then deacetylates PGC-1α and activates PGC-1α/ERRα-dependent nutrient-transporter genes. This improves nutrient uptake and juvenile growth during undernutrition but increases lipid uptake and diet-induced obesity during overnutrition.

## Evidence Supporting the Main Idea

- In germ-free mice, fecal microbiota conventionalization or Bt mono-colonization restored day–night oscillations of H3K9ac and epithelial gene expression; Bt-dependent oscillations were enriched for nutrient transport and metabolic pathways (Figure 1; 3 pooled biological replicates per sequencing library).
- Bt increased HDAC3 recruitment and H3K9ac cycling at metabolic loci including *Angptl4*, *Fkbp5*, and *Cpt1a*. These effects were dampened in mice with intestinal epithelial HDAC3 deletion (Figure 1).
- Bt increased feeding-phase serum amino acids, fatty-acid signals, triglycerides, and absorption of BODIPY-C16 and labeled amino acids (Figure 2).
- Bt enhanced expression of transporters such as *Slc36a1*, *Slc7a15*, *Slc15a1*, and *Cd36*. HDAC3, PGC-1α, and ERRα co-occupied relevant regulatory regions, and pharmacologic inhibition of PGC-1α reduced transporter expression (Figure 2; Figure S2).
- Wild-type Bt, but not a *minpp*-deletion strain, increased HDAC3–NCoR interaction and InsP3 levels. Complementation rescued the interaction phenotype, and exogenous InsP3 reproduced HDAC3–NCoR activation in cells and antibiotic-treated mice (Figure 3; Figure S3).
- InsP3 levels were higher at feeding-associated time points in conventional mice, absent or reduced in germ-free/antibiotic-treated mice, and restored by Bt but not Δ*minpp* Bt. Daytime-restricted feeding dampened the InsP3 and HDAC3–NCoR rhythms (Figure 3).
- Δ*minpp* Bt failed to restore normal genome-wide H3K9ac and RNA oscillations, and approximately 70% of BtMinpp-dependent cycling transcripts showed dampened oscillation after epithelial HDAC3 deletion (Figure 4; Figure S4).
- In low-nutrient diets, Bt or InsP3 improved body size, femur length, organ weights, serum amino acids, and glucose handling; these effects required epithelial HDAC3 and occurred without increased food intake (Figures 5–7; Figures S5–S7).
- In a 12-week Western-diet model, Bt or InsP3 increased weight gain, adipose/liver lipid accumulation, serum triglycerides, fasting glucose, insulin resistance, and intestinal lipid uptake. These phenotypes were absent after epithelial HDAC3 deletion (Figure S5–S6).

## Main Novelty

The work connects a bacterial inositol-phosphate pathway to feeding-time information, rhythmic HDAC3–NCoR activity, intestinal chromatin remodeling, and nutrient absorption. It also demonstrates that the same co-adapted pathway can be beneficial in undernutrition and harmful in overnutrition.

## Datasets Used for Evaluation

- **Mouse intestinal epithelial multi-omics:** H3K9ac ChIP-seq and RNA-seq from germ-free, conventionalized, conventional, Bt-mono-colonized, and Δ*minpp* Bt-colonized mice sampled across the light–dark cycle. Sequencing libraries generally used three pooled biological replicates; the role was to quantify diurnal chromatin and transcriptional rhythms. New data are deposited as GEO **GSE299733** (ChIP-seq) and **GSE299734** (RNA-seq).
- **Mouse physiology and absorption cohorts:** C57BL/6, *Hdac3*^fl/fl, and intestinal epithelial *Hdac3*^ΔIEC mice under chow/low-nutrient, antibiotic-depleted, Bt or mutant-colonized, InsP3-treated, and Western-diet conditions. Sample sizes varied by experiment; figure legends report n=3 for several molecular assays and n=8–12 for selected transporter-expression cohorts. These cohorts tested nutrient absorption, growth, glucose handling, lipid uptake, and obesity.
- **Cell culture experiments:** HT-29 intestinal epithelial cells and HEK293T cells treated with bacterial supernatants, Bt/Δ*minpp* products, purified InsP3, outer-membrane vesicles, or pathway inhibitors. Biological replicate numbers were typically n=3 for interaction assays; these experiments tested molecular sufficiency and mechanism.
- **Public human metagenomic dataset:** shotgun fecal metagenomic data comparing undernourished children with healthy controls, analyzed with MetaPhlAn/BioBakery and MaAsLin3. The paper does not specify the dataset accession or cohort sample size in the reported analysis; its role was to test whether Bt abundance is associated with nutritional status.
- **Published reference datasets:** prior HDAC3/ERRα ChIP-seq and intestinal NCoR-knockout RNA-seq datasets were reanalyzed to test regulatory co-occupancy and NCoR dependence of transporter genes.

## Experimental Procedure

- Compare germ-free, conventionalized, conventional, antibiotic-depleted, and Bt-mono-colonized mice across Zeitgeber time points.
- Isolate small-intestinal epithelial cells and measure H3K9ac ChIP-seq, RNA-seq, ChIP-qPCR, HDAC3–NCoR co-immunoprecipitation, transporter expression, and InsP3 abundance.
- Test feeding dependence using ad libitum, daytime-restricted, and nighttime-restricted feeding schedules.
- Compare wild-type Bt with Δ*minpp* Bt, complemented mutant Bt, and an analogous *E. coli* phosphatase mutant to establish the role of bacterial inositol-phosphate metabolism.
- Measure nutrient uptake using serum metabolomics, oral amino-acid challenges, ^13C-amino-acid tracing, BODIPY-C16/olive-oil gavage, serum triglycerides, and fecal lipid measurements.
- Test mechanism with epithelial *Hdac3* deletion, PGC-1α inhibition, InsP3 supplementation, bacterial outer-membrane vesicles, hemichannel inhibition, and the HDAC3 inhibitor RGFP966.
- Evaluate outcomes under low-nutrient diets and 12-week Western-diet feeding using body size, femur length, organ/adipose weights, glucose and insulin tolerance, serum metabolites, liver fat, and intestinal lipid accumulation.
- Analyze rhythmicity with JTK_Cycle/MetaCycle, differential expression with DESeq2, pathway enrichment/GSEA, and metagenomic differential abundance with MaAsLin3.

## Key Biology Insights

- Feeding timing is transduced into the intestinal epithelium partly through rhythmic bacterial InsP3 production rather than through changes in Bt abundance.
- InsP3 functions as a microbial signal that promotes HDAC3–NCoR complexing and PGC-1α deacetylation.
- HDAC3 links microbial signals to rhythmic chromatin accessibility/acetylation and nutrient-transporter transcription without eliminating core clock-gene rhythms.
- The pathway adjusts nutrient uptake to nutritional state: it supports linear growth during nutrient scarcity but amplifies lipid storage and metabolic dysfunction during nutrient excess.
- Bt association with healthy children in the analyzed metagenomic dataset is suggestive, not proof of human small-intestinal colonization or causality.

## Implications

Microbiota-directed interventions may need to account for feeding time and nutritional state: stimulating microbial InsP production or HDAC3 activity could help undernutrition but worsen obesity. The pathway offers candidate targets—Bt/Minpp, InsP3 transport, HDAC3–NCoR, and PGC-1α—but translation to humans requires confirmation of Bt function in the small intestine, validation in human cohorts, and assessment of long-term metabolic safety. The authors note that the study does not establish whether Bt colonizes or functions in the human small intestine.

