#!/usr/bin/python3
"""Student class defines a student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        Student instance if attrs is a list of stirngs, only
        only attribute name contained in the list must be retrieved
        else all attributes must be retrieved"""
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
