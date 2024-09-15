##

for i in range(5):
    print(i)

else:
    print("Sorry no i") 

##

for i in []:
    print(i)

else:
    print("Sorry no i") # Output is Sorry no i because the list is empty


##

# for counter in sequence:
    #Statements inside for loop block
# else:
    #Statements inside else block

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


##

for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("Sorry no i") # here break function is used to exit the loop 
    # note that it does not break but exits the loop

## Using while loop with else

i = 0
while i<7:
    print(i)
    i = i+1
    # if i == 4:
    #     break   ## by using break function we can exit the loop

else:
    print("Sorry no i") # without break function we can use else block


# output
# iteration no 1 in for loop
# iteration no 2 in for loop
# iteration no 3 in for loop
# iteration no 4 in for loop
# iteration no 5 in for loop
# else block in loop
# Out of loop