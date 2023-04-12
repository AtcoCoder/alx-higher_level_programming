#!/usr/bin/python3
"""Contains class BaseGeometry"""


class BaseGeometry:
    """Non Empty BaseGeometry class"""

    def area(self):
        """area method to not be implemented"""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
