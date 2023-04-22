#!/usr/bin/python3
""" Rectangle class methods tests """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import os
from unittest import TestCase


class TestRectangleMethods(TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_rectangle_with_default(self):
        """ Test rectangle default values """
        r = Rectangle(2, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_with_define(self):
        """ Test rectangle with assign x and y """
        r = Rectangle(2, 2, 5, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_rectangle_id(self):
        """ Test Rectangle instances id """
        r = Rectangle(2, 2)
        r2 = Rectangle(2, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r2.id, 2)

    def test_rectangle_instance_not_equal(self):
        """ Test rectangle instances """
        r1 = Rectangle(2, 2)
        r2 = Rectangle(2, 2)
        self.assertTrue(r1 != r2)

    def test_rectangle_width_1(self):
        """ Test rectangle instance width """
        with self.assertRaises(TypeError):
            r = Rectangle('2', 2)

    def test_rectangle_width_2(self):
        """ Test rectangle instance width """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_rectangle_with_3(self):
        """ Test rectangle instance width """
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r.width = "string"

    def test_rectangle_width_4(self):
        """ Test rectangle instance width """
        r = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_rectangle_width_5(self):
        """ Test rectangle instance width """
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 2)

    def test_rectangle_width_6(self):
        """ Test rectangle instance width """
        r = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            r.width = -1

    def test_rectangle_width(self):
        """ Test rectangle instance width """
        r = Rectangle(2, 2)
        r.width = 4
        self.assertEqual(r.width, 4)

    def test_rectangle_height_1(self):
        """ Test rectangle instance height """
        with self.assertRaises(TypeError):
            r = Rectangle(2, "2")

    def test_rectangle_height_2(self):
        """ Test rectangle instance height """
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r.height = "string"

    def test_rectangle_height_3(self):
        """ test rectangle instance height """
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

    def test_rectangle_height_4(self):
        """ Test Rectangle instance height """
        r = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_rectangle_height_5(self):
        """ Test Rectangle instance height """
        with self.assertRaises(ValueError):
            r = Rectangle(2, -2)

    def test_rectangle_height_6(self):
        """ Test Rectangle instance height """
        r = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            r.height = -1

    def test_rectangle_height(self):
        """ Test rectangle instance height """
        r = Rectangle(2, 2)
        r.height = 4
        self.assertEqual(r.height, 4)

    def test_rectangle_area_1(self):
        """ Test rectangle instance area """
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)

    def test_rectangle_area_2(self):
        """ Test rectangle instance area """
        r = Rectangle(2, 2)
        r.width = 4
        r.height = 5
        self.assertEqual(r.area(), 4 * 5)

    def test_rectangle_area_3(self):
        """ Test rectangle instance area """
        r = Rectangle(2, 2, 0, 0, 11)
        self.assertEqual(r.area(), 2 * 2)

    def test_rectangle_update_1(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rectangle_update_2(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)

    def test_rectangle_update_3(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89, 4, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)

    def test_rectangle_update_4(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89, 4, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)

    def test_rectangle_update_5(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(89, 4, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_update_6(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_rectangle_update_7(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(width=1, x=4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 4)

    def test_rectangle_update_8(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(y=1, width=4, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)

    def test_rectangle_update_9(self):
        """ Test rectangle instance attr update """
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(x=1, height=4, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)

    def test_to_dictionary(self):
        """ Test dictionary representation of a rectangle """
        r = Rectangle(2, 2)
        self.assertEqual(type(r.to_dictionary()), dict)
