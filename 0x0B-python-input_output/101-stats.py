#!/usr/bin/python3
"""Contains log parsing script"""


import sys


def print_statistics(file_size_list, status_code_list):
    """Prints some statistic data"""
    print(size_text, sum(file_size_list))
    for st_code in set(status_code_list):
        print("{}: {}".format(st_code, status_code_list.count(st_code)))


file_size_list = []
status_code_list = []
line_number = 0
size_text = "File size:"
try:
    for line in sys.stdin:
        is_time_to_print = False
        line_number += 1
        data = line.rstrip()
        list_data = data.split()
        file_size = int(list_data[-1])
        status_code = int(list_data[-2])
        file_size_list.append(file_size)
        status_code_list.append(status_code)
        if line_number % 10 == 0:
            print_statistics(file_size_list, status_code_list)
except KeyboardInterrupt:
    print_statistics(file_size_list, status_code_list)
    raise
