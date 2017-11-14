delim = []

#Get the list of numeric and special characters
for i in range(65):
    delim.append(chr(i))
for i in range(91,97):
    delim.append(chr(i))
for i in range(123,127):
    delim.append(chr(i))
delim.append(codecs.decode('”','utf-8'))
delim.append(codecs.decode('“','utf-8'))
delim.append(codecs.decode('–','utf-8'))

#Split unicode strings with multiple delimiters
def uSplit(uString,delim):
    uString = list(uString)
    for i in range(len(uString)):
        if uString[i] in delim:
            uString[i] = ' '
    uString = ''.join(uString)
    return uString.split()
