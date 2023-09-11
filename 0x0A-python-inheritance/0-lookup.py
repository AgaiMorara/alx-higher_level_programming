#!/usr/bin/python3
"""
defines a function that returns the list of available attributes and methods of
an object
"""

def lookup(obj):
    '''
    lookup : function that looks into the methods and attributes of an object
    args:
    obj (object): object to lookup
    Returns:
    A dictionary of namespace and methods
    '''

    return dir(obj)
