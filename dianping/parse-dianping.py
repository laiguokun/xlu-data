import json
positive = []
negative = []
unlabeled = []
fin = open('./reviews.txt')

for line in fin:
    tokens = line.strip().split('^')
    if (len(tokens) !=2 ):
        continue
    data = json.loads(tokens[1])
    review = data['content'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    if (len(review) == 0):
        continue
    rate = data['rate']
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
for i in range(len(positive)):
    if i in train_p_index:
        fout.write('1\t{}\n'.format(positive[i]))
    elif i in test_p_index:
        test_fout.write('1\t{}\n'.format(positive[i]))
    else:
        unlabeled_fout.write('1\t{}\n'.format(positive[i]))
for i in range(len(negative)):
    if i in train_n_index:
        fout.write('0\t{}\n'.format(negative[i]))
    elif i in test_n_index:
        test_fout.write('0\t{}\n'.format(negative[i]))
    else:
        unlabeled_fout.write('0\t{}\n'.format(negative[i]))
for i in range(len(unlabeled)):
    unlabeled_fout.write('-1\t{}\n'.format(unlabeled[i]))
fout.flush()
fout.close()
test_fout.flush()
test_fout.close()
unlabeled_fout.flush()
unlabeled_fout.flush()