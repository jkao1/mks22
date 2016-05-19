import urllib.request

url = "http://www.starbucks.com/menu/drinks/espresso/"
end = "?foodZone=9999"

def f(drink):
    link = url + drink + end
    response = urllib.request.urlopen(link)
    html = response.read()
    html = html.decode(encoding='utf-8')
    t_start = html.rfind('class="nutrition"')
    t_end = html.find('</table>',t_start)
    raw = html[t_start:t_end].replace('\r','').replace('\n','').replace('\t','')
    
