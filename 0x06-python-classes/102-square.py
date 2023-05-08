#!/usr/bin/python3
""" Contains the square class """


class Square:
    """ class Square defines a square by : size. """

    def __init__(self, size=0):
        """Initialises instances attributes"""

        self.size = size

    def area(self):
        """returns the current square area"""

        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Resets to size to value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Equals comparison"""
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        """Not Equals comparison"""
        if self.area() != other.area():
            return True
        return False

    def __lt__(self, other):
        """Less than comparison"""
        if self.area() < other.area():
            return True
        return False

    def __gt__(self, other):
        """Greater than comparator"""
        if self.area() > other.area():
            return True
        return False

    def __le__(self, other):
        """Less than or equal comparator"""
        if self.area() <= other.area():
            return True
        return False

    def __ge__(self, other):
        """Greater than or equal comparator"""
        if self.area() >= other.area():
            return True
        return False
