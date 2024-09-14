# Dictionaries Module

# Dictionaries are collection of data items.
# •They store multiple items in a single variable
# •Dictionary items are separated by commas and enclosed within curly brackets {}.
# •Dictionaries are unchangeable, meaning you cannot change items of the dictionary once created.
# •Dictionaries do not contain duplicate items.

# Creating Dictionary

dict = {
    "Rishabh": "Human Being",
    "Utensil": "Object",
}
print(dict["Rishabh"])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accesing Dictionary Items

info = {'name':'Rishabh', 'age':19, 'eligible':True}
print(info)
print(info['name'])
print(info['age'])
print(info['eligible'])
print(info.get('name')) # prints Rishabh too

# Accessing Keys and Values

print(info.keys()) # prints all keys
print(info.values()) # prints all values

# Note 
# print(info['name2']) # throws an error as name2 is not present in the dictionary
# Altho
# print(info.get('name2')) # prints None

for key in info.keys(): # here we can use iterate as
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")


# Dictionary Methods ( Dictionary from python 3.7 onwards is ordered )

# to update the dictionary
ep1 = {423: 39, 567: 89, 234: 56}
ep2 = {520: 70, 280: 40, 314: 69}
ep1.update(ep2)
print(ep1)

# to clear the dictionary
ep1 = {423: 39, 567: 89, 234: 56}
ep2 = {520: 70, 280: 40, 314: 69}

ep1.clear()
print(ep1)

# Creating Empty Dictionary
empt = {}
print(empt)

# Pop method is used to remove th ekey value-pair whose key is passed as a parameter

ep1 = {423: 39, 567: 89, 234: 56}
ep1.pop(423)
print(ep1)

# popitem() method is used to remove the key-value pair whose key is the last item in the dictionary

ep1 = {423: 39, 567: 89, 234: 56}
ep1.popitem()
print(ep1)

# Del can also be used to remove a dictionary item

ep1 = {423: 39, 567: 89, 234: 56}
del ep1[423]
print(ep1)

# Pretty much same as list, tuple, set.