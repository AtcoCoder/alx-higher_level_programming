#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_copy = my_list.copy()
    my_list_copy.reverse()
    for element in my_list_copy:
        print("{:d}".format(element))
