# Super Keyword in Python

'''
The super() keyword in Python is used to refer to the parent class. 
It is especially useful when a class inherits from multiple parent classes 
and you want to call a method from one of the parent classes.
'''
# Note
'''
When a class inherits from a parent class, it can override or 
extend the methods defined in the parent class.
However, sometimes you might want to use the parent class method in the child class. 
This is where the super() keyword comes in handy.
'''
# Example:

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("Rishabh")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()

# Practice ;)

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rishabh = Employee("Rishabh Y", "6996")
henry = Programmer("henry", "4389", "Python")
print(henry.name)
print(henry.id)
print(henry.lang)

# In conclusion, the super() keyword is a useful tool in Python 
# when you want to call a parent class method in a child class. 
# It can be used in inheritance scenarios with a single parent class or multiple parent classes.