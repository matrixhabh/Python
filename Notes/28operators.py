# In Python, is and == are both comparison operators that can be used to check if two values are equal.
# However, there are some important differences between the two that you should be aware of.

# for example

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

# In this case, a and b are two separate lists that have the same values, so == returns True.
# However, a and b are not the same object in memory, so is returns False.
'''
One important thing to note is that, in Python, strings and integers are immutable, 
which means that once they are created, their value cannot be changed.
This means that, for strings and integers, is and == will always return the same result:
'''
a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True

# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.

# For mutable objects such as lists and dictionaries, is and == can behave differently.
# In general, you should use == when you want to compare the values of two objects, 
# and use is when you want to check if two objects are the same object in memory.

# Walrus operator
'''
The Walrus Operator is a new addition to Python 3.8 
and allows you to assign a value to a variable within an expression. 
This can be useful when you need to use a value multiple times in a loop, 
but don't want to repeat the calculation.

The Walrus Operator is represented by the := syntax 
and can be used in a variety of contexts including while loops and if statements.
'''

# Example
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())

# Another

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

# In this example, the user input is assigned to the variable name using the Walrus Operator. 
# The value of name is then used in the if statement to determine whether it is in the names list. 
# If it is, the corresponding message is printed, otherwise, a different message is printed.