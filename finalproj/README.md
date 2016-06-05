#final proj

###To-dos
- add units of measurement
- food
- html for pages
###Problems
- there is no nutrition sheet for Frappuccinos, Sodas 
- product_type="food" title always appears with "?foodZone=9999" at the end

###Notes
```html
<form method="POST" action="filename.py">
    ...
    <!--maintains a "session", keeps info for every individual-->
    <input type="hidden" name=id value="account">
</form>
```
###Submission
- mention that all info except titles ('frappuccino-blended-beverages') and nutrient categories ('calories','carbs') is taken from the Starbucks site. 
This includes formal titles,
- symbol for 'Crème' will not work. This is because python won't allow me to manipulate the actual string that contains it becuase there are 'Unspported characters in input'.