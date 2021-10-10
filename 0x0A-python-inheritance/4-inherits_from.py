#!/usr/bin/python3
"""check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """return True if object is an instance of a class that
    inherited from specified class"""
    x = issubclass(obj.__class__, a_class)
    if x is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
