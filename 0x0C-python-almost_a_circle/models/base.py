#!/usr/bin/python3
"""defines the first class base """
import json
import csv
import os
import turtle


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")

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
        if not json_string:
            return []

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
                    instances.append(cls.create(**i))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            text = csv.reader(f)
            csv_list = list(text)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for j in csv_list:
            dict_csv = {}
            for k in enumerate(j):
                dict_csv[list_keys[k[0]]] = int(k[1])
            matrix.append(dict_csv)

        ls_ins = []

        for i in range(len(matrix)):
            ls_ins.append(cls.create(**matrix[i]))

        return ls_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rects and sq using turtle method"""

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
