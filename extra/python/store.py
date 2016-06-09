#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

content_type = "Content-type:text/html\n"

html_top = """
<html>
    <head>
        <title>Hmm</title>
    </head>
    <body>
"""
html_btm = "</body></html>"

form = cgi.FieldStorage()

def Main():
    uname = form.getvalue(uname,'')
    pword = form.getvalue(pword,'')

def read(filename):
    f = open(filename,'rU')
    s = f.read()
    f.close()
    
