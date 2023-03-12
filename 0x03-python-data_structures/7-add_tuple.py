#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Create a new tuple from the addition of the elements of the two tuples
    list_a = [0, 0]
    list_b = [0, 0]
    for idx, num in enumerate(tuple_a):
        list_a[idx] = num
    for idx, num in enumerate(tuple_b):
        list_b[idx] = num
    new_list = [a + b for a, b in zip(list_a, list_b)]
    return tuple(new_list)
