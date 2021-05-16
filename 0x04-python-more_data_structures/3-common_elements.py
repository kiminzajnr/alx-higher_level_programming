#!/usr/bin/python3
def common_elements(set_1, set_2):
    for item in set_1:
        for elem in set_2:
            if item == elem:
                return item
