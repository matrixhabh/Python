# Sets Module

# Sets are unordered collection of data items.
# •They store multiple items in a single variable
# •Set items are separated by commas and enclosed within curly brackets {}.
# •Sets are unchangeable, meaning you cannot change items of the set once created.
# •Sets do not contain duplicate items.

s = {2, 3, 2 ,4}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

# Output: {False, 19, 5.9, 'Carla'}
# Remember that sets are unordered, so the order of the items in the set is not guaranteed.

# Important:
# To create an empty set-

romeo = set()
print(type(romeo)) # <class 'set'>

# Common Mistake: (While creating an empty set)

romeo = {}
print(type(romeo)) # <class 'dict'>

# Accessing Set Items 

for value in info:
    print(value)

# Union() and Update()

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2) # s3 = {1, 2, 3, 4, 5}
print(s3) 
# Also we can use update() method
s1.update(s2)
print(s1) # {1, 2, 3, 4, 5}

cities = {"New York", "London", "Paris", "Tokyo"}
cities2 = {"Paris", "London", "Berlin"}
cities3 = cities.union(cities2)
print(cities3) # {'New York', 'London', 'Paris', 'Tokyo', 'Berlin'}


# intersection() and intersection_update() in sets


# Also we can use intersection() method using update() method
cities.intersection_update(cities2)
print(cities) # {'Paris', 'London'}


# Symmetric difference in sets


countries = {"India", "USA", "UK", "Germany"}
countries2 = {"USA", "Africa", "China", "UK"}
countries3 =countries.symmetric_difference(countries2)
print(countries3)


# Difference()  and difference_update() in sets

#  The difference() method returns a new set whereas
#  difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "London", "Paris", "Kashi"}
cities2 = {"Paris", "London", "Tokyo"}
cities3 = cities.difference(cities2)
print("My Favourite City Is:", cities3)


# isdisjoint() in sets

# The isdisjoint() method checks if items of given set are present in another set. 
# This method returns False if items are present, else it returns True.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))  # False ( Tokyo is present in both sets)


# issubset() in 

# The issubset() method checks if all the items of the original set are present in the particular set. 
# It returns True if all the items are present, else it returns False.


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Kabul", "Seoul"}
cities3 = cities2.issubset(cities)
print(cities3) # False ( Kabul and Seoul is not present in the original set)


# issupperset() in sets

# The issuperset() method checks if all the items of a particular set are present in the original set. 
# It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2)) # False ( Seoul and Kabul is not present in the original set)
cities3 = {"Tokyo", "Madrid","Delhi"}
print(cities.issuperset(cities3)) # True ( All the items are present in the original set)
# Vice Versa
print(cities3.issubset(cities)) # True ( All the items are present in the original set)


# add() method ( if want to add items to the set)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Paris")
print(cities) # {'Tokyo', 'Madrid', 'Berlin', 'Delhi', 'Paris'}


# update() method ( if you want to add more than one item to the set)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities) # {'Tokyo', 'Madrid', 'Berlin', 'Delhi', 'Helsinki', 'Warsaw', 'Seoul'}


# remove()/discard() method ( if you want to remove items from the set)

# The main difference between remove and discard is that, 
# if we try to delete an item which is not present in set, then remove() raises an error, 
# whereas discard() does not raise any error.


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo2")
# print(cities) # shows error 
# ( remove is mostly used to show error in programs in various conditions)

cities.discard("Tokyo2")
print(cities) # {'Madrid', 'Berlin', 'Delhi'}


# pop() method 

# This method removes the last item of the set 
# but the catch is that we don’t know which item gets popped as sets are unordered. 
# However, you can access the popped item if you assign the pop() method to a variable.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item) 

# del (del is not a method, rather it is a keyword which deletes the set entirely.

# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities1
# print(cities1) # Output: Syntax error.

# What if we don’t want to delete the entire set, we just want to delete all items within that set?


# clear() This method clears all items in the set and prints an empty set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities) # Output: set()

# we can also check if item exists or not

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.") # Output: Carla is present