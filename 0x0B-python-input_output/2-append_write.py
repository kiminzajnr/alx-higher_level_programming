#!/usr/bin/python3
"""this module appends a string at end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
