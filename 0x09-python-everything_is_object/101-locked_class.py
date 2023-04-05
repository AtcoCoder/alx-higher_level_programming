#!/usr/bin/python3
"""Contains Locked Class with no class or object attribute
that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute
is called first_name."""


class LockedClass:
    """Locked class that allow no dynamically creation of instances
    attributes except named first_name"""
    __slots__ = ['first_name']
