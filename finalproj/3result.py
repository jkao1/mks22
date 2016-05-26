#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"
html_top = """<html>
<head>
<title>Title</title>
<body>
"""
html_btm = "</body></html>"

css = """<style>
table {display:block;margin:0 auto}
</style></head>
"""

th = ['calories', 'fat', 'carbs', 'fiber', 'protein', 'sodium']

unit = {
    'calories': '',
    'fat': 'g',
    'carbs': 'g',
    'fiber': 'g',
    'protein': 'g',
    'sodium': 'mg',
}

##==========================##
##=====HELPER FUNCTIONS=====##
##==========================##

def capitalize(s):
    words = s.split(' ')
    output = ''
    for word in words:
        output += word.capitalize() + ' '
    return output[:-1]
    
##=================================##
##=====REGULAR FOOD/DRINK MENU=====##
##=================================##

def sb_get(product_type,item):
    url_nutr = 'http://www.starbucks.com/menu/catalog/nutrition?'+product_type+'=' + item + '#view_control=nutrition'
    f = urllib.urlopen(url_nutr)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end]

def sb_store(product_type,item,info):
    main = sb_get(product_type,item) 
    main = main.split('</tr>')[1:-1]
    M = {}
    for i in range(len(main)): # loops all <tr>'s of all products in main
        product = main[i]
        product = product.split('</td>')[:-1]
        cont = product[0] # container of title
        if i == 0:
            title = cont[cont.find('/',57)+1:cont.find('"',57)]
        else:
            title = cont[cont.find('/',42)+1:cont.find('"',42)]
        title = title.replace('-',' ')
        title = title.replace('?foodZone=9999','')
        if 'Starbucks ' == title[:10]:
            title = title.replace('Starbucks ','')
        else:
            title = title.replace(' Starbucks ','')
        dic = {}
        ls = []
        for item in product: # loops all <td>'s from the <tr>
            angle = item.rfind('>')
            ls.append(item[angle+1:])
        for i in range(6):
            dic[th[i]] = ls[i]
        M[title] = dic
    
    table = "<table border=1>"
    table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+'('+unit[info]+")</th></tr>"
    for key in M:
        table += '\n\t<tr>'+'<td>'+capitalize(key)+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>'
    table += "\n</table>"
    return table

##==========================##
##=====FRAPPUCCINO MENU=====##
##==========================##

def sb_get_frappe(item):
    url_frappe = 'http://www.starbucks.com/menu/drinks/frappuccino-blended-beverages/'+item
    f = urllib.urlopen(url_frappe)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end]

def sb_store_frappe(item):
    main = sb_get_frappe(item)
    main = main.split('</tr>')[:11] # rest info is useless
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
        num = num.replace('g','').replace('m','')
        if title in th: #th is the title list
            M[title] = num
    
    return M

form = cgi.FieldStorage()

def sb_frappe_main():
    url = 'http://www.starbucks.com/menu/drinks/frappuccino-blended-beverages'
    f = urllib.urlopen(url)
    s = f.read()
    ol_start = s.find('<ol', s.find('<h3>Drinks</h3>'))
    ol_end = s.find('</ol>', ol_start)
    #return s[ol_start:ol_end]
    
    ### NEXT FUNCTION ###
    ol = s[ol_start:ol_end]
    ol = ol.split('<li>')[1:]
    M = {}
    for i in range(len(ol)):
        elem = ol[i]
        t_start = elem.find('frappuccino-blended-beverages')+30
        t_end = elem.find('"',t_start)
        title = elem[t_start:t_end]
        M[title.replace('-',' ')] = sb_store_frappe(title)
        e_start = title.find(' blended') # redundant info
        if e_start != -1:          
            title = title[:e_start]
    
    info = 'calories'
    table = "<table border=1>"
    table += "\n\t<tr><th>Product Name</th><th>"+info.upper()+"</th></tr>"
    for key in M:
        table += '\n\t<tr>'+'<td>'+key+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>'
    table += "\n</table>"
    return table



def sb_html():
    product_type = form.getvalue('product_type')
    item = form.getvalue('item')
    info = form.getvalue('info')
    if item=='frappuccino':
        table = sb_frappe_main()
    else:
        table = sb_store(product_type, item, info)
    print table

def Main():
    print content_type
    print html_top
    print css
    if form.getvalue('Starbucks') == 'Submit':
        sb_html()
    print html_btm

Main() 
