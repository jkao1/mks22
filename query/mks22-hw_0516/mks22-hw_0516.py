#! /usr/bin/python

import cgi, cgitb
cgitb.enable()

"""
*Disregarding a few changes, the ExtremeScores_helper() function and the
ExtremeScores() function, which are combined in this file, was written by Peter
Brooks - micromind.com.
"""

content_type = 'Content-type:text/html\n'
top = """
<html>
<head>
<title>Back-end is cool</title>
<style>
td {width: 250px}
table {display:block;margin:0 auto;}
</style>
</head>
<body>"""
bottom = '</body></html>'

form = cgi.FieldStorage()
             
def ExtremeScores(which_column, how_many, is_top):
    
    # read the file and split into lines...
    f=open('SAT-2010.csv','rU')
    s=f.read()
    f.close()
    output=s.split('\n')[0].split(',')+['Total']
    output=[output[which_column]]
    lines=s.split('\n') 
        
    lines = lines[1:-1]

    hm=[]  
    for line in lines:
        fields=line.split(',')
        if fields[-1] != 's':
            if '"' not in line:  # has ordinary school name? add it
                hm.append(fields)
            else:  # school name has double-quotes...
                # the last 4 fields are always numbers, so
                school_name_in_parts = fields[1:-4]
                school_name=','.join(school_name_in_parts)
                # remove the double-quotes
                school_name=school_name[1:-1]
                # put the fields back together
                new_fields=fields[0:1]+[school_name]+fields[-4:]
                hm.append(new_fields)

    # create a list of just [[score,school_name],[score,school_name],...]
    list_to_sort=[]
    for f_list in hm
        if 3<=which_column<=5:
            list_to_sort.append([int(f_list[which_column]),f_list[1]])
        else:  # we want the total SAT score
            total=int(f_list[3])+int(f_list[4])+int(f_list[5])
            list_to_sort.append([total,f_list[1]])
            
    # now sort it
    if is_top:
        sorted_list=sorted(list_to_sort,reverse=True)
    else:
        sorted_list=sorted(list_to_sort)
    
    return output + sorted_list[:how_many]

def Main():
    print(content_type)
    print(top)
    table='<table border="1"><tr><th>School</th>'
    if form.getvalue('getFixedInfo') == 'Submit':
        table+='<th>Total mean SAT score/th>'
        info=ExtremeScores(6,5,False)
        for ls in info[1:]:
            table+='<tr><td>'+ls[1]+'</td><td>'+str(ls[0])+'</td></tr>'
        table+='</table>'
        print(table)
    else:
        col=int(form.getvalue('which_column'))
        num=int(form.getvalue('how_many'))
        is_top=form.getvalue('is_top')=='True'
        info=ExtremeScores(col,num,is_top)
        table+='<th>'+info[0]+'</th>'
        
        for ls in info[1:]:
            table+='<tr><td>'+ls[1]+'</td><td>'+str(ls[0])+'</td></tr>'
        table+='</table>'
        print(table)
    print(bottom)

Main()
 
