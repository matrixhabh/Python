# Functions is a block of code that performs a specific task.
# Types of functions are:

# 1. Built-in functions
# example of built-in functions: print, len, type
# 2. User-defined functions
# example of user-defined functions: calculategmean, isgreater, islesser


# SYNTAX:

def function_name(parameters):
    pass
     code and statements

# Simple function

def calculategmean(a,b): # this is a function definition
    gmean = (a*b)/(a+b)
    print(gmean)

def isgreater(a,b): # this is also a function definition
    if (a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

def islesser(a,b): # this is also a function definition
    pass # altho this function is not defined yet

a = 10
b = 5
gmean1 = (a*b)/(a+b)
print(gmean1)
calculategmean(a,b)

# # inluding more functions

if (a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")
isgreater(a,b)

c = 15
d = 3

gmean2 = (c*d)/(c+d)
print(gmean2)

calculategmean(c,d)

if (c>d):
    print("first number is greater")
else:
    print("second number is greater or equal")
isgreater(c,d)


# # Functons and Arguments


def average(a,b):
    print("The average is", (a+b)/2)

average(4, 6)


# # Types of Arguments


# # # Default Argument

'''
# We can provide a default value while creating a function.
# This way the function assumes a default value even 
# if a value is not provided in the function call for that argument.
'''

# # 1. Default Arguments example

def name(fname, mname = "John", lname = "Doe"):
    print("Hello", fname, mname, lname)

name("Amy", "Jacob", "Smith")


# # 2. Keyword Argument

'''
# We can provide arguments with key = value, 
# this way the interpreter recognizes the arguments by the parameter name. 
# Hence, the the order in which the arguments are passed does not matter.
'''

# #  Keyword Arguments example

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")


# # 3. Variable length Argument 

'''
# Sometimes we may need to pass more arguments than those defined in the actual function.
#  This can be done using variable-length arguments.
'''

# #Variable Length Arguments example

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")


# # 4. Required Argument

'''
# In case we don’t pass the arguments with a key = value syntax,
# then it is necessary to pass the arguments in the correct positional order
# and the number of arguments passed should match with actual function definition.
'''

# # Requried Argument example

def average(a, b, c=1):
    print("The average is", (a+b+c)/3)

average(5, 6)


# # Another case
def average(a=1, b=9):
    print("The average is", (a+b)/2)

average(5) # It shows the average of 5 and 9

def average(*numbers):
    print(type(numbers)) # <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average is", sum/len(numbers))
average(5, 6)

# Keyword Arbitrary Arguments

def name(**name):
    print(type(name)) # <class 'dict'>
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(fname = "James", mname = "Buchanan", lname = "Barnes")

# Importance of return function

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum / len(numbers) # if return is not used, the function will return None
        # if there are two return statements, 
        # the first return will be executed and the second return will not be executed

c = average(5, 6, 7, 1)
print(c)


# Module Updated

# Map, Filter & Reduce

'''
 In Python, the map, filter, and reduce functions are built-in functions that allow you to apply- 
 a function to a sequence of elements and return a new sequence. 
 These functions are known as higher-order functions, as they take other functions as arguments.
'''

# Old Fashioned ;)

def cube (x):
    return x*x*x

print(cube(5))

# Modern Fashioned :)

# map function
'''
The map function applies a function to each element in a sequence 
and returns a new sequence containing the transformed elements. 
The map function has the following syntax:
'''
map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument.
# The iterable argument can be a list, tuple, or any other iterable object.

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))

'''
In the above example, the lambda function lambda x: x * 2 is used to double each element in the numbers list.
The map function applies the lambda function to each element in the list 
and returns a new list containing the doubled numbers.
'''

# filter Function

'''
The filter function filters a sequence of elements based on a given predicate 
(a function that returns a boolean value) 
and returns a new sequence containing only the elements that meet the predicate. 
The filter function has the following syntax:
'''

filter(predicate, iterable)

# The predicate argument is a function that returns a boolean value 
# and is applied to each element in the iterable argument. 
# The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the filter function:

# List of numbers
numbers = [1, 2, 3, 4, 5]
# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)
# Print the even numbers
print(list(evens))

'''
In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers list 
and return only the even numbers. 
The filter function applies the lambda function to each element in the list 
and returns a new list containing only the even numbers.
'''

# reduce Function

'''
The reduce function is a higher-order function that applies a function to a sequence 
and returns a single value. It is a part of the functools module in Python and has the following syntax:
'''

reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a single value. 
# The iterable argument is a sequence of elements, such as a list or tuple.

# also

# The reduce function applies the function to the first two elements in the iterable 
# and then applies the function to the result and the next element, and so on. 
# The reduce function returns the final result.

# Here is an example of how to use the reduce function:

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)

'''
In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements
in the numbers list. The lambda function adds the two arguments x and y and returns the result. 
The reduce function applies the lambda function to the first two elements in the list (1 and 2), 
then applies the function to the result (3) and the next element (3), and so on. 
The final result is the sum of all the elements in the list, which is 15.
'''

'''
It is important to note that the reduce function requires the functools module 
to be imported in order to use it.
'''