# Bridging the domain gap in cross-lingual document classification 

This repository contains the preprocessing scripts, augmentation data and pretrained models for our paper

[Bridging the domain gap in cross-lingual document classification](http://arxiv.org/abs/1909.07009)

Guokun Lai, Barlas Oguz, Veselin Stoyanov

## Data Preprocessing

We include the data preprocessing scripts and download links for the cross-lingual sentiment classification task in the corresponding folder.

As for the news classification task, we directly use the MLDoc dataset, which can be obtained from [https://github.com/facebookresearch/MLDoc](https://github.com/facebookresearch/MLDoc).

After preprocessing, there are different tsv files. Each line is a data sample, and the format is "$label \t $text". For the unlabeled data file, we put a placeholder in the $label field.

## Augmentation Data

We also provide our generated augmentation data in the [google drive](https://drive.google.com/open?id=13Z9v9n4r7ieVT3wD41dhyQkOJyU7atcB). In each folder, the augmentation file is the augmentation samples generated based on the corresponding unlabeled data. 

The data format for each line is "$label \t $original \t $augmented \t $original-lang \t $augmented-lang". The $original-lang field denote the language of the original sample. 

However, the texts of these files are processed by the BPE tokenization based on the scripts from XLM repo. If you want to obtain the original text, a simple approach is removing the BPE tokenization by deleting "@@ " symbols.

## Pretrained XLM Models

The pretrained-models used in this project are also in the [google drive](https://drive.google.com/open?id=1Sc7ffqWDSQEc66FMT24We7jkpp6ysn5l). We provide the pretrained XLM models based on the unlabeled data from different domains. The XLM models are based on XNLI15 version XLM and have the same storage format. 
