
row = 0

def f():
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
    
