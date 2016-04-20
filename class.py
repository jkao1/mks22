"""

notes:

- print(%05d % 3) will print 4 0's before 3 

"""

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
    
def maxlist(ls):
    maxx = ls[0]
    for elem in ls:
        if elem > maxx:
            maxx = elem
    return maxx

def committee():
    cmt = []
    while True:
        alt = raw_input('Do something (type remove before a member\'s name to remove the member, type done to exit): ')
        if alt == 'done':
            break
        elif len(alt.split()) == 2:
            cmt.remove(alt.split()[1])
            print(alt.split()[1] + ' has been removed.')
        elif alt in cmt:
            print(alt + ' is already a committee member.')
        else:
            cmt.append(alt)
            print(alt ' has been added to the commitee.') 
    return alt





