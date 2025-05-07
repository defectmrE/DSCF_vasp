# VASP ∆SCF Excited-State Defect Computations

This repository provides input and output files for VASP calculations used in excited-state defect computations with the ∆SCF approach. It also includes a Python script for ordering wavefunction files and a patch file to fix DSCF behavior in VASP 5.4.4.

## Repository Structure

- **from_scratch**  
  Contains VASP input and output files for calculations performed entirely from scratch.

- **hse_restart**  
  Contains VASP input and output files for calculations restarted using the HSE wavefunction.

- **pbe_restart**  
  Contains VASP input and output files for calculations restarted using the PBE wavefunction.

- **orderWfcs.py**  
  A Python script designed to order wavefunction (WAVECAR) files.

- **subrot_fix.patch**  
  A patch file to correct the DSCF behavior in VASP version 5.4.4.

## Overview

The VASP calculations in this repository are related to excited-state defect computations of neutral SiV<sup>0</sup> in diamond using the ∆SCF method. For detailed information, please refer to the document:  
**"How to perform ∆SCF in VASP for excited-state defect computations: tips and pitfalls."**

## Requirements

- **VASP 5.4.4**  

- **Python 3.x**  
  Required for running the `orderWfcs.py` script.

## Usage

### Applying the DSCF Patch

To fix the DSCF behavior in VASP 5.4.4, apply the provided patch file:

```bash
patch -p1 < subrot_fix.patch
```
See details of the batch in Bulancea-Lindvall, O., Davidsson, J., Ivanov, I. G., Gali, A., Ivády, V., Armiento, R., & Abrikosov, I. A. (2024). Temperature dependence of the AB lines and optical properties of the carbon–antisite-vacancy pair in 4H-SiC. Physical Review Applied, 22, 034056. https://doi.org/10.1103/PhysRevApplied.22.034056"
