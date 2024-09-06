# Integers in string

a = "1"

b = "2"

print(a + b)

# Output-> 12

a = "1"

b = "2"

print(int(a) + int(b))

# "Output-> 3"  is correct because int() function converts the string to integer
#                also noticing that the strings given are integers



# Types of Typecasting

# Explicit Tyoecasting
# Implicit Typecasting

"""

Explicit Typecasting is when we explicitly convert one data type to another data type (by user)
ex:- int(), float(), str(), hex(), oct(), etc.

"""
"""

Implicit Typecasting is when python convert one data type to another data type (by default)

"""
# ex(1):- python automatically converts a to integer
a = 1
print(type(a))
# output-> <class 'int'>

# ex(2):- python automatically converts b to float
b = 1.5
print(type(b))
# output-> <class 'float'>

# ex(3):- python automatically converts c to float as it is a float addition
c = 1.5 + 1
print(type(c))
# output-> <class 'float'>


string = "15"
number = 7
string_number = int(string)
# throws an error if the string is not a number
sum = string_number + number
print("The Sum of both the numbers is", sum)

"""

Taking user input in python:-

"""
a = input("Enter your name: ")
print("My name is", a)

x = input(("First number: "))
y = input(("Second number: "))
print(x + y) # lets say x=1 and y=2 then output here is-> 12 i.e., Concatenation of both the numbers
print(int(x) + int(y)) # output here is-> 3 i.e., Addition of both the numbers
