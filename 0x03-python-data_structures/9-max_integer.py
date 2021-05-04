#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > max_val:
            max_val = i
    return max_val
