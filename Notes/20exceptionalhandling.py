a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")

for i in range(1, 11):
    print(f"{int(a)} X {int(a)} = {int(a)*(i)}")

# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
# Exception handling deals with these events to avoid the program or system crashing, 
# and without this process, exceptions would disrupt the normal operation of a program.

# Syntax

a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {int(a)} = {int(a)*i}")
except:
    print("Invalid Input")

print("End of line program")
print("Code ends")


# Another use:

try:
        num = int(input("Enter an integer: "))
except ValueError:
        print("Number entered is not an integer.")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
# Output: when entered '0' shows 6 when entered '1' shows 3
except ValueError:
    print("Entered value is not an integer: ")

except IndexError:
    print("Index Error")