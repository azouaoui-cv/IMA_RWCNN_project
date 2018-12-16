# A Powerful Generative Model Using Random Weights for the Deep Image Representation
 
* [arxiv](https://arxiv.org/abs/1606.04801)
* *No available implementation*


## TLDR

Generate textures and use style transfer by leveraging a random weights VGG architecture. This paper suggests that the contribution of training can be separated from the contribution of the network structure and that untrained, random weight deep neural networks can indeed be used to do deep visualization. 


## Aim

> objectives, contributions
* Contribution: This paper suggests that the failed attempt by Gatys et al.'s to synthetize textures using the VGG architecture with random weights **may be due to their inappropriate scale of the weighting factors**.

## Methods

* Apply weighting factors determined by a pre-process to normalize the different impact scales of different activation layers on the input layer.
* Greedy approach to build a *stacked* random weight network using the *inversion technique* to stabilize the visualization quality.
  * Select one single image as the reference image and start from the first convolutional layer.
  * Sample, select and fix the weights of each layer in forward order:
    * For current layer $$l$$, fix the weights of the previous $$l - 1$$ layers and sample several sets of random weights connecting the $$l^{th}$$ layer.
    * Then reconstruct the target image using the rectified representation of layer $$l$$, and choose weights yielding the smallest loss.

## Technical details

> mathematical notations, proofs

* **Deep representations inversion**

> setups

* Inversion criterion/loss: euclidean distance

> parameterizing

## Experiments - results

> comparable experiments on typical dataset/environments...

> breakthroughs

* Inversion results at least as good as a pre-trained VGG.

*  Achieves a better inversion euclidean distance much quicker than pre-trained weights.

## My thoughts and takeaways

> pros
* No more training, yeah!

> cons
* Need to resample a *ranVGG* for each image.
* Code used is not available.


> related stuff
* If the network architecture is what matters, how can we explain that *VGG*-like architectures beat every other architecture? Could ResNet with its skip connections be used?

* Similar GitHub implementations:
  * [random-texture-synthesis](https://github.com/ivust/random-texture-synthesis)
  * [subjective-functions](https://github.com/wxs/subjective-functions)

## Top Figures

* Figure 5 shows the convergence speed and reconstruction quality. 

## Metadata
```
@inproceedings{He2016APG,
  title={A Powerful Generative Model Using Random Weights for the Deep Image Representation},
  author={Kun He and Yan Wang and John E. Hopcroft},
  booktitle={NIPS},
  year={2016}
}
```
