#!/usr/bin/python3
"""Contains Class MyList"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints a sorted"""
        copy = self.copy()
        copy.sort()
        print(sorted(copy))
