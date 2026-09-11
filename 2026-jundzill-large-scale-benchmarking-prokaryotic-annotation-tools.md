# Paper Summary

### Authors

Mateusz Jundzill, Martin Hölzer, Serghei Mangul, Mike Marquet, Ralf Ehricht, Mara Lohde, Riccardo Spott, Oliwia Makarewicz, Mathias W. Pletz, and Christian Brandt.

### Journal

*Genome Biology* 27, article 284 (2026).

### Publication Date

4 September 2026 (version of record: 7 September 2026).

### DOI

[10.1186/s13059-026-04262-0](https://doi.org/10.1186/s13059-026-04262-0)

## Keywords

Bioinformatics; genome annotation; bacteria; archaea; benchmarking; computational biology; metagenome-assembled genomes; functional annotation; gene function prediction; Gene Ontology.

## Main Idea

The study benchmarks four widely used open-source prokaryotic annotation tools—Prokka, Bakta, EggNOG-mapper, and PGAP—across 156,033 genomes and multiple genome-quality contexts. It finds that tool selection should depend on taxonomy, assembly quality, and the desired annotation objective rather than on a single universal ranking.

## Evidence Supporting the Main Idea

- In 24,393 *Escherichia coli* genomes, Bakta produced the largest mean described coding density (4,485,330 bp), while PGAP produced the largest mean total coding space (4,709,183 bp) and the highest mean RefSeq accession proportion (92.50%) (Fig. 2; Additional file 1: Tables S1–S7).
- Across 26,970 bacterial representatives, Bakta ranked best for described coding density in 23,121 species; PGAP ranked best for total coding density in 9,870 species, closely followed by Bakta in 9,852 species (Fig. 3b).
- Across 2,791 archaeal genomes, PGAP ranked best for total coding density in 1,858 genomes and described coding density in 2,549 genomes. Bakta does not officially support archaeal annotation, so its archaeal results require caution.
- PGAP had the highest GO coverage in bacteria (mean 31.20%) and archaea (20.03%), whereas EggNOG-mapper had the highest GO richness (35.40 and 38.69 terms per gene, respectively) (Fig. 3d; Additional file 1: Fig. S7).
- In 3,137 bacterial MAGs, PGAP achieved the largest described and lowest undescribed coding density on average and retained higher GO coverage (31.54%) than EggNOG-mapper (6.95%) or Bakta (0.18%) (Fig. 4a–b; Additional file 2: Table S6).
- In 98,742 simulated frameshifted genomes, PGAP showed a smaller loss of coding density and more stable feature counts as nucleotide deletion increased from 0.5% to 2% (Fig. 4c–e; Additional file 2: Table S7).

## Main Novelty

This is a large, systematic comparison that combines taxonomic breadth with realistic annotation challenges—MAGs, fragmented assemblies, simulated frameshifts, and database-update effects—while evaluating structural features, coding density, database-linked descriptions, RNA genes, and GO annotations together.

## Datasets Used for Evaluation

- **GTDB release 207.0 / NCBI assemblies:** 29,761 downloaded bacterial and archaeal genomes used for broad benchmarking: 26,970 bacterial and 2,791 archaeal representatives in the main taxonomic analysis. Bacterial assemblies averaged 95.45% completeness and archaeal assemblies 85.57% completeness.
- **E. coli reference set:** 24,393 *E. coli* genomes, averaging 99.72% completeness, 0.41% contamination, 185.04 contigs, and 5,120,392 bp. The set covered 2,162 reported serotypes in the Results section (the Methods reports 2,073 distinct serotypes with O/H typing information).
- **Bacterial MAG set:** 3,137 high-quality bacterial metagenome-assembled genomes from different GTDB families, averaging 85.22% completeness and 1.67% contamination. This set evaluated annotation stability in incomplete and contaminated assemblies.
- **Frameshift simulations:** 32,914 genomes were modified with pseudo-random deletions of 0.5%, 1%, or 2% of nucleotides, producing 98,742 condition-specific data points. This set evaluated resilience to sequencing/assembly errors.
- **Temporal comparison:** Current PGAP annotations were compared with older annotation metadata in GTDB for genomes submitted between 2000 and 2021, assessing the effect of database and pipeline updates.

## Experimental Procedure

- Query GTDB release 207.0 for bacterial and archaeal metadata, download assemblies from NCBI Datasets, and assess completeness, contamination, contig count, and genome size.
- Annotate each genome with Prokka 1.15.6, Bakta 1.7, EggNOG-mapper, and PGAP using recommended settings; use translation table 4 for Mycoplasmatota where required.
- Compare total, described, and undescribed coding density; feature-length distributions; rRNA, tRNA, and tmRNA counts; database accession coverage; and GO coverage and richness.
- Use *E. coli* as a low-taxonomic-variability baseline with expected RNA-feature properties as quality references.
- Stratify analyses by Bacteria versus Archaea, genome fragmentation, MAG status, and simulated frameshift level; inspect relevant results in Figs. 2–5 and supplementary tables.
- Compare recent PGAP feature counts with older GTDB annotations to estimate temporal effects of database updates.

## Key Biology Insights

- Annotation quality is task-dependent: maximizing described bacterial coding space favors Bakta, while maximizing total coding space and robustness in difficult assemblies favors PGAP.
- PGAP is the most consistent choice for archaeal genomes, bacterial MAGs, fragmented genomes, and frameshifted sequences.
- GO coverage and GO richness measure different biological utility. PGAP assigns terms to more genes, while EggNOG-mapper supplies more terms per annotated gene; running both can be complementary.
- Fragmentation reduces complete rRNA-operon detection for all tools, but PGAP often identifies more rRNA sequence pieces in highly fragmented assemblies.
- Annotation databases and pipelines need regular updates: newer PGAP annotations detected on average 139.8 more features than older metadata annotations.

## Implications

Users should choose an annotator according to organism, assembly quality, compute/storage constraints, and whether the priority is feature discovery, described coding density, RNA detection, GO coverage, or GO richness. Bakta is a strong default for high-quality bacterial isolates; PGAP is preferable for archaea and problematic assemblies; EggNOG-mapper is useful when rich functional descriptions are the priority; and Prokka remains a lightweight option when resources are severely constrained, but its functional annotation is comparatively limited. The study also supports combined workflows and standardized, machine-readable outputs for future annotation systems.

