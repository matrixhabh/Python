# Exercise 3:-

# create a program capable of displaying questions to the user like KBC
# Use List datatype to store the questions and their correct answers
# Display the final amount the player is taking home after playing the game
print()
print("Welcome to Kaun Banega Crorepati !\n") 
input("Press Enter to continue...\n")
print("Pehla Prashn Aapke Computer Screen Pe\n")
total = 0
print("Q-1. Who has more hitpoints ?\n")

print("A. Electro Dragon") 
print("B. Super Dragon")
print("C. Electro Titan")
print("D. Root Rider")

display = input("Enter your choice: (input a, b, c or d)\n")
if display == "a":
    print("Sorry, you have chosen Electro Dragon \nThe correct answer is C\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "b":
    print("Sorry, you have chosen Super Dragon \nThe correct answer is C\n'Well Tried'\n 'To The Next Question !'\n")
elif display == "c":
    print("Bingo!! You have chosen the correct answer \n And you have won Rs. 1000000 \n'To The Next Question !'\n")
    total = total + 1000000
elif display == "d":
    print("Sorry, you have chosen Root Rider \nThe correct answer is C\n 'Well Tried'\n 'To The Next Question !'\n")
else:
    print("Invalid input \n Please try again")
    loop = True


input("Press Enter to continue...\n")

print("Dusra Prashn Aapke Computer Screen Pe\n")

print("Q-2. Which troop has more housing space ?\n")

print("A. Electro Dragon")
print("B. Super Witch")
print("C. Root Rider")
print("D. Electro Titan")
display = input("Enter your choice: (input a, b, c or d)\n")  
if display == "a":
    print("Sorry, you have chosen Electro Dragon \n The correct answer is 'B'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "b":
    print("Bingo!! You have chosen the correct answer \n And you have won Rs. 2000000 \n'To The Next Question !'\n")
    total = total + 2000000
elif display == "c":
    print("Sorry, you have chosen Root Rider \nThe correct answer is 'B'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "d":
    print("Sorry, you have chosen Electro Titan \nThe correct answer is 'B'\n 'Well Tried'\n 'To The Next Question !'\n")
else:
    print("Invalid input \n Please try again")
    loop = True


input("Press Enter to continue...\n")

print("Teesra Prashn Aapke Computer Screen Pe\n")

print("Q-3. How much maximum loot bonus is recieved in Titan League I ?\n")

print("A. 1 550 (Dark Elixir), 225 000 (Gold), 225 000 (Elixir)")
print("B. 2 400 (Dark Elixir), 410 000 (Gold), 410 000 (Elixir)")
print("C. 2 400 (Dark Elixir), 420 000 (Gold), 420 000 (Elixir)")
print("D. 2 300 (Dark Elixir), 320 000 (Gold), 320 000 (Elixir)")
display = input("Enter your choice: (input a, b, c or d)\n")
if display == "a":
    print("Sorry, you have chosen 'A' \nThe correct answer is 'D'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "b":
    print("Sorry, you have chosen 'B' \nThe correct answer is 'D'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "c":
    print("Sorry, you have chosen 'C' \nThe correct answer is 'D'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "d":
    print("Bingo!! You have chosen the correct answer \n And you have won Rs. 3000000 \n'To The Next Question !'\n")
    total = total + 3000000
else:
    print("Invalid input \n Please try again")
    loop = True


input("Press Enter to continue...\n")

print("Chautha Prashn Aapke Computer Screen Pe\n")

print("Q-4. How much maximum loot bonus is recieved in Titan League I ?\n")

print("A. 1 550 (Dark Elixir), 225 000 (Gold), 225 000 (Elixir)")
print("B. 2 400 (Dark Elixir), 410 000 (Gold), 410 000 (Elixir)")
print("C. 2 400 (Dark Elixir), 420 000 (Gold), 420 000 (Elixir)")
print("D. 2 300 (Dark Elixir), 320 000 (Gold), 320 000 (Elixir)")
display = input("Enter your choice: (input a, b, c or d)\n")
if display == "a":
    print("Sorry, you have chosen 'A' \nThe correct answer is 'D'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "b":
    print("Sorry, you have chosen 'B' \nThe correct answer is 'D'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "c":
    print("Sorry, you have chosen 'C' \nThe correct answer is 'D'\n 'Well Tried'\n 'To The Next Question !'\n")
elif display == "d":
    print("Bingo!! You have chosen the correct answer \n And you have won Rs. 4000000 \n'To The Next Question !'\n")
    total = total + 4000000
else:
    print("invalid input")
    loop = True

input("Press Enter to continue...\n")

print("Pachva Aur Aakhri Prashn Aapke Computer Screen Pe\n")

print("Q-5. What is the total troop capacity at TH-16 ?\n")

print("A. 320")
print("B. 340")
print("C. 360")
print("D. 300")
display = input("Enter your choice: (input a, b, c or d)\n")
if display == "a":
    print("Bingo!! You have chosen the correct answer \n And you ahve won Rs. 5000000 \n 'Thank You For Playing !'\n")
    total = total + 5000000
elif display == "b":
    print("Sorry, you have chosen 'B' \nThe correct answer is 'A'\n 'Well Tried'\n 'Thank You For Playing!'\n")
elif display == "c":
    print("Sorry, you have chosen 'C' \n The correct answer is 'A'\n 'Well Tried'\n 'Thank You For Playing!'\n")
elif display == "d":
    print("Sorry, you have chosen 'D' \n The correct answer is 'A'\n 'Well Tried'\n 'Thank You For Playing!'\n")
else:
    print("invalid input")
    loop = True


print("Your Total Earning Is = ", total)
print("Hope You Have Enjoyed The Game !")