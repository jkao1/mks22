import urllib

def each_one(link):
    url='http://codingbat.com'+link
    s=urllib.urlopen(url).read()
    text = s[s.find('minh')+5:s.find('</div>',s.find('minh'))]
    focus = s[s.find('minh')+5:s.find('<p>',s.find('minh'))]
    focus= focus.split('<br>')[1:]
    params = []
    for pot in focus:
        so_far=[pot[pot.find('('):pot.find(')')+1]]
        result = pot.rfind(';')+2
        so_far.append(pot[result:])
        params.append(so_far)
    title = s[s.rfind('h2')+3:s.find('<',s.rfind('h2'))]
    return [text,params,title]

def Main(start_on,category):
    url='http://codingbat.com/python/'+category
    s=urllib.urlopen(url).read()
    s=s.split('<a href=')[12:-5]
    M={}
    start = start_on
    for lol in s:
        link=lol[1:lol.find('>')-1]
        params=each_one(link)
        M[start]={'try':params[1],'text':params[0],'title':params[2]}
        start +=1
    return M
    
