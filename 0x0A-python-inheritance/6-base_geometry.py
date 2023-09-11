#!/usr/bin/python3
"""
baseGeometry with public instance method area... raises Exception if area
not implemented
"""


class BaseGeometry:
    """
    BaseGeometry has one method area that raises a given exception
    """

    def area(self):
        raise Exception("area() is not implemented")
