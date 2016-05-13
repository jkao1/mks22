#! /usr/bin/python


import cgi, cgitb
cgitb.enable()

top = "Content-type:text/html\r\n\r\n"
Top_HTML = """
<head>
    
    <link href='https://fonts.googleapis.com/css?family=Open+Sans|Montserrat' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <link href='mks22-query.css' rel='stylesheet' type='text/css'>

</head>
<body>
"""

Bottom_HTML = "</body></html>"

def Main():
    form = cgi.FieldStorage()
    print(top)
    print(Top_HTML)
    print('Hello, ' + form.getvalue('fname') + ' ' + form.getvalue('lastname'))
    print(Bottom_HTML)