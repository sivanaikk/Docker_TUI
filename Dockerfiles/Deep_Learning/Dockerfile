FROM ubuntu:18.04
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    build-essential \
    g++ \
    git \
    apache2 \
    openssh-client \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-virtualenv \
    python3-wheel \
    pkg-config \
    libopenblas-base \
    python3-numpy \
    python3-scipy \
    python3-h5py \
    python3-yaml \
    python3-pydot \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install  numpy

RUN pip3 --no-cache-dir install \
    pandas \
    scikit-learn \
    statsmodels \
    matplotlib \
    Pillow \
    papermill \
    jupyter \
    tensorflow==1.12.0 \
    tensorflow-probability==0.5.0 \
    keras==2.2.4 \
    jupyter notebook 

RUN mkdir -p /root/workspace

EXPOSE 80
CMD ["python3","/root/workspace/model.py"]
