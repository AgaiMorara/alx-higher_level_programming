#!/usr/bin/python3
""" A subclass Square of baseclass Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass Square of the base class Rectangle.

    Attributes:
    __size (int): The size of the square.

    Methods:
    __init__(self, size): Initializes attributes of the square.
    area(self): Calculates the area of the square.
    __str__(self): Returns a string representation of the square.

    Examples:
    =======
    # Valid square
    >>> s = Square(5)
    >>> s.area()
    25

    # Invalid: Negative size
    >>> s = Square(-5)
    Traceback (most recent call last):
    ...
    ValueError: width must be greater than 0

    # Invalid: Zero size
    >>> s = Square(0)
    Traceback (most recent call last):
    ...
    ValueError: width must be greater than 0

    # Invalid: Non-integer size
    >>> s = Square(5.5)
    Traceback (most recent call last):
    ...
    TypeError: width must be an integer

    # Invalid: Extremely large size (MemoryError)
    >>> s = Square(10**1000)

    # Invalid: No argument provided
    >>> s = Square()
    Traceback (most recent call last):
    ...
    TypeError: Square.__init__() missing 1 required positional argument: 'size'
    """

    def __init__(self, size):
        """Initializes attributes of the square."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
