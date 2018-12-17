# IMA_RWCNN_project
Project on the [texture synthesis using random filters in a CNN](https://arxiv.org/abs/1606.04801) paper in the digital imaging course (MVA 2018-2019).

**WORK IN PROGRESS**

Our goal is to reproduce the method from the [texture synthesis using random filters in a CNN](https://arxiv.org/abs/1606.04801) paper using the [code](https://github.com/leongatys/DeepTextures) from Gatys as described in the paper "Texture Synthesis Using Convolutional Neural Networks" (Gatys et al., NIPS 2015) [http://arxiv.org/abs/1505.07376](http://arxiv.org/abs/1505.07376).

## Contents

* [reviews](./reviews)
* [models](./models)

## Requirements

This repository is developed on Linux 64-bit in Python 3.7 using [(Mini)conda](https://conda.io/miniconda.html).

To instanciate the conda environment, run ``conda create --file conda-env.txt --name ima``.

Then use pip to install the required Python packages: ``pip -r requirements.txt``.

To work on Jupyter notebook or Jupyter lab you will need to install it via pip. Follow the instructions [here](https://anbasile.github.io/programming/2017/06/25/jupyter-venv/) to make the environment kernel available in your jupyter installation.
