Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
MATTHEW AU has a rating of 192.
MAXWELL IRIKURA has a rating of 53.
MAXWELL LIN has a rating of 83.
ERIK MAI has a rating of 21.
MATTHEW WONG has a rating of 162.


ERIK MAI has a rating of 21.
MATTHEW AU has a rating of 192.
MATTHEW WONG has a rating of 162.
MAXWELL IRIKURA has a rating of 53.
MAXWELL LIN has a rating of 83.
>>> set
<type 'set'>
>>> set()
set([])
>>> set([1])
set([1])
>>> set(1,1)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    set(1,1)
TypeError: set expected at most 1 arguments, got 2
>>> set([1,1])
set([1])
>>> set('asdfasdfasdf')
set(['a', 's', 'd', 'f'])
>>> ================================ RESTART ================================
>>> th()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    th()
NameError: name 'th' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/students/2018/jason.kao/public_html/Github/mks22/dict/mks22-dict_notes.py", line 32, in <module>
    f('last')
NameError: name 'f' is not defined
>>> th()
{' GPA': ' 4.87', ' Name': ' Peter', 'ID': 'B3', ' Age': ' 39'}
>>> th()
{' GPA': ' 4.87', ' Name': ' Peter', 'ID': 'B3', ' Age': ' 39'}
>>> a=['Jason',16,1]
>>> b=['Brian',15,2]
>>> keys=['Name','Age','Nose-size']
>>> da={}
>>> db={}
>>> for i in range(len(a)):
	da[keys[i]]=a[i]

	
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> for i in range(len(a)):
	da[keys[i]]=a[i]

	
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> for i in range(len(a)):
	db[keys[i]]=b[i]

	
>>> db
{'Nose-size': 2, 'Age': 15, 'Name': 'Brian'}
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> db
{'Nose-size': 2, 'Age': 15, 'Name': 'Brian'}
>>> M={]
SyntaxError: invalid syntax
>>> M=}{
	
SyntaxError: invalid syntax
>>> M={}
>>> M[da[0]]=da

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    M[da[0]]=da
KeyError: 0
>>> M[da['Name']]=da
>>> M[db['Name']]=db
>>> M
{'Brian': {'Nose-size': 2, 'Age': 15, 'Name': 'Brian'}, 'Jason': {'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}}
>>> da
{'Nose-size': 1, 'Age': 16, 'Name': 'Jason'}
>>> db
{'Nose-size': 2, 'Age': 15, 'Name': 'Brian'}
>>> 
