# Paper Summary

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
- In an Mtb-infected mouse model sampled at 1 day, 4 weeks, and 8 weeks post-infection, Stereo-seq V2 simultaneously detected host and bacterial RNA, with bacterial signal peaking at 4 weeks and decreasing by 8 weeks in agreement with colony-forming-unit measurements.
- The method recovered 270 BCR V genes in infected mouse lung tissue and assembled 185 BCR clones at 4 weeks and 1,736 at 8 weeks post-infection, indicating improved immune-repertoire read coverage from the 5' biased random-primer design.
- In human tuberculous lung FFPE sections, Stereo-seq V2 captured human and Mtb transcriptomes together and identified recurrent BCR clones, including 16 shared clones across three patients, with related clones also enriched in external tuberculosis bulk RNA-seq data.

## Main Novelty
- The main novelty is an FFPE-compatible, high-resolution spatial transcriptomics chemistry that measures total RNA rather than mainly polyadenylated transcripts.
- The work goes beyond a chemistry upgrade by showing three capabilities in one study: robust degraded-FFPE profiling, simultaneous host-pathogen spatial transcriptomics, and in situ spatial immune-repertoire reconstruction.
- The unbiased 5' coverage is particularly novel because it enables BCR clone assembly and spatial analysis that are difficult with conventional poly(A)-capture spatial transcriptomics platforms.

## Datasets Used for Evaluation
- Adjacent fresh-frozen mouse brain sections assayed with Stereo-seq V1 and V2 for direct platform comparison.
- Public MERFISH mouse brain data with 1,122 targeted genes for cross-platform validation.
- FFPE mouse brain sections used to assess total RNA and ncRNA capture.
- Clinical FFPE cohort:
- 10 triple-negative breast cancer FFPE tissue blocks with storage times from about 1 to 9 years and DV200 values from 18 to 76.
- Infection model cohort:
- Mouse lung FFPE sections collected at 1 day, 4 weeks, and 8 weeks after Mtb infection.
- Human disease cohort:
- Surgically resected lung tissues from three tuberculosis patients.
- External validation datasets:
- Public Mtb infection bulk RNA-seq data containing 82 Mtb-associated BCR clones and TB patient versus healthy-donor bulk RNA-seq / PBMC repertoire data used for clone comparison.

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
- The data support the idea that pathogen-specific humoral immune responses can be studied directly in tissue space rather than only through bulk immune-repertoire assays.

## Implications
- Stereo-seq V2 makes large FFPE archives more usable for spatial biology, translational oncology, and infectious disease studies.
- The method broadens spatial transcriptomics beyond polyadenylated host RNA to include ncRNAs, pathogen RNAs, and immune-receptor features in one assay.
- If the platform scales operationally, it could become useful for retrospective biomarker studies on clinically annotated FFPE cohorts where fresh tissue is unavailable.
