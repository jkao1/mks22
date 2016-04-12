def maxfile(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    s = s.split('\n')[:-1]
    maxx = 0
    for elem in s:
        maxx = max(int(elem[elem.find(',')+1:]),maxx)
    for elem in s:
        if str(maxx) in elem:
            print(elem[:-3])
            break
    
