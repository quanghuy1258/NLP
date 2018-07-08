from gensim.models import word2vec
from nltk import word_tokenize
import codecs, json
import numpy as np

iname = "text_1"
ifile = codecs.open(iname, "r", "utf-8-sig")

sens = []
while 1:
    line = ifile.readline()
    if not line:
        break
    sens.append(word_tokenize(line[:-1]))

model = word2vec.Word2Vec(sentences=sens)
words = model.wv.vocab.keys()

d = {}
for k in words:
    d[k] = model[k].tolist()
with codecs.open("data.json", "w", "utf-8-sig") as fp:
    json.dump(d, fp, ensure_ascii=False)

ifile.close()
