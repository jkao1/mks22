

#def pm_html(): 
    output = """
    <form method="GET" action="2item_info.py">
        Do you want ...
        <select name="product_type">
            <option value="87-breakfast">Breakfast</option>
            <option value="lunch">Lunch</option>
            <option value="soups">Soups</option>
            <option value="drinks">Drinks</option>
            <option value="snacks">Snacks</option>
        </select><br>
        <input type="submit" name="Pret A Manger" value="Yes">
    </form>
    """

def pm_get(product_type):
    url = "www.pret.com/en-us/our-menu/"+product_type+".aspx"
    f = urllib.urlopen(url)
    s = f.read()
    t_start = s.rfind('<!-- filter results -->')
    t_end = s.find('</section>',t_start)
    return s#[t_start:t_end]

def pm_store(product_type):
    main = pm_get(product_type)
    main = main.split('<div class="textwrap">')
    return main
   
def pm_html(): #incomplete
    product_type = form.getvalue("product_type") 
    output = '<form method="GET" action="3result.py">'
    #for hot food, don't forget '685-pret's-hot-spinach-tomato-mac-%26-cheese' 
    if product_type == "lunch":
        output += """
        <p class="choose-item">Choose a lunch item:</p><br>
        <select name="item">
            <option>Sandwiches</option>
            <option>Baguettes</option>
            <option>Hot Food</option>
            <option>Wraps</option>
            <option>Salads</option>
        </select><br>
        """
    elif product_type == "soups":
        output += """
        <p class="choose-item">Choose a type of soup:</p><br>
        <select name="item">
            <option>Today's Soups</option>
            <option>All Soups</option>
        </select>
        """
    elif product_type == "snacks":
        output += """
        <p class="choose-item">Choose a type of snack:</p><br>
        <select name="item">
            <option value="129-pret-pots">Pret's Pots</option>
            <option value="74-treats-&-snacks">Treats</option>
            <option value="76-bakery">Bakery</option>
            <option value="77-fresh-fruit">Fresh Fruit</option>
        </select>
        """
    elif product_type == "drinks":
        output += """
        <p class="choose-item">Choose a type of snack:</p><br>
        <select name="item">
            <option value="124-organic-coffee">Organic Coffee</option>
            <option value="78-cold-drinks">Cold Drinks</option>
        </select>
        """
    else:
        output = pm_store(product_type)
        print "i still have to complete the pret store function"
        
    output += '<input type="hidden" name="product_type" value="'+product_type+'">'
    output += '<input type="submit" name="Pret A Manger" value="Submit"></form>'
    print output
