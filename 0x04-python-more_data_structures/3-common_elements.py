#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ Creates a set of common elements in set_1 and set_2
    return the create set"""
    new_set = set([
        element for element in set_1
        for element2 in set_2 if element == element2])
    return new_set
