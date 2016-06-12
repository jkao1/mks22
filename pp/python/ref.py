spaces = 4

def css(txt):
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
            prop = dec[:prop_end].split(' ')
            valu = dec[prop_end+1:].split(' ')
            output += ' '*spaces+prop+':'
            #for 'prop: valu1 valu2 valu3;'
            for keyword in value:
                output += ' '+keyword
            output += ';\n'
        output += '}\n'
        print output

d="""
.fa-spin {
    -webkit-animation: fa-spin2 infinite linear;
}
"""
css('@keyframes fa-spin{0%{-webkit-transform:rotate(0deg)')




    
