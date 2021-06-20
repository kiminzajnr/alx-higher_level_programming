#!/usr/bin/python3
"""this module writes to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns
    the number of characters written"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
