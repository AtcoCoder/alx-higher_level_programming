#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test suit for the max_integer function
    """
    def test_inputs_1(self):
        """Test integer input
        """
        with self.assertRaises(TypeError):
            result = max_integer(40)

    def test_inputs_2(self):
        """Test float input
        """
        with self.assertRaises(TypeError):
            result = max_integer(50.0)

    def test_input_3(self):
        """Test dict input
        """
        with self.assertRaises(KeyError):
            result = max_integer({'name': 'Omar'})

    def test_input_4(self):
        """Test tuple input
        """
        self.assertEqual(max_integer((2, 3, 8)), 8)
        self.assertEqual(max_integer((-2, -3, -8)), -2)

    def test_input_5(self):
        """Test string input
        """
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(type(max_integer('string')), str)

    def test_input_6(self):
        """Test list of integers
        """
        self.assertEqual(max_integer([2, 3, 8]), 8)
        self.assertEqual(max_integer([-2, -3, -8]), -2)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -2, 0, 0]), 0)
        self.assertEqual(max_integer([1, 1, 8, 4, 2]), 8)
        self.assertTrue(max_integer([]) == None)
        self.assertTrue(max_integer() == None)

    def test_list_elements_1(self):
        """Test mixture integers and strings
        """
        with self.assertRaises(TypeError):
            result = max_integer([2, 4, "Omar"])

    def test_list_elements_2(self):
        """Test mixture integers and lists
        """
        with self.assertRaises(TypeError):
            result = max_integer([2, [2, 4, 2], 2])
    
    def test_list_elements_3(self):
        """Test list of lists
        """
        self.assertIsInstance(max_integer([[2, 1], [2, 1]]), list)
        self.assertEqual(max_integer([[1, 2], [2, 2]]), [2, 2])
        self.assertEqual(max_integer([[]]), [])

    def test_list_elements_4(self):
        """Test list of lists and tuple
        """
        with self.assertRaises(TypeError):
            result = max_integer([[2, 1], (2, 1)])

    def test_list_elements_5(self):
        """Test list of tuples
        """
        self.assertIsInstance(max_integer([(2, 1)]), tuple)
        self.assertEqual(max_integer([(1, 2), (2, 2)]), (2, 2))
        self.assertEqual(max_integer([()]), ())
    
    def test_list_elements_6(self):
        """Test list of dict and any
        """
        self.assertEqual(max_integer([{}]), {})

        with self.assertRaises(TypeError):
            result = max_integer([{}, 23 ,23])

        with self.assertRaises(TypeError):
            result = max_integer([{}, ()])

        with self.assertRaises(TypeError):
            result = max_integer([[], {}])
