#*CHANGES IN MAIN.PY HAVE A *
#*
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
        title = title.replace('-',' ')
        dic = {}
        ls = []
        for item in product: # loops all <td>'s from the <tr>
            angle = item.rfind('>')
            new = item[angle+1:]
            ls.append(float(new))
        for i in range(6):
            dic[th[i]] = ls[i]
        M[title] = dic        

    table = "<table border=1>"
    table += "\n\t<tr><th>Product Name</th><th>"+info.upper()+"</th></tr>"
    for key in M:
        table += '\n\t<tr>'+'<td>'+key+'</td>'+'<td>'+str(M[key][info])+'</td>'+'</tr>'
    table += "\n</table>"
    return table        

#*form = cgi.FieldStorage()

def html(product_type, item, info): #* html():
    #*product_type = form.getvalue('product_type')
    #*item = form.getvalue('item')
    #*info = form.getvalue('info')
    table = store(product_type, item, info)
    print table

def Main(product_type, item, info): #* Main():
    print content_type
    print html_top
    html(product_type, item, info)
    #*html()
    print html_btm

#*Main()
#example:

def get2():
    url_frappe = 'http://www.starbucks.com/menu/drinks/frappuccino-blended-beverages/caffe-vanilla-frappuccino-light-blended-beverage'
    f = urllib.urlopen(url_frappe)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end]

def store2():
    main = get2()
    main = main.split('</tr>')[1:11] # rest info is useless
    for elem in main: # gathering info
        if '<strong>' in elem:
            i = main.index(elem)
            elem = elem.replace('\r','').replace('\n','').replace('\t','')
            main[i] = elem
            print elem
        else:
            main.remove(elem)
    return main
    M = {}
    for i in range(len(main)):
        elem = main[i]
        t_end = elem.rfind(' ')
        title = elem[:t_end]
        num = elem[t_end+1:]
        M[title] = num
 #   M['fat'] = M['Total Fat']
#    M['carbs'] = M['Total Carbohydrate']
#    del M['Total Fat']
#    del M['Total Carbohydrate']
    return M
# 0 2 5 6 7 10
