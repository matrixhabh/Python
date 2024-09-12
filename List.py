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



# List Methods


# Using Append

lst = [1, 2, 3, 4, 5]
print(lst)
lst.append(6) # To add an item to the end of the list
print(lst)

# Using Sort

lst = [11, 3, 5, 1, 50]
lst.sort() # To sort the list in ascending order
print(lst)
# also
lst.sort(reverse=True) # To sort the list in descending order
print(lst)

# Using Index

lst3 = ['a', 'b', 'c', 'd', 'e', 'a', 'a']
print(lst3.index('c')) # To find the index of the first occurrence of the item
 
# Using Count

print(lst3.count('a')) # To count the number of occurrences of the item

# Usage of another list

lst4 = lst3
lst4[0] = 'z' # To change the first item of the list (example)
print(lst3)


lst4 = lst3.copy() # To copy the list
lst4[0] = 'z' # To change the first item of the list (example)
print(lst3)

# Using Insert

lst5 = ['a', 'b', 'c', 'd', 'e']
lst5.insert(2, 'z') # To insert an item at a specific index
print(lst5)

# Using Extend

l = [1, 2, 3]
lst5.extend(l)
print(lst5)

# To Concatenate lists

x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z)

# Using Remove

lst6 = ['a', 'b', 'c', 'd', 'e']
lst6.remove('c') # To remove an item from the list
print(lst6)

# Using Pop

lst7 = ['a', 'b', 'c', 'd', 'e']
item = lst7.pop() # To remove the last item from the list
print(lst7)
print(item)

# Using Clear

lst8 = ['a', 'b', 'c', 'd', 'e']
lst8.clear() # To remove all the items from the list
print(lst8)