#!/usr/bin/env python3
def no_c(my_string):
    counts = my_string.count('c')
    my_string = list(my_string)
    while counts:
        my_string.remove('c')
        counts -= 1
    counts = my_string.count('C')
    while counts:
        my_string.remove('C')
        counts -= 1
    my_string = ''.join(my_string)
    return my_string
