#!/usr/bin/python3
""" We further improve the square to include a method to calc area """


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

    def area(self):
        """
        Calculates the area of the square.
        Returns: The area of the square (an int).
        """
        return self.__size ** 2
