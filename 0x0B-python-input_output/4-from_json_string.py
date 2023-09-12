#!/usr/bin/python3
"""
implements from_json_string..
"""
import json


def from_json_string(my_str):
    """ parses a JSON string and returns a python data structure """
    return json.loads(my_str)
