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

Top_HTML = """
<html><head>
<title>CGI Test 2</title>
</head><body>
<b>Nihao Jason</b>
"""
Bottom_HTML = "</body></html>"
```
<a href="http://http://bert.stuy.edu/pbrooks/ml2/Python-Forms-processing.htm">explanation</a>
<br>

###Extra:
- Go to FTP and change file permissions to allow public to execute
