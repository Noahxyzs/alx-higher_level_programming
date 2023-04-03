#!/usr/bin/python3

"""create a function that add two int"""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to intger before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-int or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))