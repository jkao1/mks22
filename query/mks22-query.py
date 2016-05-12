#! usr/bin/python

import cgi, cgitb
cgitb.enable()

HTML_HEADER = 'Content-type:text/html\r\n\r\n' 

Top_HTML = """
<html><head>
<title>CGI Test 2</title>
</head><body>
"""

Bottom_HTML = "</body></html>"

def Main():
    