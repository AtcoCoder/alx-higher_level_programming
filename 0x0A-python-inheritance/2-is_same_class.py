#!/usr/bin/python3
"""Contains the is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if object ojb is an instance of
    class a_class"""
    return type(obj) is a_class
