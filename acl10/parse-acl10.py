#!/usr/bin/python

import sys
import os
import gzip
from xml.etree.cElementTree import iterparse,tostring
import traceback

def parse(itemfile):
    itemc = 0
    ratings_list = []
    print(itemfile)
    try:
        for event, elem in iterparse(itemfile):
            if elem.tag == "item":
                try:
                    rating = processItem(elem)
                    ratings_list.append(rating)
                    itemc += 1
                except Exception as e:
                    print(e)
                    input()
                elem.clear()
    except Exception as e:
        print(e)
        input()
    return ratings_list


def processItem(item):
    """ Process a review.
    Implement custom code here. Use 'item.find('tagname').text' to access the properties of a review.
    """
    rating = float(item.find("rating").text)
    text = item.find("text").text
    return (rating, text)


def write_file(L, file):
    fout = open(file, 'w')
    for item in L:
        rating, text = item
        assert (rating != 3)
        if (text is None):
            continue
        text = text.replace('\n', ' ').replace('\r','').replace('\t',' ')
        if (rating < 3):
            fout.write('0\t' + text + '\n')
        else:
            fout.write('1\t' + text + '\n')
    fout.flush()
    fout.close()

def main():
    root = './acl10'

    # integrate data from different cate
    language = ['en', 'de', 'fr', 'jp']
    category = ['dvd', 'books', 'music']
    for la in language:
        train_list = []
        test_list = []
        unlabeled_list = []
        for cate in category:
            path = os.path.join(root, la)
            path = os.path.join(path, cate)
            train_path = os.path.join(path, 'train.review')
            test_path = os.path.join(path, 'test.review')
            unlabeled_path = os.path.join(path, 'unlabeled.review')
            train_list += parse(train_path)
            test_list += parse(test_path)
            unlabeled_list += parse(unlabeled_path)

        write_file(train_list, la + '_train.tsv')
        write_file(test_list, la + '_test.tsv')
        write_file(unlabeled_list, la + '_unlabled.tsv')

    # create the english training data subset
    data_list = []
    idx_list = []
    fin = open('index_list.txt')
    for line in fin:
        idx_list.append(int(line.strip()))

    fin = open('en_train.tsv')
    for line in fin:
        data_list.append(line)

    fout = open('en_train.1000.tsv', 'w')
    for idx in idx_list:
        fout.write(data_list[idx])
    fout.flush()
    fout.close()

if __name__ == "__main__":
    main()
