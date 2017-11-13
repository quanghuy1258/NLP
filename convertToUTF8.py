import codecs

#Popular encodings
encodings = ['ascii','utf-8','utf-16']

def convertToUTF8(filename,encodings):
    f = open(filename,'r')
    data = f.read()
    f.close()
    for e in encodings:
        try:
            conv = codecs.decode(data,e)
            f = open(filename,'w')
            f.write(codecs.encode(conv,'UTF-8'))
            f.close()
        except:
            pass
