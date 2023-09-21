#!/usr/bin/python3
""" Do Unittests... to make id behaviour intuitive each time executed
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Tests and manage the behaviour of id. """

    def test_asdefined(self):
        a = Base(7)
        self.assertEqual(a.id, 7, "id will be as passed")
        b = Base()
        c = Base()
        self.assertEqual(c.id,2, "id will increament by one")
    def test_pasNone(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(b.id, a.id + 1)
