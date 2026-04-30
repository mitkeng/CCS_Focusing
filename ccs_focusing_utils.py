
import os, re, shutil, io
import pandas as pd
import numpy as np
import tensorflow as tf
from ase import io as ase_io
try: from rdkit import Chem; from rdkit.Chem import AllChem
except: pass
try: import pymol; from pymol import cmd
except: pass

def smiles_to_xyz(smiles, filename='molecule.xyz'):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    AllChem.MMFFOptimizeMolecule(mol)
    conf = mol.GetConformer()
    with open(filename, 'w') as f:
        f.write(str(mol.GetNumAtoms()) + '\n\n')
        for atom in mol.GetAtoms():
            pos = conf.GetAtomPosition(atom.GetIdx())
            f.write(f'{atom.GetSymbol()} {pos.x:10.4f} {pos.y:10.4f} {pos.z:10.4f}\n')
    return filename

def get_physical_features(xyz_path):
    mol = ase_io.read(xyz_path)
    mass = sum(mol.get_masses())
    com = mol.get_center_of_mass(scaled=False)
    cmd.reinitialize(); cmd.load(xyz_path, 'temp_mol')
    cmd.set('dot_solvent', 0); cmd.set('dot_density', 2)
    sa = cmd.get_area('temp_mol')
    return np.array([[mass, com[0], com[1], sa, 1.0]])

def filter_and_siphon_conformers(model, folder_path, experimental_ccs, std_error, compound_name='Focused'):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.xyz')]
    upper, lower = experimental_ccs*(1+std_error), experimental_ccs*(1-std_error)
    output_dir = f'{compound_name}_CCS_{experimental_ccs}'
    os.makedirs(output_dir, exist_ok=True)
    captured_count = 0
    for filename in files:
        try:
            path = os.path.join(folder_path, filename)
            feat = get_physical_features(path)
            pred = model.predict(feat, verbose=0)[0][0]
            if lower <= pred <= upper:
                shutil.copy(path, os.path.join(output_dir, filename))
                captured_count += 1
        except: continue
    print(f'Done! {captured_count} conformers siphoned into {output_dir}')
    return output_dir
