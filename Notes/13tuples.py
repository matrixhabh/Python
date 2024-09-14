# Understanding Tuples


# Tuples are immutable
# Tuples are ordered
# Tuples are used to store multiple values
# Tuples are enclosed in parentheses
# Tuples can be used to return multiple values from a function
# Tuples can be unpacked into multiple variables
# Tuples can be used to store a collection of values

tup = (1, 2, 3)
print(type(tup), tup)

# altho
tup1 = (1)
print(type(tup1), tup1) # shows class as 'int'

# To not confuse tup with int

tup2 = (1,) # add a comma at the end ( Class 'Tuple')
print(type(tup2), tup2)
 
# Tuples are immutable as

# tup3 = (1, 2, 3)
# tup3[0] = 10
# print(tup3) # shows error

# To mutate a tuple we can use tuple unpacking
a, b, c = (1, 2, 3)
a = 10
print(a, b, c)

a, b, c = 1, 2, 3
a = 10
print(a, b, c)

a, b, c = 1, 2, 3
print(a, b, c)

# or change it into a list i.e.,

tup4 = [1, 2, 3, 4]
tup4[0] = 10
print(type(tup4), tup4) # shows class as 'list'

# Tuples csan store multiple values like

tup5 = (1, 2, 30, "Python", True, 10.5)
print(tup5)
print(tup5[0])
print(tup5[1])
print(tup5[3])
print(tup5[4])
print(tup5[5])
# Postitive and Negative Index are used in tuple too

# We can also use len() to find the length of a tuple
print(len(tup5)) # shows 6
 
# To check whether an item is present in a tuple or not 
if 10 in tup5:
    print("yes, 10 is present")
else:
    print("no, 10 is not present")

# We can slice a tuple too but a new tuple is created

tup6 = (1, 2, 3, 4, 5, 6, 7)
tup7 = tup6[1:4]
print(tup7)
# slicing is just like slicing a list
print(tup6[1:4:2]) # (2, 4)
print(tup6[:]) # (1, 2, 3, 4, 5, 6, 7)
print(tup6[1:]) # (2, 3, 4, 5, 6, 7)
print(tup6[:-1]) # (1, 2, 3, 4, 5, 6)


"""Operations on tuple"""


'''Manipulating Tuples'''
# ( Mostly to change a tuple we copy the tuple, change it to list,
#  make changes, and again make it a tuple)

countries1 = ("India", "China", "USA", "Russia", "UK")
countries2 = list(countries1)
countries2.append("Germany") # add item at last
countries2.pop(1)            # remove item at index 1
countries2[2] = "France"     # change item at index 2
print(countries2)

# We can also concatenate tuples

AR = ("AK47, M4A1, UMP45, Glock, Deagle,")
Sniper = (" AWP, Mosin-Nagant, USP-S")
Guns = AR + Sniper
print(Guns)

# Note: Classes are written as 'Tuple' and variables are usually written as 'tuple'

# Using count()

tup8 = (1, 2, 3, 3, 5, 6, 3, 7, 3)
res = tup8.count(3)
print('Count of 3 is:', res)

# Using index() to check the first occurence of an item

tup9 = (1, 2, 31, 3, 5, 6, 3, 7, 3)
res = tup9.index(3)
print('Index of 3 is:', res)

# We can also slice and use index()

tup10 = (1, 2, 31, 3, 5, 6, 3, 7, 3)
res = tup10.count(3)
print('Count of 3 is:', res)
res = tup10.index(3, 6, 8) # index of 3 , from 6th to 10th occurence
print('Index of 3 is:', res) # 6

# To check the length
res = print(len(tup10))