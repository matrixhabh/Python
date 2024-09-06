'''
EXAMPLE

x = 20
y = 10
ans1 = x + y
print("Addition of ", x, "and", y, "is", ans1)
ans2 = x - y
print("Subtraction of ", x, "and", y, "is", ans2)
ans3 = x * y
print("Multiplication of ", x, "and", y, "is", ans3)
ans4 = x / y
print("Division of ", x, "and", y, "is", ans4)
ans5 = x // y
print("Modulus of ", x, "and", y, "is", ans5)
ans6 = x ** y
print("Exponentiation of ", x, "and", y, "is", ans6)
ans7 = x % y
print("Reaminder of ", x, "and", y, "is", ans7)

'''
# Code :-


Number1 = int(input("Enter the first number:= "))
Number2 = int(input("Enter the second number:= "))

add = Number1 + Number2

print("Addition of", Number1, "and", Number2, "is", add)

sub = Number1 - Number2

print("Subtraction of", Number1, "and", Number2, "is", sub)

mul = Number1 * Number2

print("Multiplication of", Number1, "and", Number2, "is", mul)

div = Number1 / Number2

print("Division of", Number1, "and", Number2, "is", div)

mod = Number1 % Number2

print("Modulus of", Number1, "and", Number2, "is", mod)

power = Number1 ** Number2

print("Exponentiation of",Number1, "and", Number2, "is", power)

flr = Number1 // Number2

print("Floor Division of", Number1, "and", Number2, "is", flr)



# Calc using Typecasting functions



a = input("Enter first number: ")
b = input("Enter second number: ")

x = (int(a) + int(b))
print("The sum of both the numbers is", x)

x = (int(a) - int(b))
print("The difference of both the numbers is", x)

x = (int(a) * int(b))
print("The product of both the numbers is", x)

x = (int(a) / int(b))
print("The quotient of both the numbers is", x)

x = (int(a) % int(b))
print("The remainder of both the numbers is", x)

x = (int(a) ** int(b))
print("The power of both the numbers is", x)

x = (int(a) // int(b))
print("The floor division of both the numbers is", x)