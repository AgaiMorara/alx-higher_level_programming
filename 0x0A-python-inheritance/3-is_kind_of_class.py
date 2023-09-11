#!/usr/bin/python3
"""
checks if an object is an instance of , or inherits from
"""
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherits from, a specific class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or inherits from it

    Example:
        >>> class Parent:
        ...     pass
        >>> class Child(Parent):
        ...     pass
        >>> obj1 = Child()
        >>> obj2 = Parent()
        >>> is_kind_of_class(obj1, Child)
        True
        >>> is_kind_of_class(obj1, Parent)
        True
        >>> is_kind_of_class(obj2, Child)
        False
    """
    obj_class = type(obj)

    return issubclass(obj_class, a_class)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
