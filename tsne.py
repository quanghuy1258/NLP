import json, codecs
import numpy as np
from sklearn.manifold import TSNE

with codecs.open("data.json", "r", "utf-8-sig") as fp:
    data = json.load(fp)

words = data.keys()
wordXY = np.array(data.values())
wordXY = TSNE().fit_transform(wordXY)

d = {}
for i in xrange(len(words)):
    d[words[i]] = wordXY[i].tolist()

with codecs.open("new_data.json", "w", "utf-8-sig") as fp:
    json.dump(d, fp, ensure_ascii=False)
