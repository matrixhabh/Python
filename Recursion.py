# Recursion is the process if defining something in terms of itself.

# for example 
# factorial(5)= 5*4*3*2*1
# factorial(4)= 4*3*2*1
# factorial(3)= 3*2*1
# factorial(2)= 2*1
# factorial(1)= 1
# factorial(0)= 1

# So we can write this process as factorial(n) = n*factorial(n-1)
# This is recursion function

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print (factorial(3)) # 6
print (factorial(4)) # 24
print (factorial(5)) # 120

# So here we recalled the function in the same function but with different argument

# Fibonacci Sequence

# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# Fibonacci Sequence is a series of numbers in which each number is the sum of the two preceding numbers.
# Here is the syntax of the Fibonacci sequence:

n = (any integer)
def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(n))