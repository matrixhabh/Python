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

# Now, "String Slicing and Operations" on string

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
print(fruit[-4:len(fruit) - 1]) # "5-4=1":"5-1=4" 
# Although above syntax is not recommended
# And noting that
print(fruit[-1:-3]) # throws an error as index is out of range



# Strings as an array
'''A string is essentially a sequence of characters also known as array.'''

# Quick Recap:-
name = 'Rishabh'
print(name[-6:-1]) # output = ?



# "More Methods" of how to use strings

a = 'Rishabh !!!'
print(len(a))               # => 11
print(a.find('i'))          # => 1
print(a.upper())            # => RISHABH !!!
print(a.lower())            # => rishabh !!!
print(a.replace('i', 'e'))  # => Reshabh !!!
print(a.rstrip("!"))        # => Rishabh
print(a.split(' '))         # => ['Rishabh', '!!!']

ytube = 'lone wolf'
print(ytube.capitalize()) # capitalize turns first letter to capital and rest to small

str1 = 'hey !!!'
print(len(str1))                # => 7
print(len(str1.center(14)))     # => 14
print(str1.endswith('!!!'))     # => True
print(str1.endswith('y', 1, 3)) # => True

# Note:- 
print(str1.find('yhh')) # find returns -1 as 'yhh' is not present in 'hey !!!'
# print(str1.index('yhh')) # index throws an error as 'yhh' is not present in 'hey !!!'

str2 = 'Hello'
print(str2.isalnum())

str3 = 'Hello World00' # condition for isalpha() -> A-Z, a-z and no punctuations or numbers(0-9)
print(str3.isalpha()) # shows False becoz it contains '00' which is not alphabet

str4 = 'hello world'
print(str4.islower()) # shows True as it contains only lower case alphabets

str5 = "We wish you a Merry Christmas"
print(str5.isprintable()) # shows True as it contains printable characters
str6 = "We wish you a Merry Christmas\n"
print(str6.isprintable()) # shows False as it contains non-printable elements

str7 = "     "
print(str7.isspace()) # shows True as it contains only spaces (by space bar)
str8 = "     "
print(str8.isspace()) # shows False as it contains only spaces (by tab bar)

str9 = "World Health Organization"
print(str9.istitle()) # shows True as it contains first letters of every word in capital

str10 = "To kill a Mockingbird"
print(str10.istitle()) # shows False as it contains first letters in small

str11 = "Python is a interpreted language"
print(str11.startswith('Python')) # shows True as it starts with 'Python'
print(str11.swapcase()) # shows pTHON IS A INTERPRETED LANGUAGE

str12 = "Python is a interpreted language"
print(str12.title()) # shows Python Is A Interpreted Language