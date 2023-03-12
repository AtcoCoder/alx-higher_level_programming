#!/usr/bin/python3
def multiple_returns(sentence):
    length_of_string = len(sentence)
    if length_of_string == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return length_of_string, first_char
