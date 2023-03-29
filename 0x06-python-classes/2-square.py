#!/usr/bin/python3
""" Contains the square class """


class Square:
    """ class Square defines a square by : size. """

    def __init__(self, size=0):
        """Initialises instances attributes"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        # initialise the size
        self.__size = size
