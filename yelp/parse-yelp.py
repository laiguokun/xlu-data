import csv
input_file = './train.csv'
fin = open(input_file)
positive = []
negative = []
with open(input_file) as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        score, review = line
        review = review.replace('\n', ' ').replace('\r', ' ')
        if (score == '2'):
            positive.append(review)
        else:
            negative.append(review)
fin = open('./train_index.txt')
train_p_index = []
train_n_index = []
for line in fin:
    tokens = line.strip().split('\t')
    if (tokens[0] == '1'):
        train_p_index.append(int(tokens[1]))
    else:
        train_n_index.append(int(tokens[1]))
        
output_file = './train.tsv'
unlabeled_file = './unlabeled.tsv'
fout = open(output_file, 'w')
unlabeled_fout = open(unlabeled_file, 'w')
for i in range(len(positive)):
    if i in train_p_index:
        fout.write('1\t{}\n'.format(positive[i]))
    else:
        unlabeled_fout.write('1\t{}\n'.format(positive[i]))
for i in range(len(negative)):
    if i in train_n_index:
        fout.write('0\t{}\n'.format(negative[i]))
    else:
        unlabeled_fout.write('0\t{}\n'.format(negative[i]))
fout.flush()
fout.close()
unlabeled_fout.flush()
unlabeled_fout.flush()