import urllib

def jm_get_num(s):
    num_start = s.rfind('<td>')+4
    num_end = s.rfind('</td>')
    try:
        return int(s[num_start:num_end])
    except:
        return '-'
    
def jm_store(product_type,info,sort):
    url = 'http://www.jambajuice.com/menu-and-nutrition/menu/'+product_type
    f = urllib.urlopen(url)
    s = f.read()

    l_start = s.find('<div class="mainbody menu menu_listing">')
    l_end = s.find('<section id="Footer1_',l_start)
    listing = s[l_start:l_end]
    listing = listing.split('<div class="prod_block')[1:]

    M={}
    
    for food in listing:

        fn_end = food.find('</h2>')
        fn_start = food.find('<h2>')
        food_name = food[fn_start:fn_end].split('\r\n')
        food_name = food_name[1].strip(' ')
        
        t_start = food.find('<td class="left_col">') # first nutritional table data
        t_end = food.find('</table>',t_start)
        table = food[t_start:t_end]
    
        table_rows = table.split('<td class="left_col">')
        table_rows = table_rows[1:3]+table_rows[6:9]+[table_rows[-1]]
        M_sub = {}
        for row in table_rows:
            if 'Calories' in row:
                nutr_fact = 'calories'
                nutr_num = row.split('\r\n')[1].strip(' ')
                M_sub[nutr_fact] = nutr_num
                continue
            row = row.split(' ')
            if row[1].isalpha(): # checking for two lettered nutr_facts
                del row[0]
            if 'Carb' in row[0]:
                row[0] = 'carbs'
            nutr_fact = row[0].lower()
            nutr_num = row[1][:-2].replace('g','').replace('mg','') # removes the '\r\n' (counted as 2 characters)
            M_sub[nutr_fact] = nutr_num
        M[food_name] = M_sub

    table = '<table border=1>'
    table += "\n\t<tr><th>Product Name</th><th>"+info.capitalize()+"</th></tr>"
    td_toSort = []
    for key in M:
        td_toSort.append('\n\t<tr>'+'<td>'+key+'</td>'+'<td>'+M[key][info]+'</td>'+'</tr>')
    td_Sorted = sorted(td_toSort, key=lambda td: jm_get_num(td) * int(sort))
    for td in td_Sorted:
        table += td
    table += "\n</table>"
    return table
    
