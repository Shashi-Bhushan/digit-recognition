#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Shashi Bhushan <sbhushan1@outlook.com>

# Standard scientific Python imports
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as dt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
# fetch original mnist dataset
from sklearn.datasets import fetch_openml

from util import *


def main():
    # it creates openml folder in your root project folder
    mnist = fetch_openml('mnist_784', version=1, data_home='./')

    show_digits(mnist.data, mnist.target)


if __name__ == "__main__":
    main()
