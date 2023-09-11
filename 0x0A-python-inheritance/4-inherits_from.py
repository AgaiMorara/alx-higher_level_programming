#!/usr/bin/python3

""" inheritance """


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits (directly or
    indirectly from a class

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of a class that inherits
    from `a_class`, False otherwise.

    Example:
        >>> class Grandparent:
        ...     pass
        >>> class Parent(Grandparent):
        ...     pass
        >>> class Child(Parent):
        ...     pass
        >>> obj1 = Child()
        >>> obj2 = Parent()
        >>> obj3 = Grandparent()
        >>> inherits_from(obj1, Child)
        True
        >>> inherits_from(obj1, Parent)
        True
        >>> inherits_from(obj1, Grandparent)
        True
        >>> inherits_from(obj2, Child)
        False
    """
    myobject = type(obj)
    return issubclass(myobject, a_class) and myobject != a_class


if __name__ == "main":
    import doctest
    doctest.testmod()
