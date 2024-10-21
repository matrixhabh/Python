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

#

## Single Inheritance Module

'''
Single inheritance is a type of inheritance where a class inherits properties 
and behaviors from a single parent class. This is the simplest and most common form of inheritance.
'''

# Syntax-
class ChildClass(ParentClass):
    # class body

# A Simple Example-
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

# If we want to create a new class for a specific type of animal, such as a dog, 
# we can create a new class named "Dog" that inherits from the Animal class.
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

# Practice ;)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")

d = Cat("Cat", "Catwoman")
d.make_sound()

a = Animal("Cat", "Cat")
a.make_sound()

#

## Multiple Inheritnace Module

'''
Multiple inheritance is a powerful feature in object-oriented programming 
that allows a class to inherit attributes and methods from multiple parent classes. 
This can be useful in situations where a class needs to inherit functionality from multiple sources.
'''

# Syntax-

# In Python, multiple inheritance is implemented by specifying multiple parent classes 
# in the class definition, separated by commas.

class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body

# Proper Example=
'''
It's important to note that, in case of multiple inheritance, 
Python follows a method resolution order (MRO) to resolve conflicts between 
methods or attributes from different parent classes. 
The MRO determines the order in which parent classes are searched for attributes and methods.
'''
# i.e.,
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

# In this example, the Dog class inherits from both the Animal and Mammal classes, 
# so it can use attributes and methods from both parent classes.

# Practice ;)

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivansh")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())

#

## Multilevel Inheritance Module

'''
Multilevel inheritance is a type of inheritance in object-oriented programming 
where a derived class inherits from another derived class. 
This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, 
leading to a more specialized class.
'''

# Syntax-
class BaseClass:
    # Base class code
    
class DerivedClass1(BaseClass):
    # Derived class 1 code
    
class DerivedClass2(DerivedClass1):
    # Derived class 2 code

# In Python, multilevel inheritance is achieved by using the class hierarchy

# Proper Example-

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
'''
In this example, we have three classes: Animal, Dog, and GoldenRetriever. 
The Dog class inherits from the Animal class, and the GoldenRetriever class inherits from the Dog class.
'''
'''
Now, when we create an object of the GoldenRetriever class, 
it has access to all the attributes and methods of the Animal class and the Dog class. 
We can also see that the GoldenRetriever class has its own attributes 
and methods that are specific to the class.
'''
# i.e.,
dog = GoldenRetriever("Max", "Golden")
dog.show_details()

# Output-

# Name: Max
# Species: Dog
# Breed: Golden Retriever
# Color: Golden

# Practice ;)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

'''
In conclusion, multilevel inheritance is a powerful feature in object-oriented programming 
that allows you to create complex and intricate classes by building upon existing ones. 
It provides the benefits of code reuse, maintainability, and readability, 
while also requiring careful consideration to avoid potential problems.
'''