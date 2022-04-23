#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass:
    """prevents user from dynamically creating a new
    instance attribute except if the new instance attribute is
    called first_name
    """
    __slots__ = ["first_name"]
