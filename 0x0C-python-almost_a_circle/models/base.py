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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(new_list))

    def from_json_string(json_string):
        """returns a list of json string representation"""
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)
