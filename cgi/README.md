<<<<<<< HEAD
=======
###HTML:
```html
<form method="GET" action="mks22-cgi_test.py"> <!--Once entered, the action GETs the input-->
  Enter a multiple of 3: <input type="text" name="num"> <!--Name assigns the variable-->
</form>
```

###Python:
```python
#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

HTML_HEADER = 'Content-type:text/html\r\n\r\n' 
Top_HTML = """<html><head><title>CGI Test 2</title></head><body>"""
Bottom_HTML = "</body></html>"
```
Btw, to change file permissiosn in the CMD line, type
```
chmod +x filename.py
```
>>>>>>> 42d7ebad7cbcae704065eb6c7a45f352d45681bf
###urllib usage
```python
>>> import urllib
>>> f=urllib.urlopen('http://www.micromind.com/stuy'_
>>> s=f.read()
<<<<<<< HEAD
=======
```

###Forms Interaction
```html
<input type="text" name="fred">
<input type="submit" name="button" value="ON">
```
- name = back-end var
- value = what shows up by default in textbox, can be the back-end var name if value is on a button
- buttons need name/values to be differentiated in your program

method="GET" will show variables inside the url.<br>
method="POST" will be sent but without showing the variables.
>>>>>>> 42d7ebad7cbcae704065eb6c7a45f352d45681bf
