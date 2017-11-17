import codecs
from nltk.tokenize import sent_tokenize
import re

#list of delimiters
delim = []

#get the list of numeric and special characters
for i in range(65):
    delim.append(codecs.decode(chr(i),'utf-8'))
for i in range(91,97):
    delim.append(codecs.decode(chr(i),'utf-8'))
for i in range(123,127):
    delim.append(codecs.decode(chr(i),'utf-8'))
delim.append(codecs.decode('”','utf-8'))
delim.append(codecs.decode('“','utf-8'))
delim.append(codecs.decode('–','utf-8'))
delim.append(codecs.decode('…','utf-8'))
delim.append(codecs.decode('’','utf-8'))
delim.append(codecs.decode('•','utf-8'))

#split sentences
def splitSentences(s,delim):
    s = codecs.decode(s,'utf-8')
    #<br> tag in html = a new paragraph = a new sentence
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
