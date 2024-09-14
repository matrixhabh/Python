
# Break Concept

i = 0
while i < 5:
    print(i)
    i += 1
    if (i == 3):
        break

for i in range(12):
    if (i == 10):
        break
    print("5 X", i+1, "=", 5 * (i+1))

print("Left the loop")

# Example of break

for i in range(1,101,1):
    print(i , end=" ")
    if(i==50):
        break

    else:
        print("Mississippi")
print("Thank You")


# Continue Concept

for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)
    

for i in range(2,3,4,6,8,0):
    if (i&2!=0):
        continue
    print(i)

# Do while loop examples (not really tho )


i = 0
while True:
    print(i)
    i = i + 1
    if (i%100 == 0):
        break

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break