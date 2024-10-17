# dir(), __dict__ and help() methods in python

## dir() method
'''
The dir() function returns a list of all the attributes 
and methods (including dunder methods) available for an object. 
It is a useful tool for discovering what you can do with an object.
'''
# example-
>>> x = [1, 2, 3]
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

## The __dict__ attribute
'''
The __dict__ attribute returns a dictionary representation of an object's attributes. 
It is a useful tool for introspection.
'''
# example-

>>> class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...
>>> p = Person("Rishabh", 24)
>>> p.__dict__

# Output-

# {'name': 'Rishabh', 'age': 24}

## The help() mehthod
'''
The help() function is used to get help documentation for an object,
 including a description of its attributes and methods.
'''
# example-
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.


# Practice ;)

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("Rishabh", 24)
print(p.__dict__)

print(help(Person))

# In conclusion, dir(), dict, and help() are useful built-in functions 
# in Python that can be used to get information about objects. 
# They are valuable tools for introspection and discovery.


## 
# Magic Dunder Methods in Python-

class Employee:
  name = "Rishabh"
  def __len__(self):
    i = 0

    for c in self.name:
        i = i + 1
    return i

e = Employee()
print(e.name)
print(len(e))

# This is called Magic Method ;)

# Context-

# __init__ method
'''
The init method is a special method that is automatically invoked when you create a new instance of a class. 
This method is responsible for setting up the object’s initial state, 
and it is where you would typically define any instance variables that you need. 
Also called "constructor"
'''

# __str__ and __repr__ methods
'''
The str and repr methods are both used to convert an object to a string representation. 
The str method is used when you want to print out an object,
while the repr method is used when you want to get a string representation of 
an object that can be used to recreate the object.
'''

# __len__ method-
'''
The len method is used to get the length of an object. 
This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
'''

# __call__ method-
'''
The call method is used to make an object callable, 
meaning that you can pass it as a parameter to a function and it will be executed when the function is called.
This is an incredibly powerful tool that allows you to create objects that behave like functions.
'''

# These are just a few of the many magic methods available in Python.

# in main.py file:-
from emp import Employee

e = Employee("Harry")
print(str(e))
print(repr(e))
# print(e.name)
# print(len(e))
e()

# in emp.py file:-
class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):
    print("Hey I am good")