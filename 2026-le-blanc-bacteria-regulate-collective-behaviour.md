# Paper Summary

### Authors

Laure Le Blanc, Giona Cattaneo, Nathel Heraud, Einollah Sarikhani, Dhivya Pushpa Meganathan, Chia-Ni Tsai, Anum Tahir, Marco J. Kühn, Zeinab Jahed, Sangwoo Kim and Alexandre Persat.

### Journal

Nature Microbiology.

### Publication Date

Online publication date is not specified in the supplied PDF. The manuscript was accepted on 10 September 2026.

### DOI

https://doi.org/10.1038/s41564-026-02505-1

## Keywords

Pseudomonas aeruginosa; mechanosensing; type IV pili; twitching motility; contact-induced reversal; bacterial collectives; active matter; navigation.

## Main Idea

Pseudomonas aeruginosa uses cell-cell collisions as sensory information. Collision-induced reversals (CRs), mediated by the Pil-Chp mechanosensory system, prevent dense populations from becoming trapped in strongly aligned groups. This feedback produces disordered motion in crowded regions but preserves coordinated outward motion at colony edges, improving collective spreading and navigation.

## Evidence Supporting the Main Idea

- At high surface density, non-reversing ΔpilH cells formed clusters and strongly aligned groups, whereas wild-type (WT) and constitutively reversing ΔpilG cells remained more uniformly distributed and locally disordered (Fig. 1).
- WT cells changed from persistent, near-ballistic motion at low density to more tortuous, weakly superdiffusive motion at high density. ΔpilH remained quasi-ballistic and ΔpilG remained approximately diffusive (Fig. 3).
- PilG polarization was randomly oriented in the colony core but aligned toward open space at the WT leading edge, consistent with density-dependent regulation of collective direction.
- Agent-based simulations reproduced the experimental patterns and showed that increasing CR probability was sufficient to suppress clustering and nematic order; cell speed had little effect on ordering (Fig. 2 and Extended Data Fig. 3).
- WT outcompeted both ΔpilH and ΔpilG in surface-expansion assays. WT also outcompeted a short, non-reversing ΔpilH cyaB strain, showing that adaptive reversal control provides an advantage beyond simply reducing cell elongation.
- In micromazes, WT cells explored about 92% of the maze area and approximately 20% escaped, compared with about 65% explored and 1% escape for ΔpilH cells (Fig. 4).

## Main Novelty

The study shows that cell-cell interactions are not only mechanical causes of collective order; they also generate sensory information that bacteria feed back into motility control. CRs therefore act as a rapid, density-dependent behavioural switch, complementing slower or more spatially diffuse chemical signalling systems.

## Datasets Used for Evaluation

- Live phase-contrast and fluorescence microscopy of surface-twitching P. aeruginosa populations at approximately 10%, 30% and 70% surface coverage. These data measured spatial organization, cell shape, polarization and trajectories; replicate numbers varied by experiment and are reported in the figure legends and Supplementary Table 5.
- Single-cell trajectory datasets from fluorescently labelled subpopulations. These were used to quantify persistence and mean-squared-displacement exponents.
- WT-mutant competition assays, generally initiated at a 1:1 mixture, used to measure relative abundance at expanding colony fronts.
- Micromaze navigation datasets from photolithographically fabricated glass mazes, used to quantify residence, area coverage and escape probability; the reported experiments used biological triplicates.
- Agent-based simulations of repulsive, self-propelled spherocylinders, calibrated using measured cell dimensions and reversal frequencies. Simulations varied aspect ratio and CR probability to map spreading and nematic order.
- Experimental datasets and analysis/simulation code are available through Zenodo records 20430747 and 22231353, as cited by the paper.

## Experimental Procedure

- Construct WT, reversal-defective, constitutively reversing and cell-shape control strains of P. aeruginosa.
- Grow cells on agarose surfaces and image populations across controlled density levels.
- Segment cells and use Voronoi tessellations, area-distribution skewness and nematic correlation decay length to quantify spreading and order.
- Track fluorescently labelled cells and measure persistence and mean-squared displacement across density regimes and colony locations.
- Image PilG polarization at colony cores and leading edges to connect local contact conditions with polarity.
- Perform agent-based simulations and calibrate them against the measured cell geometry and reversal behaviour.
- Compete WT against mutant strains and compare their expansion and spatial distributions.
- Seed cells into microfabricated mazes and quantify exploration, wall/corner accumulation and successful escape.

## Key Biology Insights

- The Pil-Chp system converts physical obstruction of polar type IV pili into a polarity switch and reversal within seconds.
- Frequent collisions in crowded regions generate reversals that disrupt alignment and promote dispersal.
- At open colony edges, asymmetric contacts orient cells toward unexplored space and allow coordinated outward motion.
- Collective reversals are context-dependent: in this system they promote dispersal, whereas reversals in other bacteria can promote cohesive streams.
- Mechanosensing can provide navigational information where chemical gradients are weak, transient or unreliable.

## Implications

The work establishes mechanosensory feedback as a mechanism by which bacterial collectives actively regulate their own organization. It may help explain how surface-associated P. aeruginosa spreads through heterogeneous environments and could inform designs of adaptive active-matter or robotic swarms. The experiments are performed in controlled surface-twitching environments, so the quantitative relevance of the mechanism in host tissues, natural soils and mature biofilms remains to be tested.
