#1
def wc(filename):
    output = []
    f = open(filename, 'rU')
    s = f.read()
    f.close()
    # number of characters
    output.append(len(s.replace('\n','k')))
    # number of words
    output.append(len(s.replace('\n',' ').split()))
    # number of lines
    output.append(len(s.split('\n'))-1)
    
    return output

#2
def igpay(infile,outfile):
    f = open(infile,'rU')
    s = f.read()
    f.close()
    s.replace('\n',' ')
    inp = s.split()
    out = []
    for word in inp:
        if word[0] in 'aeiou':
            if word[-1] in ',.':
                out.append(word[:-1] + 'way' + word[-1])
            else:
                out.append(word + 'way')
        else:
            if word[-1] in ',.':
                out.append(word[1:-1] + word[0] + 'ay' + word[-1])
            else:
                out.append(word[1:] + word[0] + 'ay')                     
    out = ' '.join(out)           
    f = open(outfile,'w')
    f.write(out)
    f.close()
    
igpay('harry.txt','arryhay.txt')

#3
def HighLow(filename):
    s = open(filename,'rU').read().split()
    s = sorted(s,key=lambda name: name[-2:])
    print('highest:',s[-2][:-3],'with',s[-2][-2:])
    print('lowest:',s[0][:-3],'with',s[0][-2:])

#4
def Rank(infile,outfile):
    s = open(infile,'rU').read().split()
    s = sorted(s,key=lambda name: name[-2:])
    i = len(s)-1
    f = open(outfile,'w')
    while i >= 0:
        f.write(s[i]+'\n')
        i-=1
    f.close()

#5
def CharRank(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close
