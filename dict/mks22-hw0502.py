def ReadSAT(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1] # empty space after last line break
    for elem in L:
        L[L.index(elem)] = elem.split(',')
    print(L)

def HighLowSAT(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1] # empty space after last line break
    for elem in L:
        if '"' in elem:
            elem = elem[:elem.find('"')] + elem[elem.find('"')+1:]
            target = elem.rfind(',', 0, elem.find('"'))
            elem = elem[:target] + elem[target+1:]
        L[L.index(elem)] = elem.split(',')
    print(L)
