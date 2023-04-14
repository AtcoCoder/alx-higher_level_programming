#!/usr/bin/python3
"""add_attribute function module
"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to object obj if it's possible
       Raise a TypeError if it's not possible
    """
    if "__dict__" in dir(obj):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
