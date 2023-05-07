#!/usr/bin/python3
""" Contains the square class """


class Square:
    """ class Square defines a square by : size. """

    def __init__(self, size=0, position=(0, 0)):
        """Initialises instances attributes"""

        # initialise the size
        self.size = size
        self.position = position

    @property
    def position(self):
        """Retrieve position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of the position, value is a tuple"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
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

    def __str__(self):
        """String representation of instance"""
        sq = ""
        if self.__size > 0:
            sq += '\n' * self.position[1]
            for i in range(self.__size):
                sq += ' ' * self.__position[0]
                for j in range(self.__size):
                    sq += '#'
                if i != self.__size - 1:
                    sq += '\n'
        return sq
