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
        self.__width = width
        self.__height = height

    def __str__(self):
        """String representation of object"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
