#!/usr/bin/python3
"""Contains class BaseGeometry"""


class BaseGeometry:
    """Non Empty BaseGeometry class"""

    def area(self):
        """area method to not be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value: value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
