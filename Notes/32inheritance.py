# Inheritance Module

# Practice ;)

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Don Louis", 400)
e1.showDetails()
e2 = Programmer("Rishabh", 4100)
e2.showDetails()
e2.showLanguage()

Output:

The name of Employee: 400 is Don Louis
The name of Employee: 4100 is Rishabh
The default langauge is Python

## Updated Module

# Access Specifiers/Modifiers

'''
Modifiers in python programming are used to limit the access of a class variable 
and class methods outside of class while implementing the concepts of inheritance.
'''

# In python, there are three types of modifiers:

# 1. Public access modifier
# 2. Private access modifier
# 3. Protected access modifier

# Private Access Modifier Example

class Employee:
    def __init__(self):
        self.__name="Rishabh63"

a = Employee()
# print(a.__name)
# Cannot be accessed directly

print(a._Employee__name)
# Can be accessed directly

# Name Mangling Concept-

'''
Python uses name mangling to convert the name of a class variable or method to a unique name.
This is done to avoid naming conflicts with other variables or methods in the same class.
'''

class Employee:
    def __init__(self):
        self.__name="Rishabh63"

a = Employee()

print(a.__dir__())

# Protected Access Modifier

# Example-

class Employee:
    def __init__(self):
        self.__name="Rishabh63"
        self.__password="123456"

    def __str__(self):
        return f"Name: {self.__name}, Password: {self.__password}"

a = Employee()
print(a)

print(a.__dir__())