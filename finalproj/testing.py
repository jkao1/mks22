import urllib

def b():
    url_nutr = 'http://www.starbucks.com/menu/catalog/nutrition?drink=espresso#view_control=nutrition'
    f = urllib.urlopen(url_nutr)
    s = f.read()
    table_loc = s.rfind('<table ')
