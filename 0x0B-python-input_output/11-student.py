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
        Student instance"""
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
