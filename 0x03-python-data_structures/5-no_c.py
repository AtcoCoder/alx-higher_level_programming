#!/usr/bin/python3
def no_c(my_string):
    letter_list = [letter for letter in my_string if letter != 'c' and letter != 'C']
    new_word = "".join(letter_list)
    return new_word
