#! /usr/bin/python


import cgi, cgitb
cgitb.enable()

top = "Content-type:text/html\r\n\r\n"
Top_HTML = """
<head>
<title>hi</title>
</head>
<body>
"""

Bottom_HTML = "</body></html>"

def Main():
    form = cgi.FieldStorage()
    print(top)
    print(Top_HTML)
    print('Hello, ' + form.getvalue('fname') + ' ' + form.getvalue('lastname'))
    print(Bottom_HTML)

Main()