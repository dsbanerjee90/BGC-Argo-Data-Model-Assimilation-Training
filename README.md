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

For this course, **Miniforge is recommended**. It installs both **Conda** and **Mamba**.

Official download page:

https://github.com/conda-forge/miniforge/releases

### macOS

1. Open the built-in **Terminal** app:

   **Applications → Utilities → Terminal**

2. In Terminal, check whether your Mac is Apple Silicon or Intel:

```bash
uname -m
```

- If it prints `arm64`: download **Miniforge3-MacOSX-arm64.sh**
- If it prints `x86_64`: download **Miniforge3-MacOSX-x86_64.sh**

3. Download the installer directly from Terminal.

For **Apple Silicon (arm64)**:

```bash
cd ~/Downloads
curl -L -o Miniforge3-MacOSX-arm64.sh \
https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
```

For **Intel Mac (x86_64)**:

```bash
cd ~/Downloads
curl -L -o Miniforge3-MacOSX-x86_64.sh \
https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh
```

4. Run the installer.

For Apple Silicon:

```bash
bash Miniforge3-MacOSX-arm64.sh
```

For Intel Mac:

```bash
bash Miniforge3-MacOSX-x86_64.sh
```

5. Follow the installer instructions. When asked whether Miniforge should initialise your shell, answer:

```text
yes
```

6. Close Terminal completely and open it again.

7. Check that Conda and Mamba are available:

```bash
conda --version
mamba --version
```

If both commands print version numbers, the installation is complete.

---

### Linux

1. Open the **Terminal** application.

   On most Linux systems you can search for **Terminal** in the application menu.

2. Check your computer architecture:

```bash
uname -m
```

For most modern Linux computers this will be `x86_64`.

3. Download the matching Linux Miniforge installer from:

https://github.com/conda-forge/miniforge/releases

For a standard x86_64 Linux computer, the file is:

```text
Miniforge3-Linux-x86_64.sh
```

4. In Terminal, go to your Downloads folder:

```bash
cd ~/Downloads
```

5. Run the installer:

```bash
bash Miniforge3-Linux-x86_64.sh
```

6. Follow the installer instructions and answer `yes` when asked whether to initialise the shell.

7. Close the Terminal and open it again.

8. Check:

```bash
conda --version
mamba --version
```

If both commands print version numbers, the installation is complete.

---

### Windows

Windows is supported, although macOS or Linux is preferable for this practical if available.

1. Download the Windows Miniforge installer from:

https://github.com/conda-forge/miniforge/releases

Choose:

```text
Miniforge3-Windows-x86_64.exe
```

2. Run the installer normally.

3. After installation, open:

**Start Menu → Miniforge Prompt**

4. In the Miniforge Prompt run:

```bat
conda --version
mamba --version
```

If both commands print version numbers, the installation is complete.

---

### If Conda is already installed

You can first check your existing installation:

```bash
conda --version
```

A recent Conda installation is usually fine.

If Conda is very old or takes a very long time to solve environments, install **Miniforge** using the instructions above and use that instead.

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
