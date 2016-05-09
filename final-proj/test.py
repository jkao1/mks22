#! /usr/bin/python

import cgi

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type:text/html\r\n\r\n'

Top_HTML = """
<html>
<head>
</head>
<body>
"""

Bottom_HTML = "</body></html>"

def ShowInputElements():
    form = cgi.FieldStorage()
    print(HTML_HEADER + Top_HTML)
    print('Hello ' + form.getvalue('fname') + form.getvalue('lname'))    
    print(Bottom_HTML)

ShowInputElements()
