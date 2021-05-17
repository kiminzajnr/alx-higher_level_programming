#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elem = 0
    len_list = 0
    for item in my_list:
        len_list += 1
    try:
        for elem in my_list:
            while num_of_elem < x and num_of_elem < len_list:
                num_of_elem += 1
            print("{}".format(elem), end="")
        print()
        return num_of_elem
    except:
        pass
