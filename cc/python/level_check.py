#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
uname = form.getvalue('uname')
pword = form.getvalue('pword')
user_sln = form.getvalue('user_sln')

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

users = eval(open('../resources/users.txt','rU').read())
levels = eval(open('../resources/levels.txt','rU').read())

def match():
    func_name = user_sln[4:user_sln.find('(')]
    M = {}
    try:
        exec user_sln in M
    except:
        return False
    level_num = users[uname]['level']
    level_sln = levels[level_num]['try']
    for test in level_sln:
        func = "M['fn']param".replace('fn',func_name).replace('param',test[0])
        try:
            result = str(eval(func)) != test[1]
        except:
            return False
        if result:
            return False
    return True

def check():
    if match():
        users[uname]['level'] += 1
        write_level = open('../resources/users.txt','w')
        write_level.write(str(users))
        write_level.close()
        a='&lt;Yay!/&gt;'
        b="""<form method="GET" action="levels.py">
        <a href="#">>&nbsp;&nbsp;Next <input type="submit" name="submit" value="level.">.</a><br>
            <input type="hidden" name="uname" value="username">
            <input type="hidden" name="pword" value="password">
        </form>""".replace('username',uname).replace('password',pword)
        b+='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'
    else:
        a='&lt;Whoops!/&gt;'
        b="""
            Something went wrong.<br>
            <form method="GET" action="levels.py">
            <a href="#">>&nbsp;&nbsp;Go <input type="submit" name="submit" value="back">.</a>
            <input type="hidden" name="uname" value="username">
            <input type="hidden" name="pword" value="password">
        </form>""".replace('username',uname).replace('password',pword)
    return [a,b]

def Main():
    print content_type
    lol = check()
    print html_top.replace('jumbotitle',lol[0]).replace('bodyy',lol[1])
    print html_bottom

Main()

