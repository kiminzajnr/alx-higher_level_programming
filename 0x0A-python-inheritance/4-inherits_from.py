#!/usr/bin/python3
"""check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """return True is object is an instance of a class that
    inherited from specified class"""
    x = issubclass(type(obj), a_class)
    if x:
        return True
    return True
