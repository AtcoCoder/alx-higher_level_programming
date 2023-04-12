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

if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
