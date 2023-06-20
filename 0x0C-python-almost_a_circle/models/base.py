#!/usr/bin/python3
"""defines the first class base """
import json


class Base:
    """defines first class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """converts python obj to json str"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json rep to file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                the_dict = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(the_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json str rep"""
        if json_string is None or len(json_string) is 0:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(5, 5)
        elif cls.__name__ == 'Square':
            dummy = cls(5)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        instances = []
        dicts = []

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                text = f.read()
                dicts = cls.from_json_string(text)

                for i in dicts:
                    instances.append(cls.create(**dictionary))
        return instances
