#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head> 
        <title>Pick & Choose</title>
        <link href="../css/custom.css" rel="stylesheet">
        <link href="http://fonts.googleapis.com/css?family=Open+Sans|Montserrat" rel="stylesheet">
    </head>
    <body class="item-info-bg">
    <div class="header">
        <script>
            document.getElementById("toIndex").onclick = function () {
                location.href = "www.yoursite.com";
            };
        </script>
        <button id="toIndex">Back</button>
"""
html_btm = "</div></body></html>"

def sb_html():
    return """
    <form method="GET" action="2item_info.py">
        <p>Do you want ...</p><br>
        <select name="product_type">
            <option value="drink">a drink?</option>
            <option value="food">some food?</option>
        </select>
        <br>
        <input type="submit" name="Starbucks" value="Yes">
    </form>
    """

def jm_html():
    return """
    <form method="GET" action="2item_info.py">
        <p>Do you want ...</p><br>
        <select name="product_type">
            <option value="juices">fresh juice?</option>
            <option value="energy-bowls">a nutritious energy bowl?</option>
            <option value="freshly-squeezed-juice-shots">shots? (of juice of course)</option>
            <option value="smoothies">blended-to-order smoothies?</option>
            <option value="jambago">a superquick to-go smoothie?</option>
            <option value="tasty-bites">a tasty bite?</option>
            <option value="jamba-kids">a kids item?</option>
            <option value="make-it-light">something light?</option>
            <option value="boosts">caffeine-free energy?</option>
        </select>
        <input type="submit" name="Jamba Juice" value="Yes">
    </form>
    """

form = cgi.FieldStorage()

def Main():
    print content_type
    print html_top
    if form.getvalue('store') == 'Starbucks':
        print sb_html()
    elif form.getvalue('store') == 'Jamba Juice':
        print jm_html()
    print html_btm

Main() 








