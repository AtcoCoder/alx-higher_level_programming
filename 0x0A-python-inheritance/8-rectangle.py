#!/usr/bin/python3
"""Contains Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass Rectangle from parent class BaseGeometry"""
    def __init__(self, width, height):
        """Initializes the instance attributes"""
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
