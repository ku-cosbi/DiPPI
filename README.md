
# DiPPI

DiPPI (Drugs in Protein-Protein Interfaces) provides a dataset for the investigation of drug-like small molecules in protein interfaces. DiPPI website can be accessed at http://interactome.ku.edu.tr:8501. 

<img width="407" alt="manuscript_flowchart_15092022" src="https://github.com/ku-cosbi/DiPPI/assets/26777185/41d47e78-f78e-4109-b99c-10afb3005a48">


## Datasets

- **drugs_in_interface**: Small molecules analyzed in this study. PDB ligand ID and FDA approval of the molecule are provided.
- *eliminatedMolecules**: Small molecules eliminated in the study are listed. These molecules are not available on the website.
- **ligandData**: Molecular descriptors of the ligand data, along with other characteristics such as FDA approval, source database, ECFP4 and Pharmacophore fingerprint clusters, SMILES ID and more.
- **ligand_data_fda**: FDA-approved subset of the ligand data.
- **protein_summary**: Summary information of used protein interfaces with their corresponding ligand information.
- **protein_summary_fda**: FDA-approved subset of the interface data.



- **featurevector_calm1_xx** : Feature vector created for benchmarking CALM1 variations. AF and PDB versions, as well as imputed and not imputed versions are found in the relevant folders.
- **training_uptodate_full_pdb_imputed_wo3genes** : Imputed PDB training feature vector without datapoints from BRCA1, P53 and CALM1.File is zipped due to size limitations.
- **training_uptodate_full_pdb_raw_wo3genes** : Non-imputed PDB training feature vector without datapoints from BRCA1, P53 and CALM1.
- **training_uptodate_full_alphafold_imputed_wo3genes** : Imputed AlphaFold training feature vector without datapoints from BRCA1, P53 and CALM1. File is zipped due to size limitations.
- **training_uptodate_full_alphafold_raw_wo3genes** : Non-imputed AlphaFold training feature vector without datapoints from BRCA1, P53 and CALM1.
