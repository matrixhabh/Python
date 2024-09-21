# example of importing a function

# import math
# math.(enter or choose a function)

import math

result = math.sqrt(16)
print(result)  # 4.0

# From Keyword

# We can also import specific functions from a module using the from keyword

from math import sqrt, pi

result = sqrt(16) * pi
print(result)  # 12.566

# Importing everything using the wildcard(*)

# However, this is generally not recommended as it can lead to confusion and 
# make it harder to understand where specific functions and variables are coming from.

from math import *

result = sqrt(16) * pi
print(result)  # 12.566

# The "as" keyword

# We can also rename the imported function or variable using the "as" keyword

from math import sqrt as s

result = s(16) * pi
print(result)  # 12.566

# also

import math as m ( here 'm'[an example] can also be used as a variable name )
result = m.sqrt(16) * m.pi
print(result)  # 12.566
 


# "The dir function"
# dir() function can be used to see the list of all the functions and variables in a module

print(dir(math))
# or
print(math.nan, type(math.nan))

# If we create a new file for example "rishabh.py"
# and create a function in it for example 

def welcome():
    print("Hey There")

    Rishabh = "Rizzler"
# and then we import it in the main file
from rishabh import welcome, Rishabh (or just use import *)
welcome()
print(Rishabh)
# we can see that the function and variable are imported
# and output is "Hey There" and "Rizzler"

# When assigning a name to rishabh.py file we can use the "as" keyword like this

# import rishabh as r
# r.welcome()
# print(r.Rishabh)
