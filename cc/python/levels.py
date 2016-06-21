#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

max = 11

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

users = '../resources/users.txt'
levels = open('../resources/levels.txt','rU')

r = open(users,'rU')

def level():
    level_num = int(eval(r.read())[uname]['level'])
    if level_num > max:
        a="&lt;U Smart/&gt;"
        b="You have solved all the problems! Buy yourself a cake!"
        b+='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br><a href="../restart.html">>&nbsp;&nbsp;Restart.</a><br>'
        return [a,b]
    level_txt = eval(levels.read())[level_num]['text']
    a='&lt;Problem num=level_num/&gt;'.replace('level_num',str(level_num+1))
    b='<a href="#">>&nbsp;&nbsp;Problem:</a><br>'+level_txt+'(Use four spaces to tab).'
    b += """<br>
    <a href="#">>&nbsp;&nbsp;Solve: </a><br>
    <form method="GET" action="level_check.py">
        
        <textarea rows="15" cols="60" name="user_sln">def foo():</textarea>
        <input type="hidden" name="uname" value="username">
        <input type="hidden" name="pword" value="password"><br>
        <input type="submit" name="submit" value="Enter">
    </form>""".replace('username',uname).replace('password',pword)
    b+='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'
    return [a,b]

def Main():
    print content_type
    lol = level()
    print html_top.replace('jumbotitle',lol[0]).replace('bodyy',lol[1])
    print html_bottom

Main()
# main function needs a return_home
