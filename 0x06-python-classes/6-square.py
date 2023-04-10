#!/usr/bin/python3
""" Contains the square class """


class Square:
    """ class Square defines a square by : size. """

    def __init__(self, size=0, position=(0, 0)):
        """Initialises instances attributes"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        # initialise the size
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Retrieve position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of the position, value is a tuple"""
        if not isinstance(value, turple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print('\n' * self.position[1], end="")
            for i in range(self.__size):
                print(' ' * self.__position[0], end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
        else:
            print()
