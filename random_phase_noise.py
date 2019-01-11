# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

i = np.complex(0,1)
def random_phase_noise(shape):
    gauss_noise = np.random.randn(shape[0], shape[1])
    uniform_random_phase = np.fft.fft2(gauss_noise)
    return uniform_random_phase

source_texture = imread("texture.jpg")

img_shape = source_texture.shape
noise = random_phase_noise(img_shape)

new_texture_fft = np.zeros(img_shape, dtype=complex)
for channel in range(img_shape[-1]):
    new_texture_fft[:, :, channel] = np.multiply((np.fft.fft2(source_texture[:, :, channel])), np.exp(-i*np.angle(noise)))

new_texture = np.zeros(img_shape, dtype=float)
for channel in range(img_shape[-1]):
    img_channel = np.real(np.fft.ifft2(new_texture_fft[:, :, channel]))
    new_texture[:,:, channel] = (img_channel - np.min(img_channel))/(np.max(img_channel) - np.min(img_channel))

f, ax = plt.subplots(1, 2)
ax[0].imshow(source_texture)
ax[1].imshow(new_texture)
plt.show()




