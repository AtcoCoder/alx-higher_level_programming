#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a copy of the list which contains only unique items using sets
    new_set = set(my_list)
    # Add of the items of the new set
    sum = 0
    for num in new_set:
        sum += num
    # Return the sums of all the items in the new set
    return sum
