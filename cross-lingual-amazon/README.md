# Preprocessing Instruction

The dataset can be downloaded from [https://webis.de/data/webis-cls-10.html](https://webis.de/data/webis-cls-10.html), and decompress it in this folder.  In our experiment, we ignore the category information and integrate them into one training and test set for a language.  

The training set split is a little different in different experimental settings.

In amazonen-amazonde and amazonen-amazonfr experiments, we use all English training data, which contains 6000 data samples. 

In amazonen-amazoncn and amazonen-yelp experiments, we use a subset of the training data which contains 2000 data samples. 

To obtain the splits, run the following command. 

```
python parse-acl10.py
```

### Reference 

[Cross-Language Text Classification using Structural Correspondence Learning](https://webis.de/downloads/publications/papers/stein_2010k.pdf). Peter Prettenhofer and Benno Stein. In 48th Annual Meeting of the Association of Computational Linguistics (ACL 10), pages 1118-1127, July  2010. Association for Computational Linguistics.