#1 (solved)
def ReadSAT(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1] # empty space after last line break
    for elem in L:
        L[L.index(elem)] = elem.split(',')
    return L

print(ReadSAT('sat10-small.csv'))
print('\n')

#2 (solved)
def HighLowSAT(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1]
    for i in range(len(L)):
        if '"' in L[i]:
            quote = L[i].find('"') 
            target = L[i].find(',',quote) # finds the first comma after double quote
            noComma = L[i][:target] + L[i][target+1:]
            L[i] = noComma.split(',')
        else:
            L[i] = L[i].split(',')
    return L

print(HighLowSAT('sat10-small.csv'))              
print('\n')

#3 (solved)
def BigStats(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1]
    numStudents = 0
    totalRead = 0
    totalMath = 0
    totalWrite= 0
    for i in range(len(L)):
        if '"' in L[i]:
            quote = L[i].find('"') 
            target = L[i].find(',',quote) # finds the first comma after double quote
            noComma = L[i][:target] + L[i][target+1:]
            L[i] = noComma.split(',')
        else:
            L[i] = L[i].split(',')
        try:
            numStudents += int(L[i][2])
            totalRead += int(L[i][3])
            totalMath += int(L[i][4])
            totalWrite += int(L[i][5])
        except ValueError: #-->can't int() a string
            numStudents += 0
    print("Total students: " + str(numStudents))
    print("Avg reading score: " + str(totalRead / numStudents))
    print("Avg math score: " + str(totalMath / numStudents))
    print("Avg writing score: " + str(totalWrite / numStudents))

BigStats('sat10.csv')
print('\n')

#4 (in proogress)
def School2Dict(line):
    if '"' in line:
        quote = line.find('"') 
        target = line.find(',',quote)
        line = (line[:target] + line[target+1:]).replace('"','')
    line = line.split(',')
    cg = ['DBN','Name','Number','Reading','Math','Writing']
    output = {}
    for i in range(len(line)):
        output[cg[i]] = line[i]
    return output
        
#5 (solved)
def MakeMaster(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1]
    for i in range(len(L)):
        if '"' in L[i]:
            quote = L[i].find('"') 
            target = L[i].find(',',quote)
            noComma = L[i][:target] + L[i][target+1:]
            L[i] = noComma.split(',')
        else:
            L[i] = L[i].split(',')
    master = {}
    for i in range(len(L)):
        output = {}
        cg = ['hi','Name','Number','Reading','Math','Writing']
        for k in range(1,6):
            output[cg[k]] = L[i][k]
        master[L[i][0]] = output
    return master

print(MakeMaster('sat10-small.csv'))
print('\n')

#6 (solved)
def NameQuery(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    L = s.split('\n')[1:-1]
    for elem in L:
        L[L.index(elem)] = elem.split(',')
    while True:
        lookfor = input('Report on what name(s)? ')
        if lookfor == 'break':
            break
        for bro in L:
            if lookfor==bro[0][:len(lookfor)].lower() or lookfor==bro[1][:len(lookfor)].lower():
                print(bro[1]+' '+bro[0] + ' has a rating of ' + bro[2])

NameQuery('namelist.csv')
print('\n')

#6a (in progress)




    









    
