#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_btm = """
<a href="../index.html" style="display:block;border:1px solid #ffs63;border-radius 10px;text-decoration:underline;font-size:24px;font-family:Gill Sans;margin:0 auto;text-align:center;padding:12px 20px;">Home</a>
</body></html>
"""

form = cgi.FieldStorage()

th = ['calories', 'fat', 'carbs', 'fiber', 'protein', 'sodium'] 

units = {
    'calories': '',
    'fat': ' (g)',
    'carbs': ' (g)',
    'fiber': ' (g)',
    'protein': ' (g)',
    'sodium': ' (mg)',
}

##==========================##
##=====HELPER FUNCTIONS=====##
##==========================##

def capitalize(s):
    words = s.split(' ')
    output = ''
    for word in words:
        output += word.capitalize() + ' '
    if 'S Mores' in output:
        output = output.replace('S M',"S'm")
    return output[:-1]

def sb_get_num(s):
    num_end = s.rfind('</td>')
    num_start = s.find('<td>', num_end-7)+4
    try:
        return int(s[num_start:num_end])
    except:
        return '-'

def jm_get_num(s):
    num_start = s.rfind('<td>')+4
    num_end = s.rfind('</td>')
    try:
        return int(s[num_start:num_end])
    except:
        return '-'
        
def html_top():
    item = capitalize(form.getvalue('item').replace('-',' '))
    if item[-1] != 's':
        item += 's'
    info = form.getvalue('info')
    output = """
    <html>
        <head>
            <title>mark</title>
            <link href="../css/custom.css" rel="stylesheet">
            <link href="http://fonts.googleapis.com/css?family=Open+Sans|Montserrat" rel="stylesheet">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        </head>
        <body class="result-bg">
    """
    if item == 'Frappuccino':
        output = output.replace('mark','Frappuccinos by '+capitalize(info))
    else:
        output = output.replace('mark',item+' by '+capitalize(info))
    return output

##=====================##
##=====SB REG MENU=====##
##=====================##

def sb_get(product_type,item):
    url_nutr = 'http://www.starbucks.com/menu/catalog/nutrition?'+product_type+'='+item+'#view_control=nutrition'
    f = urllib.urlopen(url_nutr)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end] # table's html

def sb_store(product_type,item,info,sort):
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
        if not 'oatmeal' in title:
            title = title.replace('tm','&trade;')
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
    
    table = '<table border=1>'
    table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+units[info]+"</th></tr>"
    table += "</th></tr>"
    td_toSort = []
    for key in M:
        td_toSort.append('\n\t<tr>'+'<td>'+capitalize(key)+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>')
    td_Sorted = sorted(td_toSort, key=lambda td: sb_get_num(td) * int(sort))
    for td in td_Sorted:
        table += td
    table += "\n</table>"
    return table

##======================================##
##=====SB SPEC MENU (sodas,frappes)=====##
##======================================##

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
        M[title.replace('-',' ').replace('blended beverage','').replace('\xc3\xa8','&#232;')] = sb_store_spec(product,title)
    table = '<table border=1>'
    table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+units[info]+"</th></tr>"
    td_toSort = []
    for key in M:
        td_toSort.append('\n\t<tr>'+'<td>'+capitalize(key)+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>')
    td_Sorted = sorted(td_toSort, key=lambda td: sb_get_num(td) * int(sort))
    for td in td_Sorted:
        table += td
    table += "\n</table>"
    return table

def sb_html():
    product_type = form.getvalue('product_type')
    item = form.getvalue('item')
    info = form.getvalue('info')
    sort = form.getvalue('sort')
    if item == "frappuccino-blended-beverages" or item == "sodas":
        table = sb_spec_main(item,info,sort) # param product is item
    else:
        table = sb_store(product_type, item, info, sort)
    return table

##========================##
##=====JAMBA REG MENU=====##
##========================##

def jm_store(product_type,info,sort,opt):
    url = 'http://www.jambajuice.com/menu-and-nutrition/menu/'+product_type
    f = urllib.urlopen(url)
    s = f.read()

    l_start = s.find('<div class="mainbody menu menu_listing">')
    l_end = s.find('<section id="Footer1_',l_start)
    listing = s[l_start:l_end]
    listing = listing.split('<div class="prod_block')[1:]

    M={}
    
    for food in listing:

        fn_end = food.find('</h2>')
        fn_start = food.find('<h2>')
        food_name = food[fn_start:fn_end].split('\r\n')
        food_name = food_name[1].strip(' ')
        
        t_start = food.find('<td class="left_col">') # first nutritional table data
        t_end = food.find('</table>',t_start)
        table = food[t_start:t_end]
    
        table_rows = table.split('<td class="left_col">')
        table_rows = table_rows[1:3]+table_rows[6:9]+[table_rows[-1]]
        M_sub = {}
        for row in table_rows:
            if 'Calories' in row:
                nutr_fact = 'calories'
                nutr_num = row.split('\r\n')[1].strip(' ')
                M_sub[nutr_fact] = nutr_num
                continue
            row = row.split(' ')
            if row[1].isalpha(): # checking for two lettered nutr_facts
                del row[0]
            if 'Carb' in row[0]:
                row[0] = 'carbs'
            nutr_fact = row[0].lower()
            nutr_num = row[1][:-2].replace('g','').replace('m','') # removes the '\r\n' (counted as 2 characters)
            M_sub[nutr_fact] = nutr_num
        M[food_name] = M_sub

    table = '<table border=1>'
    table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+units[info]+"</th></tr>"
    td_toSort = []
    for key in M:
        td_toSort.append('\n\t<tr>'+'<td>'+key+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>')
    if opt:
        return td_toSort
    td_Sorted = sorted(td_toSort, key=lambda td: jm_get_num(td) * int(sort))
    for td in td_Sorted:
        table += td
    table += "\n</table>"
    return table

def jm_store_spec(product_type,item,info,sort):
    if item == 'all':
        url = 'http://www.jambajuice.com/menu-and-nutrition/menu/'+product_type
        f = urllib.urlopen(url)
        s = f.read()

        c_start = s.find('<div class="mainbody menu menu_category">')
        c_end = s.find('<section id="Footer1_',c_start)
        categories = s[c_start:c_end]
        categories = categories.split('<div class="prod_block')[1:]

        td_toSort = []
        
        for category in categories:
            start = category.find('<a id=')
            stop = category.find('<img id=')
            category = category[start:stop]
            l_start = category.find('/menu/')+7+len(product_type)
            l_end = category.find('">',l_start)
            listing = category[l_start:l_end]
            td_toSort += jm_store(product_type+'/'+listing,info,sort,True)

        table = '<table border=1>'
        table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+units[info]+"</th></tr>"
        td_Sorted = sorted(td_toSort, key=lambda td: jm_get_num(td) * int(sort))
        for td in td_Sorted:
            table += td
        table += "\n</table>"
        return table
    else:
        return jm_store(product_type+'/'+item,info,sort,False)
    
def jm_html():
    product_type = form.getvalue('product_type')
    item = form.getvalue('item')
    info = form.getvalue('info')
    sort = form.getvalue('sort')
    if item == "listed": # no further directories to enter
        table = jm_store(product_type,info,sort,False)
    else:
        table = jm_store_spec(product_type,item,info,sort)
    return table

def Main():
    print content_type
    print html_top()
    if form.getvalue("Starbucks") == "Submit":
        print sb_html()
    elif form.getvalue("Jamba Juice") == "Submit":
        print jm_html()
    print html_btm

Main() 
