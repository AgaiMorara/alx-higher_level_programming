#!/usr/bin/python3
'''
Rectangle: based on 0-rectangle.py. Has private instance attributes width and h
Contains a method width(self) that retrieves the width, and a setter width(sel
Width must be an integer; otherwise, it raises a TypeError exception.
Width must be greater than or equal to 0; otherwise, it raises a ValueError exce
'''


class Rectangle:
    '''Rectangle class for representing rectangles'''

    def __init__(self, width=0, height=0):
        '''Initializes an instance of the Rectangle class.'''
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width attribute."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += '#' * self.__width + "\n"
        return string.rstrip("\n")

    def __repr__(self):
        """Returns a string representation of the rectangle for debugging."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Called when we want to delete the instance.'''
        print("Bye rectangle...")

