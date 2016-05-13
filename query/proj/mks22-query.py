#! /usr/bin/python


import cgi, cgitb
cgitb.enable()

top = "Content-type:text/html\r\n\r\n"
Top_HTML = """
<head>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans|Montserrat">
<link rel="stylesheet" href="mks22-query.css">
</head>
<body>
"""

Bottom_HTML = "</body></html>"

def Main():
    form = cgi.FieldStorage()
    print(top)
    print(Top_HTML)
    print('<p class="secpage-head">Hello, ' + form.getvalue('fname') + ' ' + form.getvalue('lname') + '.</p><br>')
    print('<p class="secpage-desc">' + 'Please proceed to our <a href="http://www.micromind.com">website</a>.</p><br>')
    print('<p class="subscribe">Subscribe to view future products: <input type="text" style="display:block;margin:0 auto;position:relative;top:10px;" placeholder="hi@micromind.com" size="20"')
    print('Hello, ' + form.getvalue('fname') + ' ' + form.getvalue('lname'))
    print(Bottom_HTML)

Main()
