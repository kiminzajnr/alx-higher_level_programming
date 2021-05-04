#!/usr/bin/python3
def no_c(my_string):
    counts = my_string.count('c')
    new_string = list(my_string)
    while counts:
        new_string.remove('c')
        counts -= 1
    counts = my_string.count('C')
    while counts:
        new_string.remove('C')
        counts -= 1
    new_string = ''.join(new_string)
    return new_string
