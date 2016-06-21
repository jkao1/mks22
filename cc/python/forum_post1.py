#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
uname = form.getvalue('uname')
content = form.getvalue('content')
title = form.getvalue('title')


content_type = "Content-type:text/html\n"
html_top = """
<html>
    
    <head>
        <title>CodeCow</title>
        <link href='https://fonts.googleapis.com/css?family=Source+Code+Pro' rel='stylesheet' type='text/css'>
        <style>
            body {
                font-family: 'Source Code Pro';
            }
            a {
                text-decoration: none;
                font-size: 20px;
                display: block;
                padding: 10px 30px 0px 30px;
            }
            #hi {
                display: block;
                height: 200px;
                color: white;
                background: #444;
            }
            #hi center {
                font-size: 80px;
            }
            input[type="text"], textarea {
                display: block;
                font-family: 'Source Code Pro';
                font-size: 14px;
                padding: 5px;
            }
            input[type=submit] {
                font-family: 'Source Code Pro';
            }
            form {
                position: relative;
                left: 50px;
            }
            span {
                position: relative;
            }
            .completed {
                color: black;
            }
            .uncompleted {
                color: gray;
            }
        </style>
    </head>

    <body>
        <br><br>
        <div id="hi">
            <center>jumbotitle</center>
        </div><br>
        <div style="display:block;height:1px;background:#333;"></div><br>
        bodyy
"""
html_bottom = "</body></html>"

M = eval(open('../resources/forum.txt','rU').read())
M[len(M)] = {'content':content,'title':title,'author':'anonymous'}

w = open('../resources/forum.txt','w')
w.write(str(M))
w.close()

a='&lt;Success!/&gt;'
b = """
<a href="forum_view.py">>&nbsp;&nbsp;View threads</a><br>
<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>"""

def Main():
    print content_type
    print html_top.replace('jumbotitle',a).replace('bodyy',b)
    print html_bottom

Main()
