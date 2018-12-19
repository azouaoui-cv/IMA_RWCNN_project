# Title of papers

> [link](https://arxiv.org/pdf/1505.07376.pdf)

> [implementations](https://github.com/leongatys/DeepTextures)

## TLDR
This paper describes a method to generate a texture from a given source image. The method first extracts features from the source image with a CNN. It summarizes the extracted features in a gram matrix. It then tries to find an image that matches the summarized features by performing gradient descent on a white-noise image.
## Aim

The main contribution of this paper is the use of a CNN to define the texture model.

## Methods

The goal is to perform gradient descent from a white noise image to find another image that matches the Gram-matrix representation of the original image.

Let $(G^1 , .., G^L )$ be the Gram-matrix representation of the source image and $(\tilde{G}^1 , .., \tilde{G}^L )$ be the representation of the target image. The loss per layer $E^L$ is :
$$
E^L = \frac{1}{Cte_{norm}} \| G^L - \tilde{G}^L \|_2^2
$$
The total loss is :
$$
\mathcal{L} = \sum_l w_l E^l
$$
**!! IN THIS PAPER THE WEIGHTS $w_l \in {0, 1}$**
## Technical details

The optimization algorithm used is L-BFGS.
## Experiments - results

"We find that constraining all layers up to layer ‘pool4’ generates complex natural textures that are almost indistinguishable from the original texture"

The authors notice that taking all the parameters up to layer 'pool4' is not necessary. Same results can be obtained by just considering conv1_1 and pool1_4. The number of parameters can further be reduced by using PCA.

## My thoughts and takeaways

> PROS : Good results, extractions of a texture model from a CNN is simple and straight forward.

> CONS : Optimization can be slow. 

> related stuff


## Metadata

> bibtex: @article{gatys_texture_2015,
	title = {Texture {Synthesis} {Using} {Convolutional} {Neural} {Networks}},
	url = {http://arxiv.org/abs/1505.07376},
	abstract = {Here we introduce a new model of natural textures based on the feature spaces of convolutional neural networks optimised for object recognition. Samples from the model are of high perceptual quality demonstrating the generative power of neural networks trained in a purely discriminative fashion. Within the model, textures are represented by the correlations between feature maps in several layers of the network. We show that across layers the texture representations increasingly capture the statistical properties of natural images while making object information more and more explicit. The model provides a new tool to generate stimuli for neuroscience and might offer insights into the deep representations learned by convolutional neural networks.},
	urldate = {2018-12-19},
	journal = {arXiv:1505.07376 [cs, q-bio]},
	author = {Gatys, Leon A. and Ecker, Alexander S. and Bethge, Matthias},
	month = may,
	year = {2015},
	note = {arXiv: 1505.07376},
	keywords = {Computer Science - Computer Vision and Pattern Recognition, Computer Science - Neural and Evolutionary Computing, Quantitative Biology - Neurons and Cognition},
	annote = {Comment: Revision for NIPS 2015 Camera Ready. In line with reviewer's comments we now focus on the texture model and texture synthesis performance. We limit the relationship of our texture model to the ventral stream and its potential use for neuroscience to the discussion of the paper},
	file = {arXiv\:1505.07376 PDF:C\:\\Users\\leello\\Zotero\\storage\\FRZISKC7\\Gatys et al. - 2015 - Texture Synthesis Using Convolutional Neural Netwo.pdf:application/pdf;arXiv.org Snapshot:C\:\\Users\\leello\\Zotero\\storage\\C3EVK467\\1505.html:text/html}
}
