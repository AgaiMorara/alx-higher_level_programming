#!/usr/bin/python3
""" Here we access and update private instance attributes """


class Square:
    """
    Represents a square with a size attribute and an area method.

    Attributes:
        size (int): The size (side length) of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.
        Args:
            size (int, optional): The side length of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Gets the side length of the square
        Returns: The size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of the square
        Args:
            Value (int): The new size value
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns: The area of the square (an int).
        """
        return self.__size ** 2
