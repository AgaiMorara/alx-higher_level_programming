#!/usr/bin/python3
""" Let us make all squares to have a field called size"""


class Square:
    """ defines a Square with private instance attribute size """
    def __init__(self, size=0):
        """ Instantiates the class square
            Args:
            @size: side of the square """
        self.__size = size
