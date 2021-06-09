#!/usr/bin/python3
"""base class for all other classes"""
import json


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
