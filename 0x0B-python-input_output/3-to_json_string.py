#!/usr/bin/python3
"""
Function that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    lightweight representation of my_obj that is human redable... dumps att
    """
    return json.dumps(my_obj)
