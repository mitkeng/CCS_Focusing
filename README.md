[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) [![tensorflow](https://img.shields.io/badge/TensorFlow-1.12-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org) ![user](https://img.shields.io/badge/GoogleColab-grey?style=flat&logo=googlecolab) ![user](https://img.shields.io/badge/Chemodeling-App-yellow?) ![user](https://img.shields.io/badge/Userfriend-1.0-sgreen?) 

# CCS Focusing: conformational space focusing and ensemble distillation

<br /><img align = "center" width="500" alt="image_1062b0ce" src="https://github.com/user-attachments/assets/541656b3-91f1-454c-ba66-338ac81f12dc">
<br />

#
### Introduction
 CCS Focusing is a sequential machine learning model implemented in a python executable platform for use to reduce the number of conformers sampled post conformation generation, which is often necessary when modeling highly flexible systems like fatty acids. This is done by predicting the gas phase ion-neutral (*i.e.*, $N_{2}$) collisional cross section (a molecular descriptor within the confines of ion-mobility mass spectrometry) values of raw conformers to determine their ion-mobility mass spectrometry (IM-MS) gas phase relevance. 
<br />
The model is trained on computed CCS values from 3D structures that have been geometry optimized at the density functional theory (DFT) D3BJ-B3LYP/6-31G(d,p) for cation, $[M+H]^+$, and D3BJ-B3LYP/6-31+G(d,p) level of theory for anion, $[M-H]^-$.
<br />

 The advantages ultimately are reduced computational workload downstream (*e.g.*, quantum mechanical calculations) and improved gas phase structure prediction precision. Currently, the only model in this repository that has been validated for use is the *lipid_model.keras* for lipids; validations for other biomolecule classes are currently in progress. 
<br />
<br />
#
### Performance 
The latest CCS prediction performance using our current dataset for lipid class molecules as compared to DFT derived CCS values is as follow: 

<img align = "center" width="500" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/6704197c-f48a-4212-b065-b6d04a798b49"> 
<br />

## 📘 Step-by-Step User Guide: CCS Focusing Pipeline


### **1. Environment Setup**
The pipeline requires a mix of scientific libraries and machine learning frameworks. 

**Automated Installation:**
Run the provided shell script. It installs scientific packages (PyMOL, RDKit, ASE) via Mamba and Python dependencies via Pip.
```bash
chmod +x setup_env.sh
./setup_env.sh
```

**Manual Installation (Fallback):**
If you prefer manual control, ensure you have a Conda environment active and run:
```bash
mamba install -c conda-forge rdkit ase pymol-open-source -y
pip install -r requirements.txt
```

---

### **2. Batch CCS Prediction**
To predict CCS values for a folder full of `.xyz` files and save them to a CSV report:

**Command:**
```bash
python predict_ensemble.py --folder ./your_xyz_folder --output results.csv
```
- `--folder`: Path to your directory containing conformers.
- `--output`: The name of the CSV file where predictions will be stored.

---

### **3. CCS Focusing (Siphoning)**
This command identifies conformers that match your experimental reference value and copies them to a new 'focused' directory.

**Command:**
```bash
python predict_ensemble.py \
    --folder ./your_xyz_folder \
    --target 145.0 \
    --tolerance 0.05 \
    --name MyMolecule \
    --output focused_results.csv

- `--target`: Your experimental CCS value (in Å²).
- `--tolerance`: The allowed deviation (e.g., `0.05` for 5%).
- `--name`: Prefix for the output folder (e.g., `MyMolecule_Target_145.0`).
```


### **4. Using the Python API**
You can integrate these utilities into your own Python workflow using the `ccs_focusing_utils` module.

```python
import tensorflow as tf
import ccs_focusing_utils as ccs_utils

# 1. Load the model
model = tf.keras.models.load_model('ML_ccs.keras')

# 2. Predict and siphon match conformers in one go
focused_dir = ccs_utils.filter_and_siphon_conformers(
    model=model,
    folder_path='input_xyz_files',
    experimental_ccs=142.5,
    std_error=0.03,
    compound_name='Inhibitor_Project'
)

print(f"Focused conformers saved in: {focused_dir}")
```


#
### Remarks and Requirement 
This program takes in an ensemble of raw conformers in atomic cartesian xyz format as input. As mentioned prior, CCS is predicted for $N_{2}$  as the neutral IM-MS collision gas. Only filtering and partitioning of conformers are accomplished; no alteration to conformer physical property is done. The filter size is automatically constructed from the model's latest performance standard prediction error and a user input reference CCS value. 

Additional unvalidated models for other biomolecule classes are made available as dropdown options for use, but proceed with discretion. 

Connection to Google Colab Notebook is required. Connecting to Google Drive for importing and exporting data or results are supported. 
<br />
<br />

#
### Web Application Option
 [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">](https://colab.research.google.com/drive/1ZTLqHMI-rdoHQZ4zjElK4VEPLQhXcUp6?usp=sharing) <code style="color : grey">to access CCS Focusing platform.</code>
<br />

#
### Complementary
  [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">](https://colab.research.google.com/drive/1HiXUZB65Ryf71YyuKg_V3VIWjwuRGXAR?usp=sharing) <code style="color : grey">to access proGENi conformation generation platform.</code>

<br />

#
### Citation
Keng, M.; Merz, K. M., Jr. Eliminating the Deadwood: A Machine Learning Model for CCS Knowledge-Based Conformational Focusing for Lipids. Journal of Chemical Information and Modeling 2024. DOI: 10.1021/acs.jcim.4c01051.


#
### Acknowledgement 
[Merz research group](https://github.com/merzlab) 

Quantum mechanical calculations and data used in building this model were organically generated through computational resources and services provided by the Institute for Cyber-Enabled Research [(ICER)](https://github.com/MSU-iCER) at Michigan State University.

<br/>
<br/>


