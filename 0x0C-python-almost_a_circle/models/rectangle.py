#!/usr/bin/python3
 """
Rectangle that inherits from  Base
"""
from .base import Base

class Rectangle(Base):
    """
    Implementation of the rectangle
    """

    def __init__ (self, width, height, x=0, y=0, id=None):
        """
        Initialization of the class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height of this rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        """Get the rectangle x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the rectangle x-co-ordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the rectangle Y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display by '#'s correspoinding to area."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
