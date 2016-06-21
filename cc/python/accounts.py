#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
uname = form.getvalue('uname')
pword = form.getvalue('pword')
status = form.getvalue('submit')

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
index = '../home.html'
return_home = '<br><a href="../index.html">>&nbsp;&nbsp;Return to home.</a>'

r = open(users,'rU')

def error():
    if uname is None:
        return 'Please enter a username.'
    elif pword is None:
        return 'Please enter a password.'

def account():
    M = eval(r.read())
    r.close()
    msg = ''

    if error() is not None and status!="Delete":
        msg = 'error: ' + error()
        return msg

    if status=='Sign Up':
        if uname in M:
            a='Username already exists.'
        else:
            M[uname] = {'pword':pword,'level':0}
            a='Account created.'
        b='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'
    elif status=='Log In':
        if uname in M:
            if pword==M[uname]['pword']:
                a='&lt;hi user="'+uname+'"/&gt;'
                b = """
                <a href="../code.html">>&nbsp;&nbsp;Continue coding.</a><br>
                <a href="../progress.html">>&nbsp;&nbsp;Track your progress.</a><br>
                <a href="../help.html">>&nbsp;&nbsp;Need help? Visit our forum.</a><br>
                <a href="../delete.html">>&nbsp;&nbsp;Delete account.</a><br>
                """.replace('username',uname).replace('password',pword)
            else:
                a='Wrong username/password combo.'
                b='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'
        else:
            a='Username not recognized.'
            b='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'

    elif status=='Delete':
        if uname in M:
            del M[uname]
            a=uname + ' was deleted.'
        else:
            a=uname +' was not found.'
        b='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'
        
    elif status=='Restart':
        if uname in M:
            M[uname]['level'] = 0
            a=uname + ' has had levels reset.'
        else:
            a=uname +' was not found.'
        b='<a href="../index.html">>&nbsp;&nbsp;Return home.</a><br>'

    w = open(users,'w')
    w.write(str(M))
    w.close()

    return [a,b]

def Main():
    print content_type
    um = account()
    print html_top.replace('jumbotitle',um[0]).replace('bodyy',um[1])
    print html_bottom

Main()
# main function needs a return_home