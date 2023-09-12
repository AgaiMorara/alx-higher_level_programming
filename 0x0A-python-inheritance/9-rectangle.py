#!/usr/bin/python3
"""
Full Rectangle... implements the area method
"""
BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle sub class with correct area implementation.

    Examples:
    =======
    # Valid rectangle
    >>> r = Rectangle(5, 4)
    >>> r.area()
    20

    # Invalid: Negative width
    >>> r = Rectangle(-5, 4)
    Traceback (most recent call last):
        ...
    ValueError: width must be greater than 0

    # Invalid: Zero height
    >>> r = Rectangle(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: height must be greater than 0

    # Invalid: Non-integer width
    >>> r = Rectangle(5.5, 4)
    Traceback (most recent call last):
        ...
    TypeError: width must be an integer

    # Invalid: Extremely large width (MemoryError)
    >>> r = Rectangle(10**1000, 4)

    # Invalid: No arguments provided
    """

    def __init__(self, width, height):
        """The super function to call the class initialization."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Magic string, for non-formal format specification."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
