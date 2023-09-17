#!/usr/bin/python3
"""
prints a square
"""


def print_square(size):
    """ prints a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
