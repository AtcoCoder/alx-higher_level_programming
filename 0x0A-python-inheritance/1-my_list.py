#!/usr/bin/python3
"""Contains Class MyList"""


class MyList(list):
    """class MyList that inherits from list"""
    def __init__(self):
        """Initializes the instance attributes"""
        list.__init__(self)

    def print_sorted(self):
        """prints a sorted"""
        copy = self.copy()
        print(sorted(copy))
