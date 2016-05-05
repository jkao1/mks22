###Notes

HTML:
```html
<form method="GET" action="mks22-cgi_test.py"> 
  Enter a multiple of 3: <input type="text" name="num">
</form>
```

Python:
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
