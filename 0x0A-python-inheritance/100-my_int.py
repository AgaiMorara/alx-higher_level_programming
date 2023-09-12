class MyInt(int):
    """
    A rebellious integer class that inherits from int.

    negates equality.

    Examples:
    =======
    # Valid: MyInt instances with different values should return True for ==
    >>> a = MyInt(5)
    >>> b = MyInt(6)
    >>> a == b
    True

    # Valid: MyInt instances with different values should return False for !=
    >>> a = MyInt(5)
    >>> b = MyInt(6)
    >>> a != b
    False

    # Valid: MyInt instances with the same value should return False for ==
    >>> a = MyInt(5)
    >>> b = MyInt(5)
    >>> a == b
    False

    # Valid: MyInt instances with the same value should return True for !=
    >>> a = MyInt(5)
    >>> b = MyInt(5)
    >>> a != b
    True

    # Valid: MyInt instances with different types should return True for ==
    >>> a = MyInt(5)
    >>> b = 5
    >>> a == b
    True

    # Valid: MyInt instances with different types should return False for !=
    >>> a = MyInt(5)
    >>> b = 5
    >>> a != b
    False

    # Valid: MyInt instances with negative values should return True for ==
    >>> a = MyInt(-5)
    >>> b = MyInt(-5)
    >>> a == b
    True

    # Valid: MyInt instances with negative values should return False for !=
    >>> a = MyInt(-5)
    >>> b = MyInt(-5)
    >>> a != b
    False
    """

    def __eq__(self, other):
        """Override the == operator to return !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to return opposite."""
        return super().__eq__(other)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
