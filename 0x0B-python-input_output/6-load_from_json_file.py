#!/usr/bin/python3
"""
create an object from a "JSON file
"""
import json


def load_from_json_file(filename):
    """
    desirialize... (translate a json object to a python object
    """

    with open(filename) as f:
        return json.load(f)
