# BGC-Argo Data and Model Assimilation Training

Pre-class setup repository for the hands-on training session.

**Author:** Deep S. Banerjee  
**Plymouth Marine Laboratory (PML)**  
**Funded by the European Space Agency (ESA)**

ESA Climate and Marine Production (CAMP):  
https://climate.esa.int/en/observations-and-modelling/camp/

> **Participants:** please complete the software setup below before attending the session.  
> The practical notebook, datasets, figures, exercises, and solutions will be provided during the class.

## What you need before the session

You only need:

- a laptop running Windows, macOS, or Linux;
- internet access for the initial software installation;
- Conda/Mamba;
- the `ecosystem-training` environment created successfully;
- JupyterLab working on your computer.

No specialist ocean-model installation, HPC account, or GPU is required.

---

## 1. Install Conda / Mamba

For the smoothest setup, **Miniforge is recommended**. It provides Conda and Mamba and uses the conda-forge package ecosystem.

Official Miniforge downloads:

https://github.com/conda-forge/miniforge/releases

### macOS

Open Terminal and check your Mac architecture:

```bash
uname -m
```

The result tells you which Miniforge installer to download:

- `arm64` → Apple Silicon (M1/M2/M3/M4...)
- `x86_64` → Intel Mac

Download the matching **macOS** Miniforge installer from the link above.

After installation, allow Miniforge to initialise your shell when asked. Then close and reopen Terminal.

Check:

```bash
which conda
conda --version
which mamba
mamba --version
```

### Linux

Open a terminal and check your architecture:

```bash
uname -m
```

Download the matching **Linux** Miniforge installer from the link above, install it, and reopen the terminal.

Then check:

```bash
conda --version
mamba --version
```

### Windows

Download the Windows Miniforge installer from:

https://github.com/conda-forge/miniforge/releases

Complete the installation and then open **Miniforge Prompt**.

Check:

```bat
conda --version
mamba --version
```

### Already have Conda?

A recent Conda installation is fine.

Check:

```bash
conda --version
```

If environment solving takes a very long time, particularly with an older Conda installation, installing a current Miniforge distribution is recommended.

---

## 2. Download this repository

### Using Git

```bash
git clone https://github.com/dsbanerjee90/BGC-Argo-Data-Model-Assimilation-Training.git
cd BGC-Argo-Data-Model-Assimilation-Training
```

### Without Git

On GitHub choose:

**Code → Download ZIP**

Extract the ZIP and open a terminal/Miniforge Prompt inside the extracted folder.

---

## 3. Create the training environment

Using Mamba (recommended):

```bash
mamba env create -f environment.yml
```

or using Conda:

```bash
conda env create -f environment.yml
```

The environment is called:

```text
ecosystem-training
```

---

## 4. Activate the environment

Using Conda:

```bash
conda activate ecosystem-training
```

or:

```bash
mamba activate ecosystem-training
```

Your command prompt should now show `ecosystem-training`.

---

## 5. Check the installation

From the repository directory run:

```bash
python scripts/check_setup.py
```

A successful installation ends with:

```text
COURSE SETUP CHECK: PASSED
```

Please make sure you see this message before attending the session.

---

## 6. Register the Jupyter kernel

With `ecosystem-training` activated, run:

```bash
python -m ipykernel install --user --name ecosystem-training --display-name "Ecosystem Model Training"
```

This only needs to be done once on each computer.

---

## 7. Test JupyterLab

Run:

```bash
jupyter lab
```

JupyterLab should open in your web browser.

You do not need a course notebook yet. If JupyterLab opens successfully, the test is complete.

You can stop JupyterLab with **Ctrl+C** in the terminal.

---

## Final pre-class checklist

Before arriving, please confirm:

- [ ] Conda or Mamba works
- [ ] the `ecosystem-training` environment exists
- [ ] `python scripts/check_setup.py` reports **PASSED**
- [ ] the **Ecosystem Model Training** kernel has been registered
- [ ] JupyterLab opens successfully

The remaining course material will be provided during the training session.

## Troubleshooting

### Environment creation is extremely slow

This can happen with older Conda installations. A current Miniforge installation with Mamba is recommended.

### `conda activate` does not work immediately after installing Miniforge

Close and reopen the terminal first.

On macOS/Linux you can also reload your shell configuration where appropriate.

### `ModuleNotFoundError`

Make sure the environment is active:

```bash
conda activate ecosystem-training
```

Then run the setup check again:

```bash
python scripts/check_setup.py
```

### JupyterLab opens with the wrong Python environment

Register the course kernel again:

```bash
python -m ipykernel install --user --name ecosystem-training --display-name "Ecosystem Model Training"
```

Then select **Ecosystem Model Training** from JupyterLab when required.
