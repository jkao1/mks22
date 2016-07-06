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
        
    score_titles = ['SAT Composite Rangesupf', 'ACT Composite Rangesupf','Percent Admittedsupe']
    for title in score_titles:
        if title[-4:-1] == 'sup':
            start = s.find('<li>'+title[:-4]+'<sup>'+title[-1]+'</sup>: <b>')
        else:
            start = s.find('<li>'+title+': <b>')
        end = s.find('</b>', start)
        score_container = s[start:end]
        score = score_container[score_container.find('<b>')+3:]
        print score

def Main():
    while True:
        d = raw_input('college: ')
        getSAT_ACT(d)

Main()
