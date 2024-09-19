a = int(input("Enter Your Age: "))
print("your age is: ", a)

# Conditional Operators:-
# >, <, >=, <=, !=, ==

if (a>18): # Here indentation (Space) is important
    print("Yes")
    print("You can drive")
else:
    print("No")
    print("You can't drive")

# If a = 18
# print(a>18) # False
# print(a>=18) # True
# print(a==18) # True
# print(a!=18) # False

# Example:-

ApplePrice = 210
Budget = 200

if (ApplePrice <= Budget):
    print("You can buy apple")

else:
    print("You can't buy apple")

# Understanding Elif:-

num = int(input("Enter the value of your num: "))

if (num<0):
    print("num is negative")
elif (num==0):
    print("num is zero")
elif (num>0):
    if (num<=10):
        print("num is between 1 and 10")
    elif (num>10 and num<=20):
        print("num is between 11 and 20")
    else:
        print("num is greater than 20")
else:
    print("num is positive")

print("One of the conditions have been satisfied")


# If else in one line :-

# There is also a shorthand syntax for the if-else statement 
# that can be used when the condition being tested is simple and the code blocks to be executed are short. 
# Here's an example:

a = 2
b = 330
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Another example:

result = value_if_true if condition else value_if_false

# This syntax is equivalent to the following if-else statement:

if condition:
    result = value_if_true
else:
    result = value_if_false