import urllib

def jm(product):
    url = 'http://www.jambajuice.com/menu-and-nutrition/menu/'+product
    f = urllib.urlopen(url)
    s = f.read()

    l_start = s.find('<div class="mainbody menu menu_listing">')
    l_end = s.find('<section id="Footer1_',l_start)
    listing = s[l_start:l_end]



    
    """
    listing = listing.split('<div class="updatePanel"')

    M = {}
    for i in range(1,len(listing)): # loops every food item
        output = listing[i]
        o_start = output.find('<tr class="table_line">')
        o_end = output.find('<sup>')
        output = output[o_start:o_end].replace('\r\n','')

        output = output.split('<td class="left_col"')
        output = output[1:3]+output[6:11]+[output[-1]] # otherwise there are repeats of nutrition info
        t_container = output[-1] # item that has title
        t_start = t_container.rfind('>')+1
        food = t_container[t_start:].strip(' ')
        sub = {}
        #return t_container
        for i in range(len(output)): # loops every nutrition info
            elem = output[i]
            l = elem.split(' ')
            if l[1].isalpha():
                title = l[1]
                num = l[2]
            else:
                title = l[0][1:]
                num = l[1]
            if i == 0:
                num = l[20]
            sub[title.lower()] = num
        del sub['sugar']

        M[food] = sub
    return M
    """
