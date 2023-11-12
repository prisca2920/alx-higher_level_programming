#!/usr/bin/python3
"""creating class Base"""
import json
from os import path


class Base:
    """ creating class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returning json format of base"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
