import os
import re
import codecs
from operator import itemgetter
#nhập danh sách các từ
wordSet = []
f = open('wordlist','r')
l = f.readline().decode('UTF-8').lower()
while l:
    wordSet.append(l[:-1])
    l = f.readline().decode('UTF-8').lower()
f.close()
f = open('newword','r')
l = f.readline().decode('UTF-8').lower()
while l:
    wordSet.append(l[:-1])
    l = f.readline().decode('UTF-8').lower()
f.close()
wordSet = list(set(wordSet))
wordSet.sort()
#xuất danh sách tổng hợp các từ
f = open('wordfinal','w')
for i in wordSet:
    f.write(i.encode('UTF-8') + '\n')
f.close()
#Xuất danh sách bảng chữ cái
alphabet = []
for i in wordSet:
    for j in i:
        alphabet.append(j)
for i in range(97,123):
    alphabet.append(chr(i))
alphabet = list(set(alphabet))
alphabet.sort()
f = open('alphabetfinal','w')
for i in alphabet:
    f.write(i.encode('UTF-8')+'\n')
f.close()
#bắt đầu thống kê 1 file
def check_a_word(word, alphabet):
    if re.search('\d', word):
        return word
    if word.find('=') != -1:
        return word
    if word.find('<') != -1:
        return word
    if word.find('>') != -1:
        return word
    if word == '':
        return word
    l = len(word)
    for x in range(0,l,1):
        if word[x] in alphabet:
            break
    for y in range(l,0,-1):
        if word[y-1] in alphabet:
            break
    if x<y:
        return word[x:y]
    else:
        return word

def stat_one_file(filedir, alphabet, distinctWords):
    f = open(filedir, 'r')
    l = f.readline().decode('UTF-8').lower()
    nWords = 0
    while l: 
        if l[:9] == 'Content: '.decode('UTF-8').lower():
            content = l[9:]
            wordList = content.split()
            for w in wordList:
                nWords += 1
                w = check_a_word(w, alphabet)
                if w in distinctWords:
                    distinctWords[w] += 1
                else:
                    distinctWords[w] = 1
        l = f.readline().decode('UTF-8').lower()
    f.close()
    return nWords

def sort_and_print(wordSet, alphabet, nWords, wordCount):
    arr = [ (x, c) for x, c in wordCount.items() ]
    arr = sorted(arr, key=itemgetter(1), reverse=True)
    x1 = 0
    f1 = open('inDict', 'w')
    f1.write(codecs.BOM_UTF8)
    x2 = 0
    f2 = open('notInDict', 'w')
    f2.write(codecs.BOM_UTF8)
    x3 = 0
    f3 = open('cannotRecognize', 'w')
    f3.write(codecs.BOM_UTF8)
    flag = 0
    for v in arr:
        if flag < 10:
            flag += 1
            print v[0].encode('UTF-8'), v[1]
        if v[0] in wordSet:
            f1.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
            x1 = x1 + v[1]
        else:
            if re.search('\d', v[0]):
                f3.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                x3 = x3 + v[1]
            elif v[0].find('=') != -1:
                f3.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                x3 = x3 + v[1]
            elif v[0].find('<') != -1:
                f3.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                x3 = x3 + v[1]
            elif v[0].find('>') != -1:
                f3.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                x3 = x3 + v[1]
            elif v[0] == '':
                f3.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                x3 = x3 + v[1]
            else:
                tst = 0
                for i in v[0]:
                    if i in alphabet:
                        tst = 1
                if tst == 1:
                    f2.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                    x2 = x2 + v[1]
                else:
                    f3.write(v[0].encode('UTF-8') + '\t' + str(v[1]) + '\n')
                    x3 = x3 + v[1]
    f1.close()
    f2.close()
    f3.close()
    f = open('nWords', 'w')
    f.write(codecs.BOM_UTF8)
    f.write(str(nWords)+'\n')
    f.write('inDict' + '\t' + str(x1)+'\n')
    f.write('notInDict' + '\t' + str(x2)+'\n')
    f.write('cannotRecognize' + '\t' + str(x3)+'\n')
    f.close()

folders = ['thanhnien', 'nld', 'dantri']
distinctWords = {} 
for fd in folders:
    for fn in os.listdir(fd):
        nWords = stat_one_file(fd+'/'+fn, alphabet, distinctWords)
        print 'Finished with %s' % fd+'/'+fn
sort_and_print(wordSet, alphabet, nWords, distinctWords)
