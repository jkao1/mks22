import urllib

def jm():
    url = 'http://www.jambajuice.com/menu-and-nutrition/menu/freshly-squeezed-juice-shots'
    f = urllib.urlopen(url)
    s = f.read()

    l_start = s.find('<div class="mainbody menu menu_listing">')
    l_end = s.find('<section id="Footer1_',l_start)
    listing = s[l_start:l_end]
    listing = listing.split('<div class="updatePanel"')

    for i in range(1,len(listing)):
        output = listing[i]
        o_start = output.find('<tr class="table_line">')
        o_end = output.find('<div class="percentages clearfix">')
        output = output[o_start:o_end].replace('\r\n','')

        output = output.split('<td class="left_col"')
        output = output[1:3]+output[6:]
        M = {}
        for i in range(len(output)):
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
            M[title.lower()] = num
        del M['sugar']
        print M
