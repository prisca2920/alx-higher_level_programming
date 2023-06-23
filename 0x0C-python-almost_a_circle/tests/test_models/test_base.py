#!/usr/bin/python3
"""tests for class base"""
import unittest
from models.base import Base
from models.square import Square
import json
import inspect


class TestBaseMethods(unittest.TestCase):
    """ tests the class base"""

    def test_idarg(self):
        b = Base()
        self.assertEqual(1, b.id)

    def test_one_id_arg(self):
        b = Base(5)
        self.assertEqual(5, b.id)

    def test_zero_id(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_neg_id(self):
        b = Base(-5)
        self.assertEqual(-5, b.id)

    def test_str_id(self):
        b = Base("Hello")
        self.assertEqual("Hello", b.id)

    def test_list_as_id(self):
        b = Base([4, 5, 6])
        self.assertEqual([4, 5, 6], b.id)

    def test_dict_as_id(self):
        b = Base({"id": 99})
        self.assertEqual({"id": 99}, b.id)

    def test_tuple_as_id(self):
        b = Base((7,))
        self.assertEqual((7,), b.id)

    def test_json_type(self):
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_json_value(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_json_None(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_json_Empty(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestClassmethods(unittest.TestCase):
    """tests Base class' methods"""

    @classmethod
    def setUpClass(cls):
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
