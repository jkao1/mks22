#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html = """
<html>
    <head> 
        <title>Choose a store</title>
        <link href="../css/custom.css" rel="stylesheet">
        <link href="http://fonts.googleapis.com/css?family=Open+Sans|Montserrat" rel="stylesheet">
    </head>
    <body>
        <section class="container">
            <div class="header">
                <form method="GET" action="1product_type.py">
                    <p class="bg-text">Choose <span>a store:</span></p><br>
                    <input type="submit" name="store" value="Starbucks">
                    <input type="submit" name="store" value="Jamba Juice">
                </form>
            </div>
        </section>
    </body>
</html>
"""

def Main():
    print content_type
    print html

Main() 








