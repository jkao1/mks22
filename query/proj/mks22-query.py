#! /usr/bin/python


import cgi, cgitb
cgitb.enable()

top = "Content-type:text/html\r\n\r\n"
Top_HTML = """
<head>
</head>
<body>
"""

Bottom_HTML = "</body></html>"

def Main():
    form = cgi.FieldStorage()
    print(top)
    print(Top_HTML)
    print("<link href='mks22-query.css' rel='stylesheet'")
    print('<p class="secpage-head">Hello, ' + form.getvalue('fname') + ' ' + form.getvalue('lname') + '.</p><br>')
    print('<p class="secpage-desc">' + 'Please proceed to our <a href="http://www.micromind.com">website</a>.</p><br><br><br><br>')
    print('<p class="subscribe">Subscribe to view future products: <input type="text" placeholder="hi@micromind.com" size="20"')
    print(Bottom_HTML)

Main()