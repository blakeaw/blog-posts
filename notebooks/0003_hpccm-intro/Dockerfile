FROM ubuntu:16.04

# Anaconda
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        wget && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp http://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh && \
    bash /var/tmp/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh -b -p /usr/local/anaconda && \
    /usr/local/anaconda/bin/conda init && \
    ln -s /usr/local/anaconda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    . /usr/local/anaconda/etc/profile.d/conda.sh && \
    conda activate base && \
    conda install -y numpy=1.23.5 pip python=3.10.11 scipy && \
    /usr/local/anaconda/bin/conda clean -afy && \
    rm -rf /var/tmp/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh

RUN . ~/.bashrc && \
    conda activate base && \
    pip --no-cache-dir install https://github.com/blakeaw/GAlibrate/archive/refs/tags/v0.7.2.zip && \
    pip --no-cache-dir install julia==0.6.1

# Julia version 1.9.2
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        tar \
        wget && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.2-linux-x86_64.tar.gz && \
    mkdir -p /var/tmp && tar -x -f /var/tmp/julia-1.9.2-linux-x86_64.tar.gz -C /var/tmp -z && \
    cp -a /var/tmp/julia-1.9.2 /usr/local/julia && \
    JULIA_DEPOT_PATH=/usr/local/julia/share/julia /usr/local/julia/bin/julia -e 'using Pkg; Pkg.add([PackageSpec(name="PyCall")])' && \
    rm -rf /var/tmp/julia-1.9.2-linux-x86_64.tar.gz /var/tmp/julia-1.9.2
ENV LD_LIBRARY_PATH=/usr/local/julia/lib:$LD_LIBRARY_PATH \
    PATH=/usr/local/julia/bin:$PATH


