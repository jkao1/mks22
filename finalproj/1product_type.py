#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head> 
        <title>Title</title>
        <link href="css/custom.css" rel="stylesheet">
        <link href="http://fonts.googleapis.com/css?family=Open+Sans|Montserrat" rel="stylesheet">
    </head>
    <body class="item-info">
    <div class="header">
"""
html_btm = "</div></body></html>"

def sb_html():
    print """
    <form method="GET" action="2item_info.py">
        <p>Do you want ...</p><br>
        <select name="product_type">
            <option value="drink">a drink?</option>
            <option value="food">some food?</option>
        </select><br>
        <input type="submit" name="Starbucks" value="Let's Go!">
    </form>
    """

def pm_html(): #incomplete
    print """
    <form method="GET" action="2item_info.py">
        Do you want ...
        <select name="product_type">
        </select><br>
        <input type="submit" name="Pret A Manger" value="Let's Go!'">
    </form>
    """

form = cgi.FieldStorage()

def Main():
    print content_type
    print html_top
    if form.getvalue('store') == 'Starbucks':
        sb_html()
    elif form.getvalue('store') == 'Pret A Manger':
        pm_html()
    print html_btm

Main() 
