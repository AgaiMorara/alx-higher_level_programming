#!/usr/bin/python3
'''
isinstance or not
'''
def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class`, False otherwise.

    Example:
        >>> is_same_class(5, int)
        True
        >>> is_same_class("hello", int)
        False
    """
    return isinstance(obj, a_class)
