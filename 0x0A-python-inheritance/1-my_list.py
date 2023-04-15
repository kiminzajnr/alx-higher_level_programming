#!/usr/bin/python3
"""Inherits from list"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """print sorted list"""
        sorted_lst = sorted(self)
        print(sorted_lst)
