# Spatial organization of bacterial transcription and translation

**Authors:** Michele Castellana et al.  
**Journal:** Proceedings of the National Academy of Sciences (PNAS)  
**Year:** 2016  
**DOI:** 10.1073/pnas.1604995113  
**PMC ID:** PMC4995950

---

## Main Idea

This paper investigates the spatial organization of transcription and translation in bacterial cells, specifically in *Escherichia coli*. The central finding is that bacterial cells exhibit a striking spatial organization where DNA is compacted into a nucleoid near the cell center, while ribosomes are mainly localized to the cell poles. The authors combine theoretical modeling (reaction-diffusion models) with experimental analysis to understand how this spatial organization impacts gene expression and to predict the extent of mRNA localization.

## Main Novelty

1. **Reaction-Diffusion Model**: The authors develop a minimal 1D reaction-diffusion model for the coupled dynamics of ribosomes and mRNAs in *E. coli*, accounting for excluded-volume effects and transient ribosome-mRNA interactions.

2. **Prediction of mRNA Segregation**: The model predicts that approximately **90% of mRNAs are segregated to the cell poles**, away from the nucleoid—providing the first quantitative prediction of genome-wide mRNA-nucleoid segregation.

3. **Ribosome Circulation**: The analysis reveals a "circulation" of ribosomes driven by mRNA flux—from synthesis in the nucleoid to degradation at the poles.

4. **Nucleoid Size Determination**: The study confirms that observed nucleoid size stems from a balance between forces exerted by the chromosome and mRNAs on each other, suggesting a potential global feedback circuit where gene expression feeds back on itself via nucleoid compaction.

5. **Robustness Analysis**: The results are shown to be robust with respect to mRNA degradation by RNase enzymes, different cell division cycle phases, growth rates, and nonspecific transient ribosome-mRNA interactions.

## Main Datasets Used for Evaluation

The study relies on:

1. **Experimental Imaging Data**: DNA fluorescence profiles from *E. coli* cells grown in glucose minimal media, stained with SYTOX Orange and imaged at exponential phase (35 cells analyzed).

2. **Ribosome Localization Data**: In vivo measurements of ribosomal protein S2-YFP to visualize ribosome distribution relative to the nucleoid.

3. **Diffusion Coefficients**: Prior experimental measurements of ribosome and mRNA diffusion coefficients in living *E. coli* cells:
   - Free ribosome diffusion coefficient: ~0.4 μm²/s
   - Polysome (mRNA-bound ribosome) diffusion coefficient: ~0.05 μm²/s

4. **Cellular Parameters**: Established values from literature:
   - ~1.5 mm of supercoiled DNA compacted into ~1 μm³ nucleoid volume
   - Average nucleoid pore diameter: ~50 nm
   - Ribosome diameter: ~20 nm
   - Total ribosomes per cell: ~60,000
   - Mean mRNA lifetime: ~5 minutes
   - Total mRNAs per cell: ~5,000

## Experimental Procedure

### Theoretical Modeling
1. **1D Reaction-Diffusion Model**: Developed a model along the long axis of the cell (coordinate x), modeling only the right half (0 to ℓ) assuming left-right symmetry.

2. **State Variables**: Tracked:
   - Concentration of free ribosomes: cF(x)
   - Density of mRNAs with m transiently bound (B) ribosomes and n translating (T) ribosomes: ρm,n(x)

3. **Exclusion Volume Effects**: Implemented fractional available volume v(x) within the nucleoid that depends on the number of ribosomes bound to mRNA.

4. **Steady-State Solution**: Solved equations at steady-state with constraints on total ribosome number and no-flux boundary conditions.

### Numerical Analysis
- Solved the model in the rapid-equilibrium limit for transiently bound ribosomes
- Fixed maximal translating ribosomes per mRNA at nmax = 24
- Computed mRNA density profiles and ribosome concentrations

### Validation and Robustness Testing
The model was tested for robustness against:
- RNase-mediated mRNA degradation
- Different cell division cycle phases and growth rates
- Existence of nonspecific transient ribosome-mRNA interactions
- Extended models including 30S and 50S ribosomal subunits

### Key Findings
- **mRNA Distribution**: Most mRNAs are loaded with ~10 translating ribosomes and ~2 transiently bound ribosomes
- **Segregation**: Strong mRNA segregation away from the nucleoid due to excluded-volume effects
- **Ribosome Concentration Gradients**: Translating (T), transiently bound (B), and free (F) ribosomes show distinct spatial distributions with flux patterns from nucleoid to poles

## Key Biological Insights

1. **Physical Origin of Localization**: The nucleoid forms a dense DNA mesh (average pore diameter ~50 nm) that excludes polysomes (effective diameter ≳50 nm) while allowing free ribosomes (~20 nm) to diffuse through.

2. **Functional Implications**: mRNAs diffuse out of the nucleoid to ribosome-rich regions (poles) in seconds—much faster than mRNA lifetime (~5 min)—ensuring colocalization of mRNAs with ribosomes where bulk translation occurs.

3. **Feedback Circuit**: The balance between forces exerted by the chromosome and mRNAs suggests a global feedback mechanism where gene expression influences nucleoid compaction.

## Conclusion

This work provides a quantitative framework for understanding bacterial subcellular organization and its functional consequences for protein synthesis. The combination of reaction-diffusion modeling with experimental validation demonstrates how physical constraints (excluded-volume effects) shape the spatial organization of essential cellular processes in bacteria.

---

*Keywords: bacteria, translation, localization, modeling, experiments, nucleoid, ribosomes, mRNA, E. coli*
