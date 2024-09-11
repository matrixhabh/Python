# Functions is a block of code that performs a specific task.
# Types of functions are:

# 1. Built-in functions
# example of built-in functions: print, len, type
# 2. User-defined functions
# example of user-defined functions: calculategmean, isgreater, islesser


# SYNTAX:

# def function_name(parameters):
    # pass
     # code and statements

# Simple function

# def calculategmean(a,b): # this is a function definition
#     gmean = (a*b)/(a+b)
#     print(gmean)

# def isgreater(a,b): # this is also a function definition
#     if (a>b):
#         print("first number is greater")
#     else:
#         print("second number is greater or equal")

# def islesser(a,b): # this is also a function definition
#     pass # altho this function is not defined yet

# a = 10
# b = 5
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# calculategmean(a,b)

# # inluding more functions

# # if (a>b):
# #     print("first number is greater")
# # else:
# #     print("second number is greater or equal")
# isgreater(a,b)

# c = 15
# d = 3

# # gmean2 = (c*d)/(c+d)
# # print(gmean2)

# calculategmean(c,d)

# # if (c>d):
# #     print("first number is greater")
# # else:
# #     print("second number is greater or equal")
# isgreater(c,d)


# # Functons and Arguments


# def average(a,b):
#     print("The average is", (a+b)/2)

# average(4, 6)

# # Types of Arguments

# # # Default Argument
# '''
# We can provide a default value while creating a function.
# This way the function assumes a default value even 
# if a value is not provided in the function call for that argument.
# '''
# # 1. Default Arguments example

# def name(fname, mname = "John", lname = "Doe"):
#     print("Hello", fname, mname, lname)

# name("Amy", "Jacob", "Smith")


# # 2. Keyword Argument
# '''
# We can provide arguments with key = value, 
# this way the interpreter recognizes the arguments by the parameter name. 
# Hence, the the order in which the arguments are passed does not matter.
# '''
# #  Keyword Arguments example

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")


# # 3. Variable length Argument 
# '''
# Sometimes we may need to pass more arguments than those defined in the actual function.
#  This can be done using variable-length arguments.
# '''
# #Variable Length Arguments example

# def name(*name):
#     print("Hello,", name[0], name[1], name[2])

# name("James", "Buchanan", "Barnes")

# # 4. Required Argument
# '''
# In case we don’t pass the arguments with a key = value syntax,
# then it is necessary to pass the arguments in the correct positional order
# and the number of arguments passed should match with actual function definition.
# '''
# # Requried Argument example

# def average(a, b, c=1):
#     print("The average is", (a+b+c)/3)

# average(5, 6)


# # Another case
# def average(a=1, b=9):
#     print("The average is", (a+b)/2)

# average(5) # It shows the average of 5 and 9

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
