#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head> 
        <title></title>
        <link href="css/custom.css" rel="stylesheet">
        <link href="http://fonts.googleapis.com/css?family=Open+Sans|Montserrat" rel="stylesheet">
    </head>
    <body class="item-info-bg">
    <div class="header">
"""
html_btm = "</div></body></html>"

form = cgi.FieldStorage()

##==========================##
##=====HELPER FUNCTIONS=====##
##==========================##

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
    
##===================##
##=====STARBUCKS=====##
##===================##

def sb_html():
    product_type = form.getvalue("product_type") 
    output = '<form method="GET" action="3result.py">'
    if product_type == 'drink':
        output += """
        <p class="choose-item">Choose a drink:</p>
        <select name="item">
            <option value="refreshers">Refreshers</option>
            <option value="iced-coffee">Iced Coffee</option>
            <option value="iced-tea">Iced Tea</option>
            <option value="espresso">Espresso</option>
            <option value="chocolate">Chocolate Drinks</option>
            <option value="brewed-coffee">Brewed Coffee</option>
            <option value="bottled-drinks">Bottled Drinks</option>
            <option value="frappuccino">Frappuccino</option>
            <option value="sodas" disabled>Sodas !coming soon!</option>
            <option value="smoothies">Smoothies</option>
            <option value="kids-drinks-and-other">Other</option>
        </select><br>
        """
    elif product_type == 'food':
        output += """
        <p class="choose-item">Choose some food:</p>
        <select name="item">
            <option value="hot-breakfast">Hot Breakfast</option>
            <option value="bistro-boxes">Bistro Boxes</option>
            <option value="bakery">Bakery</option>
            <option value="yogurt-and-fruit">Yogurt and Fruit</option>
            <option value="sandwiches-panini-and-wraps">Sandwiches, Paninis, and Wraps</option>
        </select><br>
        """
    output += """
        <p class="choose-item choose-item-sort">Sort by the</p>
        <select name="sort">
            <option value="-1">highest</option>
            <option value="1">lowest</option>
        </select>
        <p class="choose-item choose-item-sort">amount of</p>
        <select name="info">
            <option value="calories">calories</option>
            <option value="fat">fat</option>
            <option value="carbs">carbs</option>
            <option value="fiber">fiber</option>
            <option value="protein">protein</option>
            <option value="sodium">sodium</option>
        </select><p class="choose-item choose-item-sort".</p><br>
    """
    output += '<input type="hidden" name="product_type" value="'+product_type+'">'
    output += '<input type="submit" name="Starbucks" value="Submit"></form>'
    print output

##=======================##
##=====PRET A MANGER=====##
##=======================##

def pm_get(product_type):
    url = "www.pret.com/en-us/our-menu/"+product_type+".aspx"
    f = urllib.urlopen(url)
    s = f.read()
    t_start = s.rfind('<!-- filter results -->')
    t_end = s.find('</section>',t_start)
    return s#[t_start:t_end]

def pm_store(product_type):
    main = pm_get(product_type)
    main = main.split('<div class="textwrap">')
    return main
   
def pm_html(): #incomplete
    product_type = form.getvalue("product_type") 
    output = '<form method="GET" action="3result.py">'
    #for hot food, don't forget '685-pret's-hot-spinach-tomato-mac-%26-cheese' 
    if product_type == "lunch":
        output += """
        <p class="choose-item">Choose a lunch item:</p><br>
        <select name="item">
            <option>Sandwiches</option>
            <option>Baguettes</option>
            <option>Hot Food</option>
            <option>Wraps</option>
            <option>Salads</option>
        </select><br>
        """
    elif product_type == "soups":
        output += """
        <p class="choose-item">Choose a type of soup:</p><br>
        <select name="item">
            <option>Today's Soups</option>
            <option>All Soups</option>
        </select>
        """
    elif product_type == "snacks":
        output += """
        <p class="choose-item">Choose a type of snack:</p><br>
        <select name="item">
            <option value="129-pret-pots">Pret's Pots</option>
            <option value="74-treats-&-snacks">Treats</option>
            <option value="76-bakery">Bakery</option>
            <option value="77-fresh-fruit">Fresh Fruit</option>
        </select>
        """
    elif product_type == "drinks":
        output += """
        <p class="choose-item">Choose a type of snack:</p><br>
        <select name="item">
            <option value="124-organic-coffee">Organic Coffee</option>
            <option value="78-cold-drinks">Cold Drinks</option>
        </select>
        """
    else:
        output = pm_store(product_type)
        print "i still have to complete the pret store function"
        
    output += '<input type="hidden" name="product_type" value="'+product_type+'">'
    output += '<input type="submit" name="Pret A Manger" value="Submit"></form>'
    print output
    
def Main():
    print content_type
    print html_top
    if form.getvalue('Starbucks') == "Yes":
        sb_html()
    elif form.getvalue('Pret A Manger') == "Yes":
        pm_html()
    print html_btm

Main() 
