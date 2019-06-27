#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import shutil

execution_path = os.getcwd()

DATASET_DIR = os.path.join(execution_path, "dataset")
TEST_DATASET = os.path.join(DATASET_DIR, "test.csv")
TRAIN_DATASET = os.path.join(DATASET_DIR, "train.csv")

TEST_DATASET_SOURCE_PATH = "https://drive.google.com/open?id=1wzkEAVDKT_K2EGapJ6QEd7wSwmjDdi3g"
TRAIN_DATASET_SOURCE_PATH = "https://drive.google.com/open?id=1gLDkGwac_sjbdsL8qzoyoOYAsy8oK1xC"

# ----------------- The Section Responsible for Downloading the Dataset ---------------------


def download_dataset(source_path, dataset_path):
    test_data = requests.get(source_path, stream=True)
    with open(dataset_path, "wb") as file:
        shutil.copyfileobj(test_data.raw, file)
    del test_data


def download_datasets():
    if not os.path.exists(DATASET_DIR):
        os.makedirs(DATASET_DIR, exist_ok=True)

    if not os.path.isfile(TEST_DATASET):
        download_dataset(TEST_DATASET_SOURCE_PATH, TEST_DATASET)

    if not os.path.isfile(TRAIN_DATASET):
        download_dataset(TRAIN_DATASET_SOURCE_PATH, TRAIN_DATASET)


if __name__ == "__main__":
    download_datasets()
