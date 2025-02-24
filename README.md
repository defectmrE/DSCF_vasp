# VASP ∆SCF Excited-State Defect Computations

This repository provides input and output files for VASP calculations used in excited-state defect computations with the ∆SCF approach. It also includes a Python script for ordering wavefunction files and a patch file to fix DSCF behavior in VASP 5.4.4.

## Repository Structure

- **from_scratch/**  
  Contains VASP input and output files for calculations performed entirely from scratch.

- **hse_restart/**  
  Contains VASP input and output files for calculations restarted using the HSE hybrid functional.

- **pbe_restart/**  
  Contains VASP input and output files for calculations restarted using the PBE functional.

- **orderWfcs.py**  
  A Python script designed to order or process wavefunction (WFC) files.

- **subrot_fix.patch**  
  A patch file to correct the DSCF behavior in VASP version 5.4.4.

## Overview

The VASP calculations in this repository are related to excited-state defect computations using the ∆SCF method. For detailed information, tips, and pitfalls related to these calculations, please refer to the document:  
**"How to perform ∆SCF in VASP for excited-state defect computations: tips and pitfalls."**

## Requirements

- **VASP 5.4.4**  
  (Note: Be sure to apply the DSCF patch provided in this repository.)

- **Python 3.x**  
  Required for running the `orderWfcs.py` script.

## Usage

### 1. Applying the DSCF Patch

To fix the DSCF behavior in VASP 5.4.4, apply the provided patch file:

```bash
patch -p1 < subrot_fix.patch
