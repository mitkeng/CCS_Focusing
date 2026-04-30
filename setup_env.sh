#!/bin/bash
# setup_env.sh - Installation script for CCS Focusing Utilities

echo "Starting installation of dependencies..."

# 1. Install core scientific dependencies via Mamba (preferred for PyMOL)
mamba install -c conda-forge rdkit ase pymol-open-source pandas numpy matplotlib seaborn -y

# 2. Install Python libraries using the requirements file
if [ -f requirements.txt ]; then
    echo "Installing Python dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "Warning: requirements.txt not found, installing defaults..."
    pip install tensorflow tensorflow-decision-forests py3Dmol
fi

echo "Installation Complete."
