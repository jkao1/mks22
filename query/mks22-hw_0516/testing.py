def f(col,num,is_top):
    f=open('SAT-2010.csv','rU')
    s=f.read()
    f.close()

    s=s.split('\n')[1:-1] #remove header and ''
    for line in s:
        if line[-1] == 's':
            s.remove(line)
    print(s)

f(3,3,True)
