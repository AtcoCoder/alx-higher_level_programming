#!/usr/bin/python3
""" Rectangle class methods tests """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import os
from unittest import TestCase


class TestSquareMethods(TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_square_with_default(self):
        """ Test square default values """
        r = Square(2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_square_with_define(self):
        """ Test square with assign x and y """
        r = Square(2, 2, 5)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 1)

    def test_square_id(self):
        """ Test square instances id """
        r = Square(2)
        r2 = Square(2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r2.id, 2)

    def test_square_instance_not_equal(self):
        """ Test square instances """
        r1 = Square(2)
        r2 = Square(2)
        self.assertTrue(r1 != r2)

    def test_square_width_1(self):
        """ Test square instance width """
        with self.assertRaises(TypeError):
            r = Square('2')

    def test_square_width_2(self):
        """ Test square instance width """
        with self.assertRaises(ValueError):
            r = Square(0)

    def test_square_with_3(self):
        """ Test square instance width """
        r = Square(2)
        with self.assertRaises(TypeError):
            r.size = "string"

    def test_square_width_4(self):
        """ Test square instance width """
        r = Square(2)
        with self.assertRaises(ValueError):
            r.size = 0

    def test_square_width_5(self):
        """ Test square instance width """
        with self.assertRaises(ValueError):
            r = Square(-2)

    def test_square_width_6(self):
        """ Test square instance width """
        r = Square(2)
        with self.assertRaises(ValueError):
            r.size = -1

    def test_square_width(self):
        """ Test square instance width """
        r = Square(2)
        r.size = 4
        self.assertEqual(r.size, 4)

    def test_square_height_1(self):
        """ Test square instance height """
        with self.assertRaises(TypeError):
            r = Square("2")

    def test_square_height_2(self):
        """ Test square instance height """
        r = Square(2)
        with self.assertRaises(TypeError):
            r.size = "string"

    def test_square_height_3(self):
        """ test square instance height """
        with self.assertRaises(ValueError):
            r = Square(0)

    def test_square_height_4(self):
        """ Test Square instance height """
        r = Square(2)
        with self.assertRaises(ValueError):
            r.size = 0

    def test_square_height_5(self):
        """ Test Square instance height """
        with self.assertRaises(ValueError):
            r = Square(-2)

    def test_square_height_6(self):
        """ Test Square instance height """
        r = Square(2, 2)
        with self.assertRaises(ValueError):
            r.size = -1

    def test_square_height(self):
        """ Test square instance height """
        r = Square(2, 2)
        r.size = 4
        self.assertEqual(r.size, 4)

    def test_square_area_1(self):
        """ Test square instance area """
        r = Square(2, 2)
        self.assertEqual(r.area(), 4)

    def test_square_area_2(self):
        """ Test square instance area """
        r = Square(2, 2)
        r.size = 4
        self.assertEqual(r.area(), 4 * 4)

    def test_square_area_3(self):
        """ Test square instance area """
        r = Square(2, 0, 11)
        self.assertEqual(r.area(), 2 * 2)

    def test_square_update_1(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_square_update_2(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(89, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.size, 4)

    def test_square_update_3(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(89, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.size, 4)

    def test_square_update_4(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(89, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.x, 4)

    def test_square_update_5(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(89, 4, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_square_update_6(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(size=1)
        self.assertEqual(r.size, 1)

    def test_square_update_7(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(size=1, x=4)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 4)

    def test_square_update_8(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(y=1, size=4, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.size, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)

    def test_square_update_9(self):
        """ Test square instance attr update """
        r = Square(2, 2, 2, 2)
        r.update(x=1, size=4, y=3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.size, 4)
        self.assertEqual(r.y, 3)

    def test_to_dictionary(self):
        """ Test dictionary representation of a square """
        r = Square(2, 2)
        self.assertEqual(type(r.to_dictionary()), dict)
