#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        new_list = my_list.copy()
        new_list.reverse()
        for element in new_list:
            print("{:d}".format(element))
