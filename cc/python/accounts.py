#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

form = cgi.FieldValues()

content_type = "Content-type:text/html\n"
html_top = """<html>
<head>
    <title></title>
</head>
<body>
"""
html_bottom = "</body></html>"

uname = form.getvalue('uname')
pword = form.getvalue('pword')

r = open('../resources/users.txt','rU').read()

def login():
    M = eval(r)
    r.close()
    if uname not in M:
        M[uname] = pword
        html_insert = '<p>Thanks for signing up.</p>'
    else:
        if pword==M[uname]:
            dashboard()
        else:
            html_insert = '<b>You entered the wrong password.</b><a href="../index.html">Back to homepage.</a>'
    

def Main():
    print content_type
    print html_top
    print html_insert
    print html_bottom
