#!/usr/bin/python3
"""
baseGeometry with public instance method area... raises Exception if area
not implemented
"""


class BaseGeometry:
    """
    BaseGeometry has two methods now
    """

    def area(self):
        """ Calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks wether the passed arg is int """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
