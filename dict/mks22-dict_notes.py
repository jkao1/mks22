def thursday():
    f = open('file.txt', 'rU')
    s = f.read()
    f.close()
    L = s.split('\n')
    output = {}
    title = L[0].split(',')
    item = L[1]
    row = item.split(',')
    for thing in title:
        output[thing] = row[title.index(thing)]
    return output
    
def friday():
    f = open('p8.csv', 'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:]
    for elem in L:
        L[L.index(elem)] = elem.split(',')
    for bro in L:
        if 'MA' in bro[1] + bro[0]:
            print(bro[1]+' '+bro[0] + ' has a rating of ' + bro[2])

friday()
