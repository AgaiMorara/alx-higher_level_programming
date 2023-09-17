#!/usr/bin/python3
"""
Integer addition module... The start of test-driven development.
This module provides a function for adding two integers.

>>> add_integer(27, 74)
101
TypeError: Both 'a' and 'b' must be integers
>>> add_integer(2)
100
"""


def add_integer(a, b=98):
    '''
    Adds two integers and returns the result.

    Parameters:
    a (int/float): The first integer.
    b (int, optional): The second integer. Defaults to 98.

    Returns:
    int: The sum of the two integers.

    Raises:
    TypeError: If a or b is not an integer.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
