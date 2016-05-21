#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head> 
    <title>Title</title>
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
    output = """
    <form method="GET" action="result.py">
        Choose an item:
        <select name="item">
            <option value="refreshers">Refreshers</option>
            <option value="iced-coffee">Iced Coffee</option>
            <option value="iced-tea">Iced Tea</option>
            <option value="espresso">Espresso</option>
            <option value="chocolate">Chocolate Drinks</option>
            <option value="brewed-coffee">Brewed Coffee</option>
            <option value="bottled-drinks">Bottled Drinks</option>
            <option value="smoothies">Smoothies</option>
            <option value="kids-drinks-and-other">Other</option>
        </select><br>
        Choose a nutrition statistic:
        <select name="info">
            <option value="calories">Calories</option>
            <option value="fat">Fat</option>
            <option value="carbs">Carbs</option>
            <option value="fiber">Fiber</option>
            <option value="protein">Protein</option>
            <option value="Sodium">Sodium</option>
        </select><br>
    """
    output += '<input type="hidden" name="product_type" value="'+product_type+'">'
    output += '<input type="submit" name="Starbucks" value="Submit"></form>'
    print output
    
def Main():
    print content_type
    print html_top
    print css
    if form.getvalue('Starbucks') == 'Submit':
        sb_html()
    print html_btm

Main() 
