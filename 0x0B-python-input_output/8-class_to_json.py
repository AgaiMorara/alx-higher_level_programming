#!/usr/bin/python3
"""
defination of a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean for json
serialization)
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for json serialization
    of an object
    """
    return obj.__dict__
