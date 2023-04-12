#!/usr/bin/python3
"""Contains function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance
    of, or if the object is an instance
    of a class that inherited"""

    return issubclass(type(obj), a_class)
