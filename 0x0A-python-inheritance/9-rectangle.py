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
        self.width = width
        self.height = height

    def __str__(self):
        """String representation of object"""
        return f"[Rectangle] {self.width}/{self.height}"

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    @property
    def width(self):
        """Retrieves the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        self.__height = value


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
