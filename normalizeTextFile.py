import codecs
import unicodedata

#popular encodings
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
