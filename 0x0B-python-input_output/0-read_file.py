#!/usr/bin/python3
"""
Practice reading from files using open and stream object attributes
"""


def read_file(filename=""):
    """open a file in r mode and read its contents: Read attribute"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
