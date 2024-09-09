name = 'Rishabh'
for i in name:
    print('i') # Output-> iiiiiii (veritcally)

name2 = 'Vishwajeet'
for i in name2:
    print(i) # Output-> vishwajeet (vertically)
    if (i =='s'):
      print("This is something special")

colors = ['red', 'green', 'blue']
for color in colors:
    print(color)
    for i in color: # Can use i or char in these cases
        print(i)

# Range Concept

for k in range(5):
    print(k) # Output-> 0 1 2 3 4

for k in range(5):
    print(k + 1) # Output-> 1 2 3 4 5

# also
for k in range(1, 6):
    print(k) # Output-> 1 2 3 4 5 range goes from 1 to 5 i.e., (n-1)

for k in range(1, 6, 2):
    print(k) # Output-> 1 3 5 range goes from 1 to 5 with (step 2)

# Nested Loops

for i in range(5):
    for j in range(5):
        print(i, j)
        if (i == j):
            print("This is something special")

# While Loop -> executes statements while condition is true
#               if the condition becomes false, loop stops (i.e., interpreter exits the loop)
i = 0
while i < 5:
    print(i)
    i += 1 # or i = i + 1

# Another example

i = int(input("Enter a number: "))
while i<=30:
    i = int(input("Enter a number again: "))
    print(i)

print("You entered a number greater than 30") 

# Decrementing while loop

count = 5
while (count > 0):
    print(count)
    count = count - 1 # or count -= 1 if you enter count = count + 1 it will run infinitely

# when while loop is executed, count becomes 0, so it stops
# so we can also use else here

else:
    print("I'm in else")




# extra info about do while loop ( not in ython)
do{
    # context;
}while(condition);

# here do while loop runs the program atleast once, whether the condition is true or false
# also line 49 to 52 is same as do while loop.