#!/usr/bin/python3
"""Contains lookup function"""


def lookup(obj):
    """Takes object obj and returns the list
    of available attributes and methods
    of obj"""
    return list(obj.__dict__)
