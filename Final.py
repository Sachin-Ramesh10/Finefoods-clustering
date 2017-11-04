import nltk
import re

print("Selecting review/text")

inFile = input("Enter the input File Name: ")

Lfile = open("Reviews.txt", 'a')
with open(inFile, 'r', encoding = "ISO-8859-1") as f:
    for line in f:
       if 'review/text:' in line:
           Lfile.write("%s" % line)

print("Tokenizing the Review/text")

words = []
with open('Reviews.txt', 'r') as ff:
    for line in ff:
        tokens = nltk.word_tokenize(line)
        for w in tokens:
            words.append(w.lower())

			
print("removing special characters")
wow = []
rx = "[^A-Za-z]+"
for word in words:
    data = re.sub(rx, '', word)
    wow.append(data)#

print("finding unique words")

L =[]
for w in wow:
    if w not in L:
        L.append(w)

with open('UniqueWords.txt', 'a', encoding='utf-8') as f:
    for i in L:
        f.write("%s\n"% i)

print("removing stopwords")

stopwords = []
with open('stopwords.txt', 'r') as f:
    for word in f.read().split():
        stopwords.append(word)

W1 = [word for word in L if word not in stopwords]
waste = ['reviewtext','br','nt','ve','ll','lb','wo']
W = [word for word in W1 if word not in waste]

wset = set(W)
freq = {}
j = 0
print("finding frequency of top 500")
for word in wow:
    if word in wset:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    j = j +1

Finalwords = []
d_view = [(v, k) for k, v in freq.items()]
d_view.sort(reverse=True)  # natively sort tuples by first element
for v, k in d_view[:500]:
    Finalwords.append(k)


if '' in Finalwords:
    Finalwords.remove('')


import csv
with open('Top500_Freq.csv', 'a', newline= '') as csv_file:
    writer = csv.writer(csv_file)
    for i in Finalwords:
       writer.writerow([i, freq[i]])


##########################################################################################################################

print("creating vector matrix")
import os
cwd = os.getcwd()
path = cwd+"\VectorMatrix.csv"
path = path.replace('\\','/')

import csv
from collections import OrderedDict

def doc(dict):
    file_exists = os.path.isfile(path)
    with open('VectorMatrix.csv', 'a', newline='') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, dict.keys())
        if not file_exists:
            w.writeheader()
        w.writerow(dict)

def send(got,l):
    inter = OrderedDict()
    inter["Review No"] = l
    for i in Finalwords:
        if i in got:
            inter[i] = got.count(i)
        else:
            inter[i] = 0

    doc(inter)
import nltk

with open('Reviews.txt', "r") as toks:
    count = 0
    for line in toks:
      words = nltk.word_tokenize(line)
      count = count + 1
      send(words,count)

#####################################################################################################################################################

from sklearn import cluster as c


import numpy as np
print("creating dataframe of vectors")
import pandas as pd
df = pd.read_csv('VectorMatrix.csv')
df = df.drop('Review No', 1)
print("dataframe created")
print("Starting Clustering")
kmeans = c.KMeans(n_clusters=10, random_state=0).fit(df)
print("clustering complete")

import csv
labels  = list(df.columns.values)

from collections import Counter


def topwords(num):
    cluster = {}
    wlist = []
    cvlist = []
    clist = kmeans.cluster_centers_[num].astype(np.float).tolist()
    for i in labels:
        cluster[i] = clist[labels.index(i)]
    top = Counter(cluster)
    for k,v in top.most_common(5):
        wlist.append(k)
        cvlist.append(v)

    return wlist,cvlist

print("Finding top 5 words from Each clusters")
for i in range(len(kmeans.cluster_centers_)):
        with open('TopClusterwords.txt', 'a', encoding='utf-8') as f:
            f.write("cluster" + str(i))
            w,c = topwords(i)
            f.write("\n%s"% w)
            f.write("\n%s\n\n"%c)
            #print("{} \n {} \n {}".format(w,c))