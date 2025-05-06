#!/usr/bin/python3
import sys
"""                                                                                                                                                                                                         
 This script finds the lenght of argv, and returns the output                                                                                                                                               
"""
number = len(sys.argv) - 1
if number == 1:
    print(f"{number} argument:\n1: {sys.argv[1]}")
elif number == 0:
    print(f"{number} arguments.")
else:
    print(f"{number} arguments:")
    for index, string in enumerate(sys.argv[1:]):
        print(f"{index + 1}: {string}")


