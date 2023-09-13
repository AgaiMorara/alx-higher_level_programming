#!/usr/bin/python3
"""
Writes a class that defines a student
"""


class Student:
    """ Here are the fields of students
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student
        Args:
        first_name (str): self_explanatory
        last_name (str): self explanatory
        age (int): today - dob
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a student instance
        and returns it.
        """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            are_all_strings = all(isinstance(attr, str) for attr in attrs)
            if are_all_strings:
                return {h: getattr(self, h) for h in attrs if hasattr(self, h)}
        else:
            return self.__dict__
