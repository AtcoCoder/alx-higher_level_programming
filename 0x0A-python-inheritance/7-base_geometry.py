#!/usr/bin/python3
"""Contains class BaseGeometry"""


class BaseGeometry:
    """Non Empty BaseGeometry class"""

    def area(self):
        """area method to not be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value: value"""
        if self.is_not_integer(value):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def is_not_integer(self, value):
        """checks if value is integer or not"""
        if type(value) == bool:
            return True
        if isinstance(value, int):
            return False
        return True
