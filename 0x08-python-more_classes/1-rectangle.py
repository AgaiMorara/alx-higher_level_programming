#!/usr/bin/python3
'''
Rectangle: based on 0-rectangle.py.. Has private instance attributes width.
contains a method width(self) - that retrieves it... and a setter width (self,
value) that sets it.
Width must be an integer, otherwise raises a TypeError exception with the message
width must be an integer.
'''
class Rectangle:
      ''' width and height here comply with assertions'''
      def __init__(self, width=0, height=0):
            self.width = width
            self.height = height

            @property
            def width(self):
                  return self.__width
            @width.setter
            def width(self, value):
                  if type(value) is not int:
                        raise TypeError('width must be an integer')
                  if value < 0:
                        raise ValueError('height must be >= 0')
                  self.__height = value
