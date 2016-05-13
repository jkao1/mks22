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
    print('Hello, ' + form.getvalue('fname') + ' ' + form.getvalue('lname'))
    print(Bottom_HTML)

Main()
