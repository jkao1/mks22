#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head> 
    <title></title>
"""
css = """
    <style>
    table {display:block;margin:0 auto}
    </style>
</head>
<body>
"""
html_btm = "</body></html>"

form = cgi.FieldStorage()

def sb_html():
    product_type = form.getvalue("product_type") 
    output = '<form method="GET" action="3result.py">'
    if product_type == 'drink':
        output += """
        Choose a drink:
        <select name="item">
            <option value="refreshers">Refreshers</option>
            <option value="iced-coffee">Iced Coffee</option>
            <option value="iced-tea">Iced Tea</option>
            <option value="espresso">Espresso</option>
            <option value="chocolate">Chocolate Drinks</option>
            <option value="brewed-coffee">Brewed Coffee</option>
            <option value="bottled-drinks">Bottled Drinks</option>
            <option value="frappuccino" disabled>Frappuccino !coming soon!</option>
            <option value="sodas" disabled>Sodas !coming soon!</option>
            <option value="smoothies">Smoothies</option>
            <option value="kids-drinks-and-other">Other</option>
        </select><br>
        """
    elif product_type == 'food':
        output += """
        Choose some food:
        <select name="item">
            <option value="hot-breakfast">Hot Breakfast</option>
            <option value="bistro-boxes">Bistro Boxes</option>
            <option value="bakery">Bakery</option>
            <option value="yogurt-and-fruit">Yogurt and Fruit</option>
            <option value="sandwiches-panini-and-wraps">Sandwiches, Paninis, and Wraps</option>
        </select><br>
        """
    output += """
        Sort by the
        <select name="sort">
            <option value="high">highest</option>
            <option value="low">lowest</option>
        </select>
        amount of
        <select name="info">
            <option value="calories">calories</option>
            <option value="fat">fat</option>
            <option value="carbs">carbs</option>
            <option value="fiber">fiber</option>
            <option value="protein">protein</option>
            <option value="sodium">sodium</option>
        </select>.<br>
    """
    output += '<input type="hidden" name="product_type" value="'+product_type+'">'
    output += '<input type="submit" name="Starbucks" value="Submit"></form>'
    print output

def pm_html(): #incomplete
    product_type = form.getvalue("product_type") 
    output = '<form method="GET" action="3result.py">'
    print "nothing yet"
    
def Main():
    print content_type
    print html_top
    print css
    if form.getvalue('Starbucks') == "Yes":
        sb_html()
    elif form.getvalue('Pret A Manger') == "Yes":
        pm_html()
    print html_btm

Main() 
