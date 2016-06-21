#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
uname = form.getvalue('uname')
pword = form.getvalue('pword')

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
            input[type="text"] {
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

users = eval(open('../resources/users.txt','rU').read())
levels = eval(open('../resources/levels.txt','rU').read())

def progress():
    M=levels
    a='&lt;Progress user="uname"/&gt;'.replace('uname',uname)
    b='<a href="#">>&nbsp;&nbsp;Completed:</a><br><div class="completed">'
    uncompleted ='</div><div class="uncompleted">'
    up_to = users[uname]['level']
    for i in range(len(levels)):
        if i < up_to:
            b+='Level '+str(i+1)+': '+str(M[i]['title'])+'<br>'
        else:
            uncompleted+='Level '+str(i+1)+': '+str(M[i]['title'])+'<br>'
    b+='<a href="#">>&nbsp;&nbsp;Uncompleted:</a><br>'+uncompleted
    b+='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'
    return [a,b]

def Main():
    print content_type
    lol = progress()
    print html_top.replace('jumbotitle',lol[0]).replace('bodyy',lol[1])
    print html_bottom

Main()
