# Lists
'''lists are a collection of data items'''
'''they store multiple items in a single variable'''
'''lists items are separated by commas and enclosed in square brackets'''
'''lists can be modified by adding, removing, or changing items'''

# Syntax
# list_name = [item1, item2, item3, ...]

# Creating a list
# list_name = []

# Accessing items in a list
# list_name[index]

# Modifying items in a list
# list_name[index] = new_item

# Appending items to a list
# list_name.append(new_item)

# Removing items from a list
# list_name.remove(item)

# Sorting a list
# list_name.sort()

# Reversing a list
# list_name.reverse()

# Length of a list
# len(list_name)



marks = [1, 2, 3, 4, 5]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# IndexError: list index out of range

# We can also include Strings and Booleans in a list
list = ["Python", True, 10, 20.5]
print(list)


# List Index

names = ["John", "Amy", "Jacob", "Peter"]
#         [0]     [1]     [2]      [3]

# Remember that the index starts from 0 altho list items are numbered from 1
# Also that index and length of a list are not the same

# Ways to access items in a list

emoji = ["Happy", "Sad", "Cherish", "Smile"]
print(emoji[3])
print(emoji[-1]) # Negative Index
print(emoji[len(emoji)-1])
print(emoji[4-1])

 # check whether an item is present in a list or not

if "Joy" in emoji: # because joy as an integer is present
    print("yes")
else:
    print("no")

# Same thing applies for strings
if "Ha" in "Happy":
    print("yes")

# printing can be used as

print(emoji)
print(emoji[:])
print(emoji[1:]) # slicing # can also be written as emoji[1:len(emoji)]
print(emoji[:-1]) # slicing
print(emoji[1:3:2]) # Output is [Sad, Cherish]

# Example: printing every 3rd consecutive value withing a given range

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

# List Comprehension

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)