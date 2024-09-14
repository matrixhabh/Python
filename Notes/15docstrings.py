# Python docstrings are the string literals that appear right after -
# the definition of a function, method, class, or module.

def square(x): # Docstring is written write below the function
    '''Takes in a number x, Returns the square of x''' # This is a docstring (i.e., a special string)
    print(x**2) # Docstring is palced right above the function
square(5)
print(square.__doc__) # prints the docstring
 
# another example of docstring
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
print(add.__doc__)

# Difference between Docstring and Comments

# Comments are descriptions that help programmers better understand the intent -
# and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings are strings used right after the definition of a function, method, class, or module
# They are used to document our code.

# PEP 8
PEP 8 is a document that provides guidelines and best practices on how to write Python code.
It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
The primary focus of PEP 8 is to improve the readability and consistency of Python code.