#!/usr/bin/python3
"""This script prints the number and list of arguments passed via the command line."""

import sys

if __name__ == "__main__":
    number = len(sys.argv) - 1
    if number == 0:
        print(f"{number} arguments.")
    elif number == 1:
        print(f"{number} argument:\n1: {sys.argv[1]}")
    else:
        print(f"{number} arguments:")
        for index, string in enumerate(sys.argv[1:]):
            print(f"{index + 1}: {string}")
