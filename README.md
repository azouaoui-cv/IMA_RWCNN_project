# IMA_RWCNN_project
Project on the [texture synthesis using random filters in a CNN](https://arxiv.org/abs/1606.04801) paper in the digital imaging course (MVA 2018-2019).

**WORK IN PROGRESS**

Our goal is to reproduce the method from the [texture synthesis using random filters in a CNN](https://arxiv.org/abs/1606.04801) paper using the [code](https://github.com/leongatys/DeepTextures) from Gatys as described in the paper "Texture Synthesis Using Convolutional Neural Networks" (Gatys et al., NIPS 2015) [http://arxiv.org/abs/1505.07376](http://arxiv.org/abs/1505.07376).

## Contents

* [reviews](./reviews)
* Final_Notebook.ipynb contains the code used to produce the report results. It is a notebook meant to be run in Google Colaboratory, hence it might need a few tweaks to run properly on a local instance.

## Requirements

This repository is developed on Linux 64-bit in Python 3.7 using [(Mini)conda](https://conda.io/miniconda.html).

To instanciate the conda environment, run ``conda create --file conda-env.txt --name ima``.

Then use pip to install the required Python packages: ``pip -r requirements.txt``.

To use the virtual environment: ``source activate ima``

To install a custom kernel in jupyter lab/notebook: ``ipython kernel install --user --name=ima``

To work on Jupyter notebook or Jupyter lab you will need to install it via pip. Follow the instructions [here](https://anbasile.github.io/programming/2017/06/25/jupyter-venv/) to make the environment kernel available in your jupyter installation.
## Old

### Docker instructions to run Gatys code

See detailed [issue](https://github.com/leongatys/DeepTextures/issues/7)

1. Install Docker: https://docs.docker.com/engine/installation/
2. ``sudo docker pull leongatys/caffe-cpu`` (download the image)
3. Download the code (``git clone https://github.com/leongatys/DeepTextures.git``)
4. Download the fully trained VGG network: http://bethgelab.org/media/uploads/deeptextures/vgg_normalised.caffemodel
5. Start a notebook server in the docker container: ``sudo docker run -v $HOME:/home -p 8888:8888 -d leongatys/caffe-cpu jupyter-notebook``
6. Check the docker container IP: ``sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <docker_id>`` where ``docker_id`` is given at the end of the previous command or by ``sudo docker container ls -aq``
7. Go to the browser and type in the IP with port 8888 (``<output_IP>:8888``)
8. You can play with the existing notebook and/or create your own.
9. To stop the docker container: ``sudo docker container stop <container_hash>``
