#!/usr/bin/python3
"""
inheritance in action
"""

BaseGeometry  = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle is a subclass of BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self.__height = height
