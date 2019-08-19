import json

import xml.etree.ElementTree
positive = []
negative = []
unlabeled = []
fin = open('./convert-amazon.txt')
cnt = 0
for line in fin:
    tokens = line.strip().split('\t')
    if (len(tokens) !=2 ):
        continue
    inp = '<root>' + tokens[1] + '</root>'
    data = xml.etree.ElementTree.fromstring(inp)
    review = data.find('content')
    if (review is None):
        continue
    review = review.text.replace('\n', ' ').replace('\r', ' ')
    if (len(review) == 0):
        continue
    c = data.find('category')
    if (c is None):
        continue
    c = c.text.split(']')[0]
    if (c != '[621'):
        unlabeled.append(review)
        continue
    rate = data.find('score')
    if (rate is None):
        continue
    rate = int(rate.text)
    if (rate > 3):
        positive.append(review)
    elif (rate <3 and rate != -1):
        negative.append(review)
    else:
        unlabeled.append(review)

fin = open('./train_index.txt')
train_p_index = []
train_n_index = []
for line in fin:
    tokens = line.strip().split('\t')
    if (tokens[0] == '1'):
        train_p_index.append(int(tokens[1]))
    else:
        train_n_index.append(int(tokens[1]))
fin = open('./test_index.txt')
test_p_index = []
test_n_index = []
for line in fin:
    tokens = line.strip().split('\t')
    if (tokens[0] == '1'):
        test_p_index.append(int(tokens[1]))
    else:
        test_n_index.append(int(tokens[1]))

        
output_file = './train.tsv'
test_file = './test.tsv'
unlabeled_file = './unlabeled.tsv'
fout = open(output_file, 'w')
test_fout = open(test_file, 'w')
unlabeled_fout = open(unlabeled_file, 'w')
for i in range(len(train_p_index)):
    fout.write('1\t{}\n'.format(positive[train_p_index[i]]))
    fout.write('0\t{}\n'.format(negative[train_n_index[i]]))
    
for i in range(len(test_p_index)):
    test_fout.write('1\t{}\n'.format(positive[test_p_index[i]]))
for i in range(len(test_n_index)):
    test_fout.write('0\t{}\n'.format(negative[test_n_index[i]]))

for i in range(len(positive)):
    if not(i in train_p_index or i in test_p_index):
        unlabeled_fout.write('1\t{}\n'.format(positive[i]))
for i in range(len(negative)):
    if not(i in train_n_index or i in test_n_index):
        unlabeled_fout.write('0\t{}\n'.format(negative[i]))
for i in range(len(unlabeled)):
    unlabeled_fout.write('-1\t{}\n'.format(unlabeled[i]))

fout.flush()
fout.close()
test_fout.flush()
test_fout.close()
unlabeled_fout.flush()
unlabeled_fout.flush()