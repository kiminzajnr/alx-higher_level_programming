#!/usr/bin/python3
"""this module writes to a file"""


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
