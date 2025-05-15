#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a square shape with a given size and position.
It provides methods for calculating the area and printing the square
using the `#` symbol, taking the position into account.
"""


class Square:
    """
    Represents a square with a size and a position.

    Attributes:
        __size (int): The length of the square's side.
        __position (tuple): The (x, y) position to print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
            position (tuple, optional): The position as a tuple (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The (x, y) position used when printing the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(val, int) and val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the `#` symbol, taking the position into account.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        print('\n' * self.__position[1], end="")
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
