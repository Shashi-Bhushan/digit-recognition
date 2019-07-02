#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Shashi Bhushan <sbhushan1@outlook.com>

# Standard scientific Python imports
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np


def show_digits(images, target, sample_size=10):
    random_index = np.random.choice(images.shape[0], sample_size)

    images_with_labels = list(zip(images[random_index], target[random_index]))

    img = plt.figure(1, figsize=(16, 20), dpi = 120)

    for index, (image, label) in enumerate(images_with_labels):
        plt.subplot(np.ceil(sample_size/6.0), 6, index + 1)
        plt.axis('off')
        plt.imshow(image.reshape(28, 28), cmap = plt.cm.gray_r, interpolation='nearest')
        plt.title("Digit {}".format(label))
    plt.show()