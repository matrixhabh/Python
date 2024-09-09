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
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculategmean(a,b)

# inluding more functions

# if (a>b):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")
isgreater(a,b)

c = 15
d = 3

# gmean2 = (c*d)/(c+d)
# print(gmean2)

calculategmean(c,d)

# if (c>d):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")
isgreater(c,d)