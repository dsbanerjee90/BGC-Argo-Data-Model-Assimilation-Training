#!/usr/bin/env python3
"""
Pre-class environment check.

Author: Deep S. Banerjee
Plymouth Marine Laboratory (PML)
Funded by the European Space Agency (ESA).
"""

import importlib
import sys

REQUIRED_MODULES = [
    "numpy",
    "pandas",
    "xarray",
    "matplotlib",
    "netCDF4",
    "sklearn",
    "IPython",
    "ipywidgets",
]

failed = False

print("Checking Python packages...")

for module in REQUIRED_MODULES:
    try:
        imported = importlib.import_module(module)
        version = getattr(imported, "__version__", "")
        suffix = f" ({version})" if version else ""
        print(f"  OK  {module}{suffix}")
    except Exception as exc:
        failed = True
        print(f"  FAIL {module}: {exc}")

print()
print(f"Python: {sys.version.split()[0]}")
print(f"Executable: {sys.executable}")
print()

if failed:
    print("COURSE SETUP CHECK: FAILED")
    print("Activate the ecosystem-training environment and recreate it from environment.yml if needed.")
    sys.exit(1)

print("COURSE SETUP CHECK: PASSED")
