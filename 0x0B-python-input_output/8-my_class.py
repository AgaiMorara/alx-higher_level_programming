#!/usr/bin/python3
"""My class Module
"""

class MyClass:
    """My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:}".format(self.name, self.number)
    
