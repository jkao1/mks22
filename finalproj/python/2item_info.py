#! /usr/bin/python

import urllib
import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head> 
        <title></title>
        <link href="../css/custom.css" rel="stylesheet">
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

# fetches numbers from <td> for sorting
def get_num(s):
    num_end = s.rfind('</td>')
    num_start = s.find('<td>', num_end-7)+4
    try:
        return int(s[num_start:num_end])
    except:
        return '-'

def html_top():
    product_type = form.getvalue('product_type')
    output = """
    <html>
        <head> 
            <title>mark</title>
            <link href="../css/custom.css" rel="stylesheet">
            <link href="http://fonts.googleapis.com/css?family=Open+Sans|Montserrat" rel="stylesheet">
        </head>
        <body class="item-info-bg">
        <div class="header">
    """
    output = output.replace('mark','Choose a '+capitalize(product_type))
    return output
    
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
            <option value="frappuccino-blended-beverages">Frappuccino</option>
            <option value="sodas">Sodas</option>
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
    return output

def jm_html():
    product_type = form.getvalue("product_type") 
    output = '<form method="GET" action="3result.py">'
    #listed: juices, energybowls,juiceshots,jambago,kids,makeitlight
    #unlisted: smoothies,tastyy-bites, boosts
    if product_type == 'smoothies':
        output += """
        <p class="choose-item">Choose a type of smoothie:</p>
        <select name="item">
            <option value="all">All smoothies</option>
            <option value="classic-smoothies">Classic</option>
            <option value="island-getaway-smoothies">Island Getaway</option>
            <option value="whole-food-nutrition">Whole Food Nutrition</option>
            <option value="all-fruit-smoothies">All-Fruit</option>
            <option value="fit-n-fruitful">Fit 'N Fruitful</option>
            <option value="fruit-veggie">Fruit & Veggie</option>
            <option value="functional-smoothies">Functional</option>
            <option value="creamy-treats">Creamy Treats</option>
        </select><br>
        """
    elif product_type == 'tasty-bites':
        output += """
        <p class="choose-item">Choose a tasty bite:</p>
        <select name="item">
            <option value="all">All tasty bites</option>
            <option value="oatmeal">Oatmeal</option>
            <option value="artisan-flatbreads">Artisan Flatbreads</option>
            <option value="baked-goods">Baked Goods</option>
            <option value="breakfast-wraps">Breakfast Wraps</option>
            <option value="toasted-bistro-sandwiches">Toasted Bistro Sandwiches</option>
        </select><br>
        """
    elif product_type == 'boosts':
        output += """
        <p class="choose-item">Choose a boost:</p>
        <select name="item">
            <option value="all">All boosts</option>
            <option value="whole-food-boosts">Whole Food Boosts</option>
            <option value="boosts">Boosts</option>
        </select><br>
        """
    else:
        output += '<input type="hidden" name="item" value="listed">'
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
    output += '<input type="submit" name="Jamba Juice" value="Submit"></form>'
    return output
    
def Main():
    print content_type
    print html_top()
    if form.getvalue('Starbucks') == "Yes":
        print sb_html()
    elif form.getvalue('Jamba Juice') == "Yes":
        print jm_html()
    print html_btm

Main() 
