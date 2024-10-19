# Operator Overloading Module

'''
Operator Overloading is a feature in Python that allows developers to 
redefine the behavior of mathematical and comparison operators for custom data types. 
This means that you can use the standard mathematical operators (+, -, *, /, etc.) 
and comparison operators (>, <, ==, etc.) in your own classes
'''

# Why Operator Overloading is Important?

'''
Operator overloading allows you to create more readable and intuitive code. 
For instance, consider a custom class that represents a point in 2D space. 
You could define a method called 'add' to add two points together, 
but using the + operator makes the code more concise and readable:
'''

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6

# How to overload an operator in python-

# You can overload an operator in Python by defining special methods in your class. 
# These methods are identified by their names, which start and end with double underscores (__).

# + : __add__
# - : __sub__
# * : __mul__
# / : __truediv__
# < : __lt__
# > : __gt__
# == : __eq__

# For example, if you want to overload the + operator to add two instances of a custom class, 
# you would define the add method:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Practice ;)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius