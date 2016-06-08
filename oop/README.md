#Object-Oriented Programming

###Notes
Creating a class:
```python
class hi:
    def __init__(self):
        self.age = 16
        self.color = 'green'
    def change_color(self, new_color): # arg0 must be self
    	self.color = 'yellow'
```
Creating an object:
```python
jason = hi()
return jason.age # returns 16
jason.change_color('yellow')
return jason.color # returns 'yellow'
```
 
