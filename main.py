import codecs
import unicodedata
from nltk.tokenize import sent_tokenize
import re


import os
from operator import itemgetter




encodings = ['ascii','utf-8','utf-16']

def normalizeTextFile(filename,encodings):
    f = open(filename,'r')
    data = f.read()
    f.close()
    for e in encodings:
        try:
            conv = codecs.decode(data,e)
            f = open(filename,'w')
            conv = unicodedata.normalize('NFC',conv)
            f.write(codecs.encode(conv,'utf-8'))
            f.close()
            return
        except:
            pass

delim = []

for i in range(65):
    delim.append(codecs.decode(chr(i),'utf-8'))
for i in range(91,97):
    delim.append(codecs.decode(chr(i),'utf-8'))
for i in range(123,127):
    delim.append(codecs.decode(chr(i),'utf-8'))
delim.append(codecs.decode('”','utf-8'))
delim.append(codecs.decode('“','utf-8'))
delim.append(codecs.decode('–','utf-8'))

def splitSentences(s,delim):
    s = codecs.decode(s,'utf-8')
    s = re.sub(codecs.decode('<br>','utf-8'),codecs.decode('. ','utf-8'),s)
    sentences = sent_tokenize(s)
    for i in range(len(sentences)):
        sentences[i] = list(sentences[i])
        for j in range(len(sentences[i])):
            if sentences[i][j] in delim:
               sentences[i][j] = codecs.decode(' ','utf-8')
        sentences[i] = ''.join(sentences[i])
        sentences[i] = sentences[i].strip()
        sentences[i] = re.sub(codecs.decode(' +','utf-8'),codecs.decode(' ','utf-8'),sentences[i])
        sentences[i] = sentences[i].lower()
    return sentences

wordSet = []
f = open('wordfinal','r')
l = f.readline()
while l:
    tmp = codecs.decode(l,'utf-8')
    wordSet.append(tmp[:-1])
    l = f.readline()
f.close()

def stat_one_file(filename,distinctWords):
    normalizeTextFile(filename,encodings)
    f = open(filename, 'r')
    l = f.readline()
    nWords = 0
    while l: 
        if l[:9] == 'Content: ':
            sentences = splitSentences(l[9:],delim)
            for s in sentences:
                for w in s.split():
                    nWords += 1
                    if w in distinctWords:
                        distinctWords[w] += 1
                    else:
                        distinctWords[w] = 1
        l = f.readline()
    f.close()
    return nWords

def sort_and_print(wordSet,nWords,wordCount):
    arr = [ (x, c) for x, c in wordCount.items() ]
    arr = sorted(arr, key=itemgetter(1), reverse=True)
    x1 = 0
    f1 = open('inDict', 'w')
    x2 = 0
    f2 = open('notInDict', 'w')
    flag = 0
    for v in arr:
        if flag < 10:
            flag += 1
            print codecs.encode(v[0],'utf-8'), v[1]
        if v[0] in wordSet:
            f1.write(codecs.encode(v[0],'utf-8') + '\t' + str(v[1]) + '\n')
            x1 = x1 + v[1]
        else:
            f2.write(codecs.encode(v[0],'utf-8') + '\t' + str(v[1]) + '\n')
            x2 = x2 + v[1]
    f1.close()
    f2.close()
    f = open('nWords', 'w')
    f.write('Total' + '\t' + str(nWords)+'\n')
    f.write('inDict' + '\t' + str(x1)+'\n')
    f.write('notInDict' + '\t' + str(x2)+'\n')
    f.close()

folders = ['t']
distinctWords = {} 
nWords = 0
for fd in folders:
    for fn in os.listdir(fd):
        print 'Beginning with %s' % fd+'/'+fn
        nWords += stat_one_file(fd+'/'+fn,distinctWords)
        print 'Finished with %s' % fd+'/'+fn
sort_and_print(wordSet,nWords,distinctWords)
