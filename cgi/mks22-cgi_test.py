#! /usr/bin/python

import cgi

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type:text/html\r\n\r\n'

Top_HTML = """
<html>
<head>
<title>CGI Test 2</title>
</head>
<body>
<b>Nihao Jason</b>
<p>
"""

Bottom_HTML = "</body></html>"

def ShowInputElements():
    form = cgi.FieldStorage()
    print(HTML_HEADER + Top_HTML)
<<<<<<< HEAD
    print('hi</p>')
    print(form.getvalue('name'))
    print(form.getvalue('num'))
=======
    print('nihao</p>')
>>>>>>> dcb4115aba449b57753994a89654ecbfc8168496
    print(Bottom_HTML)

ShowInputElements()
