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

def sb_html():
    print """
    <form method="GET" action="2item_info.py">
        Do you want ...
        <select name="product_type">
            <option value="drink">a drink?</option>
            <option value="food">some food?</option>
        </select><br>
<<<<<<< HEAD
        <input type="submit" name="Starbucks" value="Submit">
=======
        <input type="submit" name="Starbucks" value="Let's Go!'">
    </form>
    """

def pm_html(): #incomplete
    print """
    <form method="GET" action="2item_info.py">
        Do you want ...
        <select name="product_type">
        </select><br>
        <input type="submit" name="Pret A Manger" value="Let's Go!'">
>>>>>>> 4240850cdd301fddbb3560c99871a9a18e481437
    </form>
    """

form = cgi.FieldStorage()

def Main():
    print content_type
    print html_top
    print css
<<<<<<< HEAD
    if form.getvalue('store') == 'starbucks':
        sb_html()
=======
    if form.getvalue('store') == 'Starbucks':
        sb_html()
    elif form.getvalue('store') == 'Pret A Manger':
        pm_html()
>>>>>>> 4240850cdd301fddbb3560c99871a9a18e481437
    print html_btm

Main() 