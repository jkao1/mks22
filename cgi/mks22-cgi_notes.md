#CGI Notes

###urllib usage
```python
>>> import urllib
>>> f=urllib.urlopen('http://www.micromind.com/stuy'_
>>> s=f.read()
```

###Forms Interaction
```html
<input type="text" name="fred">
<input type="submit" name="button" value="ON">
```
- name = back-end var
- value = what shows up by default in textbox, can be the back-end var name if value is on a button
- buttons need name/values to be differentiated in your program
