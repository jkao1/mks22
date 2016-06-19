#! /usr/bin/python

from html5print import HTMLBeautifier
import jsbeautifier

import cgi, cgitb
cgitb.enable()

content_type = 'Content-type:text/html\n'
top = """
<html>
    <head>
        <title>Pretty Printed</title>
    </head>
    <body>
        <p>
"""
bottom = '</body></html>'
"""
form = cgi.FieldStorage()

spaces=4
def css(txt,spaces):
    L = txt.split('}')

    for s in L[:-1]:
        output = ''
        s = s.replace('\n','').replace('\t','')
        slec_end = s.find('{')
        slec = s[:slec_end]
        output += slec.strip(' ') + ' {\n'
        
        if ';' in s:
            dec_block = s[slec_end+1:].split(';')
        else:
            dec_block = s[s.find('{')+1:]
            dec_block = [dec_block,'']
            
        for dec in dec_block[:-1]:
            prop_end = dec.find(':')
            prop = dec[:prop_end].strip(' ')
            value = dec[prop_end+1:].split(' ')
            output += ' '*spaces+prop+':'
            for keyword in value:
                output += ' '+keyword
            output += ';\n'
        output += '}\n'
        print output

prob_css = [
    '.fa-contao:before{content:"\f26d"}',
    '@keyframes fa-spin{0%{-webkit-transform:rotate(0deg);}}'
    ]

def html(txt):
    return HTMLBeautifier.beautify(txt, 4)

def js(txt):
    res = jsbeautifier.beautify(txt)
    return res"""

def Main():
    print content_type
    print top
    #print js("""var x = 5 + 6 ;var y = x * 10;document.getElementById("demo").innerHTML = y;""")
    print bottom

Main()








    
