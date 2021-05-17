#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elem = 0
    try:
        for elem in my_list:
            while num_of_elem < x:
                num_of_elem += 1
            print("{}".format(elem), end="")
        print()
        return num_of_elem
    except:
        print("out of range")
