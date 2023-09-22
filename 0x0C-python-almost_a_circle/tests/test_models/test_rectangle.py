#!/usr/bin/python3
""" test rectangle behaviour """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    def test_typeBase(self):
        self.assertIsInstance(Rectangle(3,5), Base)
    def test_incorrectargs(self):
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(8)
    def test_Basic(self):
        a = Rectangle(5,4,3,2)
        self.assertEqual(a.area(), 20, "4 * 5 == 20")
        b = Rectangle (2,3,4,5,6)
        self.assertEqual(b.id, 6, "when id is given")
        c = Rectangle(8,8)
        self.assertEqual(c.id, b.id, "encapsulated class")
        self.assertEqual(b.area(), 6, "2 * 3 == 6")
    def test_withNegcoord(self):
        with self.assertRaises(ValueError):
            Rectangle (3, 2, -1, -1)
    def test_access_Private_attributes(self):
        h = Rectangle(8,8,2,2,1)
        with self.assertRaises(AttributeError):
            h.__width
            h.__height
            h.__x
            h.__y
    def test_height_getter(self):
        h = Rectangle(7,9)
        self.assertEqual(7, h.width, "width of rectangle")
        self.assertEqual(9, h.height, "height of rectangle")
    def test_raises_methoderror (self):
        with self.assertRaises(TypeError):
            l = Rectangle('a', 1)
            b = Rectangle( 3, 'b')
        with self.assertRaises(ValueError):
            l = Rectangle(-1, 6)
            b = Rectangle (6, -1)
