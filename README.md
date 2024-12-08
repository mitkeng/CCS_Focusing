[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) [![tensorflow](https://img.shields.io/badge/TensorFlow-1.12-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org) ![user](https://img.shields.io/badge/GoogleColab-grey?style=flat&logo=googlecolab) ![user](https://img.shields.io/badge/Chemodeling-App-yellow?) ![user](https://img.shields.io/badge/Userfriend-1.0-sgreen?) 

# CCS Focusing: conformational space focusing and ensemble distillation

<br /><img align = "center" width="700" alt="focus" src="https://github.com/user-attachments/assets/9855af8d-012f-47d1-8a9c-76cd29e4e592">
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

#
### Remarks and Requirement 
This program takes in an ensemble of raw conformers in atomic cartesian xyz format as input. As mentioned prior, CCS is predicted for $N_{2}$  as the neutral IM-MS collision gas. Only filtering and partitioning of conformers are accomplished; no alteration to conformer physical property is done. The filter size is automatically constructed from the model's latest performance standard prediction error and a user input reference CCS value. 

Additional unvalidated models for other biomolecule classes are made available as dropdown options for use, but proceed with discretion. 

Connection to Google Colab Notebook is required. Connecting to Google Drive for importing and exporting data or results are supported. 
<br />
<br />

#
### Accessibility
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

<br />

<img align = "right" width="75" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/c02957e7-bf41-43ce-860c-4927420b2f20">
