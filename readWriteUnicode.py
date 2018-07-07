from nltk.tokenize import word_tokenize
import codecs

iname = "text"
oname = "text_1"

ifile = codecs.open(iname, "r", "utf-8-sig")
ofile = codecs.open(oname, "w", "utf-8-sig")

while 1:
    line = ifile.readline()
    if not line:
        break
    ofile.write(" ".join(word_tokenize(line))+"\n")

ifile.close()
ofile.close()
