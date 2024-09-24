a = 1
a1 = 9
b = True
c = None
d = "Rishabh"
e = complex(8, 3)
f = float(3.14)
print(a)
print(b)
print(a + a1)
print(e)
print("This type of a is", type(a)) # output = int
print("This type of b is", type(b)) # output = bool
print("This type of c is", type(c)) # output = NoneType
print("This type of d is", type(d)) # output = str
print("This type of f is", type(f)) # output = float

'''
Data Types:-

1) Numeric Data: int,       float,      complex
                3,-8,0     3.14,0.0      8+3j

Text Data:    str,        bytes,       bytearray
             "Hello"     b"Hello"     bytearray(b"Hello")

Boolean Data: bool
              True,       False

None Data:    None
              NoneType

Sequence Data: list,      tuple,       range
               [1,2,3]   (1,2,3)      range(5)

Mapping Data: dict,       set
               {"a":1}   {1,2,3}

'''
# Arithmetic Operations:-

print(5+6) # output = 11
print(5-6) # output = 1
print(5*6) # output = 30
print(12/6) # output = 2
print(2**4) # output = 16
print(7%6) # output = 1
print(13//6) # output = 2



# After 26th part:-
# Concept of Global and Local variables

'''Global variables are defined outside of any function and can be accessed anywhere in the program.
Local variables are defined inside a function and can only be accessed inside that function.'''

x = 4 #global variable
print(x) # first print 

def hello():
    x = 5 #local variable
    print(f"The local x is {x}")
    print("Hello Rishabh")

print(f"The global x is {x}") # second print
hello() # calling the function, third print
x = 6
print(f"The global x is {x}") # fourth print

# Output
"""
4
The global x is 4
The local x is 5
Hello Rishabh
The global x is 6
"""

# Another example

# here the global variable x is updated to 7 and the local variable y is not updated:-

x = 10

def my_func():
    global x
    x = 7
    y = 8
    print(y)

my_func()
print(x)