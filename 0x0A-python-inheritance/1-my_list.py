#!/usr/bin/python3
"""Inherits from list"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
