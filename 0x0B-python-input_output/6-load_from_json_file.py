#!/usr/bin/python3
"""creates an object from a json file"""
import json


def load_from_json_file(filename):
    """creates an Object from a json file"""
    with open(filename, "r") as f:
        return json.load(f)
