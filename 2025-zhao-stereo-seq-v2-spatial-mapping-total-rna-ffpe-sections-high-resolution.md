# Paper Summary

**Title:** Stereo-seq V2: Spatial mapping of total RNA in FFPE sections at high resolution

**Source:** [Published article](https://doi.org/10.1016/j.cell.2025.08.008); full-text PDF reviewed from the [repository archive](archived/2025-zhao-stereo-seq-v2-spatial-mapping-total-rna-ffpe-sections-high-resolution.pdf).

### Authors
Yu Zhao, Young Li, Ying He, et al.

### Journal
Cell

### Publication Date
2025-11-13

### DOI
10.1016/j.cell.2025.08.008

## Keywords
- Spatial transcriptomics
- FFPE
- Stereo-seq V2
- Total RNA
- Random priming
- Mycobacterium tuberculosis
- B cell receptor repertoire
- Triple-negative breast cancer

## Main Idea
- The paper introduces Stereo-seq V2, a spatial transcriptomics method for formalin-fixed paraffin-embedded (FFPE) tissue that replaces poly(T) capture with random-primer-based total RNA capture.
- The authors argue that this design preserves the large field of view and near-single-cell spatial resolution of Stereo-seq while improving compatibility with degraded FFPE RNA, non-coding RNA detection, and 5' coverage.
- They show that the method can profile clinical FFPE tumors, jointly measure host and pathogen transcripts in tuberculosis samples, and recover spatial B cell receptor (BCR) repertoire information in situ.

## Evidence Supporting the Main Idea
- The platform uses random primers plus FFPE-compatible deparaffinization, rehydration, and decrosslinking steps, while retaining 500 nm DNA nanoball spacing for theoretical subcellular resolution.
- On adjacent fresh-frozen mouse brain sections, Stereo-seq V1 and V2 showed strong expression concordance, and Stereo-seq V2 detected 1,099 of 1,122 MERFISH probe targets, supporting robust gene detection rather than increased nonspecific noise.
- In FFPE mouse brain, the method captured both coding and non-coding RNAs, including region-restricted ncRNAs such as `D130079A08Rik` and `4921539H07Rik`, which the paper uses to support total RNA spatial profiling.
- In 10 triple-negative breast cancer FFPE blocks stored for roughly 1 to 9 years, Stereo-seq V2 maintained consistent gene capture across DV200 values from 18 to 76, and sample `T202301978` still showed strong capture despite DV200 = 18 when cDNA yield was high.
- In the same TNBC cohort, the authors identified histology-aligned spatial marker patterns, inferCNV-defined tumor subtypes, and 1,414 differential alternative splicing events between tumor regions, including a BEX4 exon-skipping event.
- In an Mtb-infected mouse model sampled at 1 day, 4 weeks, and 8 weeks post-infection, Stereo-seq V2 simultaneously detected host and bacterial RNA, with bacterial RNA signal peaking at 4 weeks and decreasing by 8 weeks (Figure 6). The plotted 4-versus-8-week CFU comparison has p = 0.078; the direction agrees, but this comparison does not establish a statistically significant decline in viable burden. RNA signal is not a direct viability assay.
- The method recovered 270 BCR V genes in infected mouse lung tissue and assembled 185 BCR clones at 4 weeks and 1,736 at 8 weeks post-infection, demonstrating immune-repertoire recovery from the random-primer design (Figure 7). Differences in clone counts can also reflect sampling depth and tissue composition.
- In human tuberculous lung FFPE sections, Stereo-seq V2 captured human and Mtb transcriptomes together and identified recurrent BCR clones, including 16 shared clones across three patients, with related clones also enriched in external tuberculosis bulk RNA-seq data (Figure 7). Sequence similarity and enrichment suggest an association with TB; antigen specificity was not directly demonstrated by binding assays.

## Main Novelty
- The main novelty is an FFPE-compatible, high-resolution spatial transcriptomics chemistry that measures total RNA rather than mainly polyadenylated transcripts.
- The work goes beyond a chemistry upgrade by showing three capabilities in one study: robust degraded-FFPE profiling, simultaneous host-pathogen spatial transcriptomics, and in situ spatial immune-repertoire reconstruction.
- The unbiased 5' coverage is particularly novel because it enables BCR clone assembly and spatial analysis that are difficult with conventional poly(A)-capture spatial transcriptomics platforms.

## Datasets Used for Evaluation

| Dataset | Contents and sample size | Role and access |
|---|---|---|
| Fresh mouse brain, Stereo-seq V1/V2 | Adjacent sections; biological animal count: Not specified in paper | Platform comparison; [CRA018257](https://ngdc.cncb.ac.cn/gsa/browse/CRA018257) |
| FFPE mouse brain | Coding and noncoding spatial RNA; animal count: Not specified in paper | Total-RNA and FFPE benchmarking; [CRA016462](https://ngdc.cncb.ac.cn/gsa/browse/CRA016462) |
| TNBC FFPE cohort | 10 patients; blocks stored 1–9 years, DV200 18–76 | Clinical performance, spatial tumor states and alternative splicing; [HRA007387](https://ngdc.cncb.ac.cn/gsa-human/browse/HRA007387) |
| Mouse TB lung | Normal, 1-day, 4-week and 8-week conditions; Figure 6D shows two sections per condition. Independent animal count: Not specified in paper | Host–pathogen and temporal repertoire analysis; [CRA018250](https://ngdc.cncb.ac.cn/gsa/browse/CRA018250) |
| Human TB lung FFPE | Three patients | Host–pathogen and shared-clonotype demonstration; [HRA011927](https://ngdc.cncb.ac.cn/gsa-human/browse/HRA011927) |
| MERFISH mouse brain | 1,122 targeted genes; 1,099 recovered by V2; specimen count: Not specified in paper | Cross-platform benchmark; Zhuang laboratory ABCA-2 resource in the key resources table |
| Other brain reference data | Visium FFPE coronal sections 1 and 2; Stereo-seq V1 brain; Allen Brain Atlas in-situ hybridization; bulk brain RNA-seq. Biological sample counts: Not specified in paper | Spatial patterns and expression benchmarking; V1 resource [BSDC.1699433096.20001](https://doi.org/10.12412/BSDC.1699433096.20001), [Allen Mouse Brain Atlas](https://mouse.brain-map.org/), bulk [GSE206562](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE206562) |
| Additional spatial comparators | COAD Stereo-seq CNP0002432; lung cancer Stereo-seq CNP0002199; DCIS Visium GSE181254; STRS GSE200481. Sample counts: Not specified in paper | Published spatial-assay comparisons listed in the key resources table |
| Infected-mouse bulk RNA-seq | Reanalysis recovered 82 clones, 25 matching the spatial data; biological sample count: Not specified in paper | External repertoire comparison; [source study](https://doi.org/10.1128/spectrum.03431-22) |
| Human PBMC bulk RNA-seq | Active TB and healthy comparators; sample count: Not specified in paper | External clone enrichment. **Accession discrepancy:** key resources list GSE107991, whereas Figures 7 and S7 cite GSE107995; reconcile against the original data before downloading |

Counts of sections, cells, genes, and clonotypes are not interchangeable with independent biological sample sizes. Controlled-access human deposits may require a data-access application.

## Experimental Procedure
- Modify Stereo-seq chemistry for FFPE by adding deparaffinization, rehydration, decrosslinking, and random-primer-based total RNA capture.
- Benchmark Stereo-seq V2 against Stereo-seq V1 and MERFISH on mouse brain to assess expression concordance, diffusion behavior, and target recovery.
- Apply the method to FFPE mouse brain to test coding and non-coding RNA spatial detection.
- Profile 10 clinical TNBC FFPE samples and analyze spatial marker expression, inferCNV patterns, and alternative splicing events.
- Apply Stereo-seq V2, H&E staining, and acid-fast staining to adjacent sections from Mtb-infected mouse lungs across three time points.
- Quantify host-pathogen spatial transcriptomes, immune modules, and BCR heavy-chain expression dynamics across infection stages.
- Assemble BCR repertoires with MIXCR, map clonotypes back to spatial coordinates, and compare them with public bulk RNA-seq repertoires.
- Validate the infection-related BCR findings on surgically resected human tuberculous lung FFPE sections.

## Key Biology Insights
- FFPE tissues retain enough biological signal for high-resolution total RNA spatial profiling when the capture chemistry is adapted to fragmented RNA.
- Clinical FFPE tumors contain spatially organized transcriptional, copy-number, and splicing heterogeneity that can be resolved from archived material.
- During tuberculosis infection, adaptive immune signatures and BCR-related programs increase as infection progresses, with spatial organization around infected or necrotic regions.
- The data support spatial study of TB-associated humoral responses. Demonstrating that a recovered clonotype binds a particular mycobacterial antigen requires additional functional validation.

## Implications
- Stereo-seq V2 makes large FFPE archives more usable for spatial biology, translational oncology, and infectious disease studies.
- The method broadens spatial transcriptomics beyond polyadenylated host RNA to include ncRNAs, pathogen RNAs, and immune-receptor features in one assay.
- If the platform scales operationally, it could become useful for retrospective biomarker studies on clinically annotated FFPE cohorts where fresh tissue is unavailable.

The 500-nm DNA-nanoball pitch is a capture-array property, not a guarantee that every analysis resolves individual cells. Binning, tissue processing, RNA diffusion, and signal sparsity determine effective biological resolution. For downstream host–microbe analysis, retain the reported analysis binning and assess mixed-cell contributions.

The study is primarily a technology demonstration, with only three human TB donors. It does not establish that local BCR enrichment protects against TB, that microbial RNA implies viable organisms, or that tissue proximity proves a causal host–pathogen interaction. Independent donor-level replication, negative controls for microbial assignments, and functional testing of selected antibodies are appropriate next steps.
