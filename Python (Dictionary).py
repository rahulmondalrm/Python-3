Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dictionary in Python:
>>> d={'name':'Max','age':14,'year':2004}
>>> d
{'name': 'Max', 'age': 14, 'year': 2004}
>>> d['name']
'Max'
>>> d['age']
14
>>> d['year']
2004
>>> E={'name':'John',15:15,25.5:50.5,True:True,(5,2):6}
>>> e
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> E
{'name': 'John', 15: 15, 25.5: 50.5, True: True, (5, 2): 6}
>>> E[name]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    E[name]
NameError: name 'name' is not defined
>>> E['name']
'John'
>>> E[(5,2)]
6
>>> E[15]
15
>>> len(E)
5
>>> d['name']
'Max'
>>> d.get('name')
'Max'
>>> d.get('age'))
SyntaxError: unmatched ')'
>>> d.get('age')
14
>>> d
{'name': 'Max', 'age': 14, 'year': 2004}
>>> d['Surname']='Tesar'
>>> d
{'name': 'Max', 'age': 14, 'year': 2004, 'Surname': 'Tesar'}
>>> d.pop('Surname')
'Tesar'
>>> d
{'name': 'Max', 'age': 14, 'year': 2004}
>>> e
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> E
{'name': 'John', 15: 15, 25.5: 50.5, True: True, (5, 2): 6}
>>> E.clear()
>>> E
{}
>>> del E
>>> E
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    E
NameError: name 'E' is not defined
>>> d
{'name': 'Max', 'age': 14, 'year': 2004}
>>> d['name']='Raj'
>>> d
{'name': 'Raj', 'age': 14, 'year': 2004}
>>> d.update({'name':'Max'})
>>> d
{'name': 'Max', 'age': 14, 'year': 2004}
>>> d.keys()
dict_keys(['name', 'age', 'year'])
>>> d.values()
dict_values(['Max', 14, 2004])
>>> d.items()
dict_items([('name', 'Max'), ('age', 14), ('year', 2004)])
>>> d
{'name': 'Max', 'age': 14, 'year': 2004}
>>> d.popitem()
('year', 2004)
>>> d
{'name': 'Max', 'age': 14}
>>> 