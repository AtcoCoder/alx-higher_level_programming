#!/usr/bin/python3
"""Contains unittest for the base class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBaseMethods(unittest.TestCase):
    """ Test suite for Base class methods """

    def setUp(self):
        """Initiailizing test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def
