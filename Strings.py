'''
In python,
 Anything enclosed in single quotes ('example') or double quotes ("example") is a string.

 String is like an array of characters.

 Strings are immutable, which means that once a string is created, it cannot be changed.
 However, you can create a new string by concatenating two or more strings.



'''
speaker = '''He said "do you like phonk music"?
             I said:- ofcourse.'''

print(speaker)

# Simple string operation

name1 = 'Rishabh'
print("Hello", name1)

# Accessing characters of a string operation

name2 = 'Rishabh'
print(name2[0])
print(name2[1])
print(name2[2])
print(name2[3])
print(name2[4])
print(name2[5])
print(name2[6])
''' …also print(name[7]) throws an error as index is out of range '''

idea = 'break'
print(idea)


# Using for loop to print all characters of a string
# i.e., Loop through a string:

statement = 'Boku no namae wa "Rishabh" desu'
for character in statement:
    print(character)

# printing specific characters of a string

statement2 = 'Rishabh,Rudra'
print(statement2[0:7])

# Now, string slicing and operations on string

statement3 = 'Rishabh,Rudra'
print(len(statement3))



'''Usage'''
fruit = 'mango'
len1 = len(fruit)
print("Mango is a", len1, "letter word")

# Can also be written as
print("First four letters of mango are", fruit[:4]) # including 0 but not 4

# Also we can use it as
print("Middle letters of mango are", fruit[1:4]) # including 1 but not 4
# Above syntax can also be written as
print(fruit[-4:-1]) # "5-4=1":"5-1=4" 
# Although above syntax is not recommended
# And noting that
print(fruit[-1:-3]) # throws an error as index is out of range



# Strings as an array
'''A string is essentiallya sequenceof characters also known as array.'''