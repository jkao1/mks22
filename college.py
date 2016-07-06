import urllib

def getSAT_ACT(url):
    url = 'http://www.forbes.com/colleges/' +url
    f = urllib.urlopen(url)
    s = f.read()

    all_titles = [
        'Student Population',
        'Undergraduate Population',
        'Student to Faculty Ratiosupa',
        'Total Annual Costsupc',
        'In-State Tuitionsupc',
        'Out-Of_state Tuitionsupc',
        'Percent on Financial Aidsupd',
        'Average Grant Aid Received (FT/First-Time)',
        'Percent Admittedsupe',
        'SAT Composite Rangesupf',
        'ACT Composite Rangesupf'
        ]
        
    score_titles = ['SAT Composite Rangesupf', 'ACT Composite Rangef','Percent Admittede']
    for title in score_titles:
        if title[-4:-1] == 'sup':
            start = s.find('<li>'+title[:-1]+'<sup>'+title[-1]+'</sup>: <b>')
        else:
            start = s.find('<li>'+title+': <b>')
        end = s.find('</b>', start)
        score_container = s[start:end]
        score = score_container[score_container.find('<b>')+3:]
        print score
    
getSAT_ACT('colgate-university')

"""
Student Population: 2,900
Undergraduate Population: 2,890
Student to Faculty Ratioa: 9
Total Annual Costc: $62,405
In-State Tuitionc: $48,175
Out-of-State Tuitionc: $48,175
Percent on Financial Aidd: 41%
Average Grant Aid Received (FT/First-Time): $34,062
Percent Admittede: 26%
SAT Composite Rangef: 1270-1460
ACT Composite R
"""
