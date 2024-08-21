"""HPCCM Recipe for GAlibrate with Julia backend acceleration.

GAlibrate source:
https://github.com/blakeaw/GAlibrate

Usage:
$ hpccm.py --recipe hpccm_recipe.py --format docker
# hpccm.py --recipe hpccm_recipe --format singularity
"""

# Choose a base image - Ubuntu
Stage0 += baseimage(image="ubuntu:16.04")  # primitive

# Install Conda with dependencies.
Stage0 += conda(
    eula=True, packages=["python=3.10.11", "pip", "numpy=1.23.5", "scipy"]
)  # building block


# Install GAlibrate version 0.7.2 with Julia integration
# and PyJulia (julia on PyPI)
Stage0 += shell(
    commands=[
        ". ~/.bashrc", # Explicitly activate the bashrc
        "conda activate base", # Activate the conda environment
        "pip --no-cache-dir install https://github.com/blakeaw/GAlibrate/archive/refs/tags/v0.7.2.zip", # Install GAlibrate
        "pip --no-cache-dir install julia==0.6.1", # Install PyJulia
    ]
)  # primitive

# Install Julia programming environment - PyJulia needs
# the PyCall.jl package, so we install that here.
Stage0 += julia(version="1.9.2", packages=["PyCall"])  # building block


