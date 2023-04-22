#!/usr/bin/python3
"""Contains unittest for the base class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


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

    def test_to_json_string_is_empty(self):
        """ Test for an empty list as input """
        b = Base()
        empty_list = []
        self.assertEqual(b.to_json_string(empty_list), "[]")

    def test_to_json_string_is_none(self):
        """ Test for None input """
        b = Base()
        none_list = None
        self.assertEqual(b.to_json_string(none_list), "[]")

    def test_to_json_string(self):
        """ Test for JSON string representation of list of dictionaries """
        b = Base()
        list_dictionaries = [
            {"name": "Omar", "surname": "Jammeh"},
            {"name": "Alx", "surname": "Africa"}]
        self.assertEqual(type(b.to_json_string(list_dictionaries)), str)

    def test_save_to_file_none(self):
        """Test JSON file"""
        Square.save_to_file(None)
        with open('Square.json', mode='r', encoding='utf-8') as f:
            file_content = f.read()
            self.assertEqual(file_content, '[]')
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_save_to_file_empty(self):
        """Test JSON file"""
        Square.save_to_file([])
        with open('Square.json', 'r') as f:
            file_content = f.read()
            self.assertEqual(file_content, '[]')
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_from_json_string_none(self):
        """ Test JSON file """
        list_string = None
        self.assertEqual(type(Rectangle.from_json_string(list_string)), list)

    def test_from_json_string_empty(self):
        """ Test JSON file """
        list_string = "[]"
        self.assertEqual(type(Rectangle.from_json_string(list_string)), list)

    def test_load_from_file(self):
        """ Test load from JSON file """
        list_objs = Rectangle.load_from_file()
        self.assertEqual(type(list_objs), list)
