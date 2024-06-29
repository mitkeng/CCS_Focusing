## CCS Focusing: conformational space focusing and ensemble distillation

<br /><img align = "center" width="550" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/2e01119f-7dc2-4361-aca7-60e17e7fda79">
<br />
<br />
<br />
### Introduction
 CCS Focusing is a sequential machine learning model implemented in a python executable platform for use to reduce the number of conformers sampled post conformation generation. This is done by predicting the gas phase collisional cross section (a molecular descriptor within the confines of ion-mobility mass spectrometry) values of raw conformers to determine their ion-mobility mass spectrometry gas phase relevance. 
<br />

 The model is trained on molecular features obtained from 3D structures that have been geometry optimized at the density functional theory (DFT) D3BJ-B3LYP/6-31G(d,p) for cation and D3BJ-B3LYP/6-31+G(d,p) level of theory for anion.
<br />

 The advantages ultimately are reduced computational workload downstream (*e.g.*, quantum mechanical calculations) and improved gas phase structure prediction precision. The model is currently only appropriate for lipid molecules; validations for other biomolecule classes are currently in progress. 
<br />
<br />

### Performance 
The latest CCS prediction performances using our current datasets for three molecule classes as compared to DFT derived CCS values are as follow: 

<img align = "left" width="400" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/6704197c-f48a-4212-b065-b6d04a798b49">
<img align = "center" width="400" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/33d3fd35-2971-416b-b5e0-f66cea68de54">
<img align = "left" width="400" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/ed54742b-c178-4632-84b3-9d2081ddaf93">
<img align = "center" width="400" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/c9467f02-3343-46a8-b54c-4c43b76e921b">
<br />

### Requirement and Disclaimer
 This program takes in an ensemble of raw conformers in atomic cartesian xyz format as input. Only filtering and partitioning of conformers are accomplished; no alteration to conformer physical property is done. Connection to google drive for importing and exporting data or results are supported. 
<br />
<br />


### Accessible
 [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">](https://colab.research.google.com/drive/1ZTLqHMI-rdoHQZ4zjElK4VEPLQhXcUp6?usp=sharing) <code style="color : grey">to access CCS Focusing platform.</code>
<br />

### Complementary
  [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">](https://colab.research.google.com/drive/1HiXUZB65Ryf71YyuKg_V3VIWjwuRGXAR?usp=sharing) <code style="color : grey">to access proGENi conformation generation platform.</code>

<br />

### Acknowledgement 
[Merz research group](https://github.com/merzlab) 

Quantum mechanical calculations and data used in building this model were organically generated through computational resources and services provided by the Institute for Cyber-Enabled Research [(ICER)](https://github.com/MSU-iCER) at Michigan State University.

<br/>
<br/>

<br />

<img align = "right" width="75" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/c02957e7-bf41-43ce-860c-4927420b2f20">
