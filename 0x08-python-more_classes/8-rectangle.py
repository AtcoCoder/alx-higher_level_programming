#!/usr/bin/python3
"""Contains Class Rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises the instances"""
        self.raise_if_error(width, "width")
        self.raise_if_error(height, "height")
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Returns: printed rectangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        row = symbol * self.__width + "\n"
        rectangle = row * (self.__height - 1) + (self.__width * symbol)
        return rectangle

    def __repr__(self):
        """Returns: string representation of object name and args as passed"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a bye message when an object is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the length of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        self.raise_if_error(value, "width")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        self.raise_if_error(value, "height")
        self.__height = value

    def raise_if_error(self, value, attr):
        """Raise the appropiate error
        if the value is not integer or is less 0"""
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        elif value < 0:
            raise ValueError(f"{attr} must be >= 0")

    def area(self):
        """Method area calculate the area of a rectangle

        Returns: the area of the rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle

        Returns: the perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle base of area

        Returns: the biggest rectangle, or

        raise TypeError exception if either input is not
        a instance of Rectangle,

        if both are equal area then rect_1 is returned.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
if __name__ == "__main__":
    r = Rectangle(2, 2)
    print(r.width)
