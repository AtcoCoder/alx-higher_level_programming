#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Generate a list where all values 'search' in the my_list
    # are replace with 'replace'
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    # Return the new_list
    return new_list
