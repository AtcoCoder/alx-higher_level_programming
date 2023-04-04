#!/usr/bin/python3
"""Contains Class Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises the instances"""
        self.raise_if_error(width)
        self.raise_if_error(height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the length of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        self.raise_if_error(value)
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        self.raise_if_error(value)
        self.__height = value

    def raise_if_error(self, value):
        """Raise the appropiate error
        if the value is not integer or is less 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
