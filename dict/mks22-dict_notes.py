def t():
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
    
def f(opt):
    f = open('p8.csv', 'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:]
    for elem in L:
        L[L.index(elem)] = elem.split(',')
    output = []
    for bro in L:
        if 'MA' == bro[1][:2] or 'MA' == bro[0][:2]:
            output.append(bro[1]+' '+bro[0] + ' has a rating of ' + bro[2])
    if opt == 'last':
        sorted(output, key=lambda output: output.split(' ')[1])
    elif opt == 'first':
        output.sort()
    for hi in output:
        print(hi)

f()
