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

    def my_print(self):
        """that prints in stdout the square"""


        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
        else:
            print()
