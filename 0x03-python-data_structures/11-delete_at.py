#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at index, idx in my_list
    Returns the new_list, or the orginal list if idx is negative or
    out of range."""
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
