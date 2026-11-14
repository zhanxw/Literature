# Paper Summary

### Authors
Rayan Najjar, Xiaoxing Wang, Farheen Shaikh, Ning Wang, Ethan Le, Jie An, Mohammad Pourshamsi, Cecilia Mustelin, Fatemeh Moadab, Spencer Mirabile-Brightman, Leslie Montero, Karla S. Zavala, Vincent Gureghian, Gabriela Cervantes, Sadie J. Van den Bogaerde, Samir Adhikari, Mikhail V. Pogorelyy, Paul G. Thomas, Stephen P. Schoenberger, and Tomas Mustelin.

### Journal
Nature.

### Publication Date
28 October 2026 (published online).

### DOI
[10.1038/s41586-026-11219-7](https://doi.org/10.1038/s41586-026-11219-7)

## Keywords
Systemic lupus erythematosus; neutrophils; alternative mRNA splicing; cryptic splicing; neoantigens; immunopeptidomics; T-cell receptors; autoantibodies; type I interferon.

## Main Idea
Neutrophils from patients with systemic lupus erythematosus (SLE) produce disease-restricted, aberrantly spliced transcripts. Translation of these transcripts generates novel amino-acid sequences that are absent from canonical human proteins and can function as autoantigens. The authors provide evidence that these splicing-derived neoantigens are presented on HLA molecules and recognized by both T cells and class-switched IgG autoantibodies.

## Evidence Supporting the Main Idea
- RNA-seq of neutrophils identified 271 SLE-restricted cryptic splicing events in 130 protein-coding genes; the events were absent from the healthy-control and rheumatoid-arthritis neutrophil groups. Events were detected in 33 of 34 SLE patients.
- RiboSplitter translated the cryptic transcripts into candidate peptides. HLA-binding prediction yielded 86 high-affinity candidate peptides from 46 genes, with 65 in the top 0.5th percentile for the patients' HLA alleles.
- Targeted LC-MS/MS of HLA immunoprecipitates detected 21 predicted novel peptides, including products of USP18, IFI44L, OGG1, OAS1, RSAD2, FCGRT, MX1, and other genes (Fig. 3; Table 1). RT-PCR and Sanger sequencing independently validated representative cryptic splice forms in USP18, ABCG1, IFI44L, OAS1, and MX1 (Fig. 2).
- In a 14-day peptide-expansion/restimulation assay, T cells from 9 of 10 tested SLE patients showed moderate-to-strong responses to at least some neoantigen peptides. Responses included IFN-γ and IL-17 secretion and CD69 activation in both CD4+ and CD8+ T cells, whereas healthy-donor T cells showed little response.
- TCR sequencing found strong clonal expansion after stimulation with two IFI44L neoantigens. Re-expression of one paired TCR in T-FINDER reporter cells transferred selective reactivity to the IFI44L-2 peptide.
- ELISAs found IgG against several neo-sequences; 17 of 34 SLE patients recognized the first IFI44L peptide above the healthy-donor 95th-percentile cutoff. Reactivity was also observed for OAS1, MX1, IFI44, and RSAD2 neo-sequences.
- Poly-perforin pores were detected on 0–20% of SLE neutrophils but not healthy-donor neutrophils, consistent with prior cytotoxic-T-cell contact with antigen-bearing neutrophils (Fig. 5).

## Main Novelty
The study connects an SLE-specific RNA-processing defect to a complete autoimmune-antigen pathway: cryptic splicing, translation into novel sequences, HLA presentation, antigen-specific T-cell clonal expansion, and class-switched IgG recognition. It extends the neoantigen concept from cancer to autoimmunity without requiring genomic mutation.

## Datasets Used for Evaluation
- **Primary neutrophil RNA-seq cohort:** 34 SLE patients, 20 healthy controls, and 15 rheumatoid-arthritis patients; used to identify and compare cryptic splicing events.
- **SLE monocyte RNA-seq:** patient-derived monocyte data; used to test whether the events were neutrophil-specific.
- **Interferon-treated healthy neutrophils and Sjögren’s-disease neutrophils:** comparator transcriptomes; used to distinguish SLE-specific splicing from generic interferon exposure or another autoimmune disease.
- **SLE PBMC RNA-seq:** two public datasets, 36 patients in total; used for cross-cell-type and cross-dataset comparison.
- **AML14 myeloid cell-line transcriptome:** used as an additional immature-myeloid comparison.
- **Primary samples for immunopeptidomics, ELISA, and T-cell assays:** selected SLE patient neutrophils, sera, and PBMCs from the clinical cohort; the paper reports assay-specific sample counts, including 10 SLE patients in the principal T-cell response experiment and 34 SLE sera for the IFI44L IgG analysis.
- **External regulatory datasets:** ENCODE RNA-binding-protein/eCLIP and perturbation data; used to nominate splice-factor mechanisms, not as a primary outcome dataset.

## Experimental Procedure
- Isolate neutrophils and other immune cells from SLE, healthy-control, and rheumatoid-arthritis blood samples.
- Perform stranded paired-end neutrophil RNA-seq at approximately 50 million 101-base reads per sample.
- Use the RiboSplitter pipeline to detect disease-restricted splice junctions, translate them, remove canonical/annotated products, and predict HLA-I/HLA-II binding with patient-specific HLA types.
- Validate representative splice forms by diagnostic RT-PCR and Sanger sequencing.
- Immunoprecipitate class-I HLA from SLE neutrophils and identify candidate presented peptides by targeted LC-MS/MS against a custom cryptic-peptide database.
- Measure serum IgG binding to tiled 15-mer peptides from the novel sequences by ELISA.
- Expand patient PBMC T cells for 14 days with peptide pools, restimulate with individual peptides, and measure IFN-γ/IL-17 ELISpot and CD69 by flow cytometry.
- Sequence expanded TCRs, pair TCR alpha/beta chains with TIRTL-seq, and test antigen specificity after expression in T-FINDER reporter cells.
- Stain neutrophils for poly-perforin pores as evidence of cytotoxic-T-cell engagement.

## Key Biology Insights
- SLE neutrophils contain a broad but patient-variable repertoire of cryptic splice events, dominated by exon skipping, altered splice sites, and intron retention.
- The affected transcript set is enriched for type-I-interferon-inducible genes, but expression level alone does not explain all events; non-interferon genes are also affected.
- Cryptic splicing is largely cell-type and disease-context specific: only a small number of events overlapped with SLE monocytes, SLE PBMC datasets, interferon-treated healthy neutrophils, or Sjögren’s-disease neutrophils.
- Novel peptides can arise through frameshifts, translation beyond canonical stop sites, and inclusion of intronic transposable-element sequence such as Alu or LINE-derived sequence.
- The observed T-cell responses are polyclonal and patient-specific, with estimated neoantigen-reactive T-cell frequencies of approximately 1–15 per million T cells.
- The findings support a model in which aberrant RNA processing creates “foreign” self-antigens that can drive cytotoxicity, T-cell help to B cells, IgG class switching, and ongoing autoimmune inflammation.

## Implications
The work suggests that abnormal RNA splicing is a potential upstream source of antigenic diversity in SLE and may help explain neutrophil consumption, inflammatory cell death, disease fluctuations, and the breadth of autoimmunity. Cryptic peptides, their HLA presentation, or the responsible splicing machinery could become biomarkers or therapeutic targets. The study is associative for the initiating cause: RNA-seq was collected at one time point, estimated splice-event coverage was about 60%, and the experiments do not establish that every detected neoantigen is pathogenic in vivo or identify a single universal splice-factor defect.
