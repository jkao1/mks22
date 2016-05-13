def ExtremeScores(which_column,how_many,is_top):    
    f=open('SAT-2010-small.csv')
    s=f.read()
    f.close()
    L=s.split('\n')[1:-1]
    return L
