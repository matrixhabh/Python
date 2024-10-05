# Class & Objects

'''
A class is a blueprint or a template for creating objects, providing initial values for state 
(member variables or attributes), and implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.
'''

# Creating a class:- (using the class keyword)

class Details:
    name = "Rohan"
    age = 20

# Creating an Object:-

# Object is the instance of the class used to access the properties of the class 
# (Now lets create an object of the class)

obj1 = Details()

# Now we can print values-
# e.g.,

class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)

# output-

# Rohan
# 20

# Self Parameter

'''
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
'''
# It must be provided as the extra parameter inside the method definition.

# e.g.,

class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()

# Output-

# My name is Rohan and I'm 20 years old.

# Practice Code ;)

class Person:
  name = "Rishabh"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Rahul"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()

##

# Constructor 
# (a better method)
'''
A constructor is a special method in a class used to create and initialize an object of a class. 
There are different types of constructors. 
Constructor is invoked automatically when an object of a class is created.
'''
'''
A constructor is a unique function that gets called automatically when an object is created of a class. 
The main purpose of a constructor is to initialize or assign values to the data members of that class. 
It cannot return any value other than None.
'''

# Syntax of Constructor
def __init__(self):
	# initializations

# Types of Constructors in Python

# • Parameterized Constructor
# • Default Constructor

# (1) PC

# When the constructor accepts arguments along with self, it is known as parameterized constructor.

# These arguments can be used inside the class to assign the values to the data members.

# e.g.,

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

# Output 

# Crab belongs to the Crustaceans group.

# (2) DC

# When the constructor doesn't accept any arguments from the object and 
# has only one argument, self, in the constructor, it is known as a Default constructor.

# e.g.,

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()

# Output

animal Crab belongs to Crustaceans group

##

# Practice ;)

class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Rishabh", "Developer")
b = Person("Travis", "Head") 
a.info()
b.info()
# print(a.name)
# a.name = "Toliver"
# a.occ = "Head"
# a.info()