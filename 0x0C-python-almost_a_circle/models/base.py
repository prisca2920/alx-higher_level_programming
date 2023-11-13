#!/usr/bin/python3
"""creating class Base"""
import json
from os import path
import csv
import turtle


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json rep to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json str rep"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attr"""
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        elif cls.__name__ == 'Square':
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename, "r") as file:
            obj = Base.from_json_string(file.read())
        list = [cls.create(**dict) for dict in obj]
        return list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws a rect n sq in turtle mode"""
        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(3)
        t.shape("turtle")

        t.color("#ffffff")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#b5e3d8")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
