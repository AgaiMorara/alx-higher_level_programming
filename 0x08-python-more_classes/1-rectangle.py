#!/usr/bin/python3
'''
Rectangle: based on 0-rectangle.py.. Has private instance attributes width.
contains a method width(self) - that retrieves it... and a setter width (self,
value) that sets it.
Width must be an integer, otherwise raises a TypeError exception
width must be an integer.
'''


class Rectangle:
    ''' width and height here comply with assertions'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
