#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    for position in range(len(str)):
        if position == n:
            continue
        else:
            str_copy += str[position]
    return str_copy
