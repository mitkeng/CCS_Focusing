
<br /><img align = "center" width="550" alt="focus" src="https://github.com/mitkeng/CCS_Focusing/assets/97419520/2e01119f-7dc2-4361-aca7-60e17e7fda79">
<br />
<br />
<br />

### CCS Focusing is a sequential machine learning model implemented in a python executable platform for use to reduce the number of conformers sampled post conformation generation. This is done by predicting the gas phase collisional cross section (molecular descriptor) values of raw conformers to determine their ion-mobility mass spectrometry gas phase relevance. 
<br />

### The model is trained on molecular features obtained from 3D structures that have been geometry optimized at the DFT D3BJ-B3LYP/6-31G(d,p) for cation and D3BJ-B3LYP/6-31+G(d,p) level of theory for anion.
<br />

### The advantage ultimately is reduced computational workload downstream (e.g., quantum mechanical calculations) and improved gas phase structure prediction precision. It is currently only appropriate for lipid molecules. 
<br />

### This program takes in an ensemble of raw conformers in atomic cartesian xyz format as input. Only filtering and partitioning of conformers are accomplished; no alteration to conformer physical property is done. Connection to google drive for importing and exporting data or results is supported. 
### Click [CCS Focusing](https://colab.research.google.com/drive/1Sr0ydH5AGFRG15xTjFpZHpcZPgy4k1Lp#scrollTo=-DId6ORx7rPy) to access the google Colab platform for use. 

<br />
<br />

<br />
<br />


<br />
<br />

