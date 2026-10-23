# Paper Summary

### Authors

Gwanggyu Sun*, Tim Hudelmaier*, Joshua C. Gilligan, Gabriel A. Gonzalez, Peter Yin, Fangping Wan, Zijian (Carl) Ma, Matthew G. Durrant, Chiara Ricci-Tam, April Pawluk, Andreas S. Puschnik, Silvana Konermann, and Patrick D. Hsu (corresponding author). (*Equal contribution.)

### Journal

bioRxiv preprint (not peer reviewed)

### Publication Date

October 22, 2026 (version 1)

### DOI

10.64898/2026.10.21.760802

## Keywords

Genomic language model; noncoding RNA; prokaryotes; Evo-PIN; COMPASS; RNA structure; CRISPR; bridge RNA; riboswitch; agentic discovery.

## Main Idea

The authors fine-tuned the genomic language model Evo 2 on prokaryotic intergenic DNA to create Evo-PIN, then used its sequence embeddings and token-level signals to organize the prokaryotic noncoding sequence space without alignment or reference selection. Their COMPASS pipeline clustered 376 million intergenic regions from 1.3 terabase pairs of genomes and metagenomes into 5.14 million clusters, providing an explorable map for discovering structured noncoding RNAs and their genomic partners.

## Evidence Supporting the Main Idea

- The input collection comprised 465 Gbp from 144,000 bacterial and archaeal species plus 855 Gbp of metagenomes. After deduplication, it contained 750 million intergenic sequences; 376 million were clustered after filtering (Results 2.1; Fig. 1B).
- On a benchmark of known ncRNAs, mean-pooled Evo 2 embeddings had a cluster-quality score of 0.43. Fine-tuning increased this to 0.60, and strand-specific low-entropy pooling increased it to 0.65 (Fig. 1C,H).
- Evo-PIN’s categorical Jacobians recovered known consensus base pairs more accurately than Evo 2 across five ncRNA families (Fig. 1D). Known ncRNA subsequences had median token entropies 73% lower than surrounding sequence for Evo-PIN, versus 55% for Evo 2 (Fig. 1E,F).
- The resulting clusters had median within-cluster pairwise identity of only 28.5%, below the usual 50–60% RNA alignment “twilight zone”; clusters containing known annotations had mean annotation consistency of 0.92 (Fig. 1J and Fig. S4B).
- Cluster-level structure and genomic-context analysis produced 20,149 clusters with strong covariation and a clear colocalized-gene signature. Known bridge RNA and omega RNA systems were recovered with their expected IS110 transposase and IsrB-like partners (Fig. 2B–D and Fig. S7A).
- Periodic token-entropy analysis identified 1,672 clusters covering 365,000 sequences. The dominant periods matched CRISPR arrays (60–79 nt), TIGR arrays (18 nt), and VIPR arrays (5 nt); the flanking protein folds matched Cas12f, FpTasA, and Vipr effectors, respectively (Fig. 3B–E).
- Targeted clustering of bridge-recombinase-adjacent sequences predicted programmable guide lengths for 32,190 bridge RNAs. Of these, 6,113 (19.0%) had predicted total programmable nucleotides above the experimentally characterized IS621 value of 28; a representative cluster-14 RNA was predicted to have 34 guide base pairs (Fig. 4C–I).
- Researcher-guided agents nominated a divergent fluoride-riboswitch candidate, a hammerhead-ribozyme candidate, and a PhoH2-associated structured RNA. These remain computational candidates and require experimental validation (Fig. 5F,J,M).

## Main Novelty

1. A top-down, alignment-free atlas of prokaryotic intergenic sequence space at hundreds-of-millions scale.
2. A single fine-tuned genomic language model supplies multiple discovery signals: pooled embeddings, low-entropy localization, periodicity, and Jacobian-derived structural contacts.
3. COMPASS combines cluster structure with gene-neighborhood enrichment and protein-fold searches to generate functional hypotheses without starting from known RNA families.
4. The study demonstrates researcher–agent workflows that train probes, search millions of clusters, integrate genomic and transcriptomic evidence, and rank candidates under an explicit rubric.

## Datasets Used for Evaluation

- **Prokaryotic genome collection:** 465 Gbp from 144,000 bacterial and archaeal species; used to parse intergenic regions and fine-tune Evo 2.
- **Prokaryotic metagenomes:** 855 Gbp; combined with genomes for the 1.3-terabase input collection.
- **Deduplicated intergenic regions:** 750 million sequences, 10–10,000 bp long, with median length 113 bp and median GC content 50.0%; used for fine-tuning and discovery, with 376 million entering COMPASS clustering.
- **Known ncRNA benchmark:** Intergenic sequences annotated by Rfam and other recently discovered ncRNA covariance models; used to score embedding quality and validate structure-related signals. Only 0.4% of sequences had a significant known-ncRNA hit.
- **Bridge-recombinase-adjacent sequences:** 32,190 predicted bridge RNAs represented by 86 cluster-specific covariance models; used to estimate target and donor guide lengths.
- **Pedobacter mucosus RNA-seq:** Nine public datasets; used to test transcriptional coverage over the PhoH2-associated candidate RNA.
- **Protein and structure resources:** Pfam, PDB, Swiss-Prot, Foldseek, and ESMFold-derived comparisons; used to identify enriched neighboring proteins and structural analogs.

## Experimental Procedure

- Parse 10–10,000 bp regions between annotated protein-coding genes, tRNAs, and rRNAs from prokaryotic genomes and metagenomes; remove redundancy and annotate known ncRNAs with covariance models.
- Fine-tune the 7B-parameter Evo 2 model by continued pretraining on intergenic sequences, producing Evo-PIN.
- Extract forward- and reverse-strand token entropies and embeddings; pool embeddings only at strand-specific low-entropy positions.
- Build an approximate k-nearest-neighbor graph and apply Leiden clustering to obtain COMPASS clusters; evaluate cluster quality against known ncRNA annotations.
- Reorient cluster members, infer shared motifs with CMfinder, test base-pair covariation, and extend each locus by 5 kb on both sides to annotate neighboring genes and protein folds.
- Autocorrelate token-entropy tracks within clusters to detect tandem-repeat periodicity; classify CRISPR-, TIGR-, VIPR-like, and previously uncharacterized arrays using repeat architecture and genomic context.
- Recluster sequences adjacent to bridge recombinases, construct covariance models, reconstruct target and donor sites, and infer RNA–DNA guide lengths from covariation and local alignments.
- Deploy researcher-guided AI agents to train embedding probes, rank divergent riboswitch and ribozyme candidates, and investigate thousands of nuclease/helicase-associated hypotheses using RNA structure, genomic context, protein identity, conservation, and transcriptomic evidence.

## Key Biology Insights

- Prokaryotic intergenic sequence space is much less annotated than its scale suggests: fewer than 1% of COMPASS clusters contained known ncRNA annotations, and only 1.5% of motif-bearing clusters overlapped known ncRNAs in at least two sequences.
- Evo-PIN representations capture evolutionary constraints associated with RNA structure, not just short sequence similarity, enabling clustering at a median within-cluster identity of 28.5%.
- Periodic entropy is a general signature of tandem repeat architecture and can recover RNA-guided systems even when the initial clustering uses only intergenic sequence embeddings.
- The bridge-RNA search nominates orthologs with longer programmable recognition regions than the characterized IS621 system, potentially useful for future genome-engineering development.
- The study proposes divergent fluoride riboswitch and hammerhead-ribozyme families that evade their existing Rfam models, as well as lineage-associated structured RNAs near PhoH2 helicase/nuclease proteins.

## Implications

COMPASS provides a public database and web/MCP interface for exploring prokaryotic noncoding sequence diversity and prioritizing experiments. Its strongest value is as a candidate-generation and evidence-integration system: predicted structures, gene associations, taxonomy, and transcriptional evidence can guide experimental testing. The authors emphasize that computational candidates are not validated molecular functions. Interpretation is also biased toward detectable covariation, recognizable periodicity, and conserved gene neighborhoods. Extending the approach to viruses and eukaryotes will require adaptations for overlapping elements, much longer intergenic regions, lower sequence diversity, and weaker gene-neighborhood signals.

Source: https://www.biorxiv.org/content/10.64898/2026.10.21.760802v1
