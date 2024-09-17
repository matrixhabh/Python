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


# Finally Clause usage-

def func1():
    try:
        l = [1, 3, 5, 7]
        i = int(input("Enter the index: "))
        print(l[i]) # prints the index no.
        return 1 # returns 1 atlast if index entered is 0, 1, 2 or 3
    except:
        print("Invalid Index")
        return 0 # returns 0 atlast if index entered is greater than '3'

    finally: # very imp as it is printed doesn't matter if the syntax is correct or not

        print("I am always executed")

x = func1()
print(x)