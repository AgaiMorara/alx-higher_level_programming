#!/usr/bin/python3
"""
A restricted class for memory optimization.
"""

class LockedClass:
    """
    This class defines a restricted class using __slots__ for memory optimization.

    Attributes:
        first_name (str): A string representing the first name of an object.
    """
    __slots__ = ['first_name']

