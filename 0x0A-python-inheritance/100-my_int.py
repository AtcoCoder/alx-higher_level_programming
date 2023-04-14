#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """Subclass of parent class int
    """

    def __eq__(self, other):
        """Returns False if instance is eq to other
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True if instance is ne to other
        """
        return int.__eq__(self, other)


if __name__ == "__main__":
    my_i = MyInt(3)
    #print(dir(my_i))
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
