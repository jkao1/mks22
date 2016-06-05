import urllib
th = ['calories', 'fat', 'carbs', 'fiber', 'protein', 'sodium'] 

units = {
    'fat': 'g',
    'carbs': 'g',
    'fiber': 'g',
    'protein': 'g',
    'sodium': 'mg',
}

def capitalize(s):
    words = s.split(' ')
    output = ''
    for word in words:
        output += word.capitalize() + ' '
    return output[:-1]

def get_num(s):
    num_end = s.rfind('</td>')
    num_start = s.find('<td>', num_end-7)+4
    try:
        return int(s[num_start:num_end])
    except:
        return '-'
    
def sb_get_spec(product,item):
    url_product = 'http://www.starbucks.com/menu/drinks/'+product+'/'+item
    f = urllib.urlopen(url_product)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end]

def sb_store_spec(product,item):
    main = sb_get_spec(product,item)
    main = main.split('</tr>')[:11]
    M = {}
    for i in range(len(main)): # gathering info
        elem = main[i]
        if '<strong>' in elem:
            elem = elem.replace('\r','').replace('\n','').replace('\t','')
            t_start = elem.find('<strong>') + 8 # title start
            t_end = elem.find('</strong>') # title end
            title = elem[t_start:t_end].lower()
            num_end = elem.find('</td>',t_end)
            num = elem[t_end+10:num_end]
            if title == 'total fat':
                title = 'fat'
            elif title == 'total carbohydrate':
                title = 'carbs'
        elif 'Dietary Fiber' in elem:
            title = 'fiber'
            num_start = elem.find('Fiber') + 6
            num_end = elem.find('</td>', num_start)
            num = elem[num_start:num_end]
        else:
            continue
        num = num.replace('g','').replace('m','')
        if title in th: #th is the title list
            M[title] = num
    return M

def sb_spec_main(product,info,sort):
    url = 'http://www.starbucks.com/menu/drinks/'+product
    f = urllib.urlopen(url)
    s = f.read()

    if 'frappuccino' in product:
        ol_start = s.find('<ol', s.find('<h3>Drinks</h3>'))
    elif 'sodas' == product:
        ol_start = s.find('<ol', s.find('<p>At participating stores.</p>'))
    ol_end = s.find('</ol>', ol_start)
    ol = s[ol_start:ol_end]
    ol = ol.split('<li>')[1:]
    
    M = {}
    for i in range(len(ol)):
        elem = ol[i]
        t_start = elem.find(product)+len(product)+1
        t_end = elem.find('"',t_start)
        title = elem[t_start:t_end]
        M[title.replace('-',' ')] = sb_store_spec(product,title)
    table = '<table border=1>'
    table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+"</th></tr>"
    td_toSort = []
    for key in M:
        td_toSort.append('\n\t<tr>'+'<td>'+capitalize(key)+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>')
    td_Sorted = sorted(td_toSort, key=lambda td: get_num(td) * int(sort))
    for td in td_Sorted:
        table += td
    table += "\n</table>"
    return M

print sb_spec_main('frappuccino-blended-beverages','carbs','-1')
