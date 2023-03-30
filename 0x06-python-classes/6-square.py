#!/usr/bin/python3
""" This module contains one class
    Class:
        Square
"""


class Square:
    """This is square contains one private attribute
    It defines a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """This function initialises the object"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (type(position) != tuple) or\
                (len(position) != 2) or \
                (type(position[0]) != int) or\
                (type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """ Determine the area of the square
        Return: area of square. """

        return self.__size * self.__size

    @property
    def size(self):
        """ Retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Print square using # """

        if self.__size == 0:
            print("")
            return

        for row in range(self.__position[1]):
            print("")
        for line in range(self.__size):
            print("_" * self.__position[0], "#" * self.__size, sep="")
        return

    @property
    def position(self):
        """ Retrieve the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square"""

        if (type(position) != tuple) or\
                (len(position) != 2) or \
                (type(position[0]) != int) or\
                (type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
