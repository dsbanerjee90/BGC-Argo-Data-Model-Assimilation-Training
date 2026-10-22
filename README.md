# BGC-Argo Data and Model Assimilation Training

Hands-on training material for working with numerical ecosystem-model output, satellite observations, BGC-Argo observations, data assimilation concepts, and a short machine-learning extension.

**Author:** Deep S. Banerjee  
**Plymouth Marine Laboratory (PML)**  
**Funded by the European Space Agency (ESA)**

ESA Climate and Marine Production (CAMP):  
https://climate.esa.int/en/observations-and-modelling/camp/

> This repository is prepared for participants attending the training session. Please complete the software setup before the class. The practical itself will be guided during the session.

## Repository structure

```text
BGC-Argo-Data-Model-Assimilation-Training/
├── BGC_Argo_Data_and_Model_Data_Assimilation.ipynb
├── environment.yml
├── README.md
├── data/
├── images/
└── scripts/
```

Keep the folder structure unchanged so that the notebook can find the supplied data and images.

## 1. Install Conda / Mamba

For the smoothest setup, **Miniforge is recommended** because it includes Conda/Mamba and uses conda-forge.

Official Miniforge downloads:  
https://github.com/conda-forge/miniforge/releases

### macOS

Check your Mac architecture:

```bash
uname -m
```

- `arm64` → Apple Silicon
- `x86_64` → Intel Mac

Download the matching Miniforge installer, run it, and allow it to initialise your shell. Then close and reopen Terminal.

### Linux

Check the architecture:

```bash
uname -m
```

Download the matching Miniforge Linux installer from the link above, install it, and reopen the terminal.

### Windows

Download the Miniforge Windows installer from the link above and complete the installation. Open **Miniforge Prompt** after installation.

### Already have Conda?

A recent Conda installation is fine. If environment solving is extremely slow or your Conda version is very old, installing Miniforge is recommended rather than modifying the old installation.

Check with:

```bash
conda --version
```

## 2. Get the course material

Clone the repository:

```bash
git clone https://github.com/dsbanerjee90/BGC-Argo-Data-Model-Assimilation-Training.git
cd BGC-Argo-Data-Model-Assimilation-Training
```

Alternatively, download the repository as a ZIP from GitHub and extract it.

## 3. Create the course environment

Using Mamba:

```bash
mamba env create -f environment.yml
```

or using Conda:

```bash
conda env create -f environment.yml
```

Activate it:

```bash
conda activate ecosystem-training
```

or:

```bash
mamba activate ecosystem-training
```

## 4. Check the installation

From the repository directory run:

```bash
python scripts/check_setup.py
```

A successful installation ends with:

```text
COURSE SETUP CHECK: PASSED
```

If it does not pass, resolve the reported missing package/file before the session.

## 5. Register the Jupyter kernel

Run once:

```bash
python -m ipykernel install --user --name ecosystem-training --display-name "Ecosystem Model Training"
```

## 6. Launch JupyterLab

Run:

```bash
jupyter lab
```

or on macOS/Linux:

```bash
bash scripts/launch_training.sh
```

On Windows:

```bat
scripts\launch_training.bat
```

Open:

```text
BGC_Argo_Data_and_Model_Data_Assimilation.ipynb
```

and, if asked, select the kernel:

```text
Ecosystem Model Training
```

## Before the session

Please make sure that:

- the repository has been downloaded;
- the `ecosystem-training` environment has been created;
- `python scripts/check_setup.py` reports **PASSED**;
- JupyterLab opens successfully;
- the **Ecosystem Model Training** kernel is available.

No specialist ocean-model installation, HPC account, or GPU is required.

## Troubleshooting

### Environment solving takes a very long time

This is most commonly seen with an old Conda installation. Miniforge/Mamba is recommended.

### `ModuleNotFoundError`

Activate the environment before launching Jupyter:

```bash
conda activate ecosystem-training
jupyter lab
```

### Wrong notebook kernel

In JupyterLab choose:

**Kernel → Change Kernel → Ecosystem Model Training**

### Missing image or data file

Keep the repository folder structure unchanged. The notebook uses relative paths to the `data/` and `images/` directories.
