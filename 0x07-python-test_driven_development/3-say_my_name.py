#!/usr/bin/python3
"""
Basic printing, "coming up with tests is the main intention
"""


def say_my_name(first_name, last_name=""):
    """ prints the first and last natme
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("last_name must be a string"
                        if isinstance(first_name, str)
                        else "first_name must be a string")
    print("My name is", first_name, last_name)
