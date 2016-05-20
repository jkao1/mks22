import urllib

def html(product_type,item):
    url_nutr = 'http://www.starbucks.com/menu/catalog/nutrition?'+product_type+'=' + item + '#view_control=nutrition'
    f = urllib.urlopen(url_nutr)
    s = f.read()
    t_start = s.rfind('<table ')
    t_end = s.find('</table>',t_start)
    return s[t_start:t_end]
 
th = ['Calories', 'Fat', 'Carbs', 'Fiber', 'Protein', 'Sodium']

def get(product_type,item):
    main = html(product_type,item) 
    main = main.split('</tr>')[1:-1]
    M = {}
    for i in range(len(main)): # loops all <tr>'s of all products in main
        product = main[i]
        product = product.split('</td>')[:-1]
        cont = product[0] # container of title
        if i == 0:
            title = cont[cont.find('/',57)+1:cont.find('"',57)]
        else:
            title = cont[cont.find('/',42)+1:cont.find('"',42)]
        dic = {}
        ls = []
        for item in product: # loops all <td>'s from the <tr>
            angle = item.rfind('>')
            ls.append(item[angle+1:])
        for i in range(6):
            dic[th[i]] = ls[i]
        M[title] = dic
    query = "Calories"
    table = "<table>"
    for key in M:
        table += '<tr>'+'<td>'+key+'</td>'+'<td>'+M[key][query]+'</td>'+'</tr>'
    print table           
    
