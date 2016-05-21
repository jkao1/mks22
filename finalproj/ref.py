#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"
html_top = """<html>
<head>
<title>Title</title>
</head>
<body>
"""
html_btm = "</body></html>"


def get(product_type,item):
    url_nutr = 'http://www.starbucks.com/menu/catalog/nutrition?'+product_type+'=' + item + '#view_control=nutrition'
    f = urllib.urlopen(url_nutr)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end]
 
th = ['calories', 'fat', 'carbs', 'fiber', 'protein', 'sodium']

def store(product_type,item,info):
    main = get(product_type,item) 
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
        dic = {}
        ls = []
        for item in product: # loops all <td>'s from the <tr>
            angle = item.rfind('>')
            ls.append(item[angle+1:])
        for i in range(6):
            dic[th[i]] = ls[i]
        M[title] = dic

    table = "<table border=1>"
    
    for key in M:
        table += '<tr>'+'<td>'+key+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>'
    return table        

form = cgi.FieldStorage()

def html():
    product_type = form.getvalue('product_type')
    item = form.getvalue('item')
    info = form.getvalue('info')
    table = store(product_type, item, info)
    print table

def Main():
    print content_type
    print html_top
    html()
    print html_btm

Main() 
