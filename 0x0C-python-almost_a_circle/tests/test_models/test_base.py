#!/usr/bin/python3
""" tests for base"""
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os
import unittest
from unittest.mock import patch

class Test_the_base(unittest.TestCase):
    """ this tests the base"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_the_id(self):
        i = Base(5)
        self.assertEqual(i.id, 5)

    def test_baseID(self):
        i = Base()
        self.assertEqual(i.id, 5)

    def test_ID_obj(self):
        i = Base()
        i2 = Base()
        i3 = Base()
        self.assertEqual(i.id, 5)
        self.assertEqual(i2.id, 6)
        self.assertEqual(i3.id, 7)

    def test_ID_mix(self):
        i = Base()
        i2 = Base(102)
        i3 = Base()
        self.assertEqual(i.id, 5)
        self.assertEqual(i2.id, 102)
        self.assertEqual(i3.id, 7)

    def test_ID_str(self):
        i = Base('8')
        self.assertEqual(i.id, '8')

    def test_more_ID_args(self):
        with self.assertRaises(TypeError):
            i = Base(8, 8)

    def test_private_obj(self):
        i = Base()
        with self.assertRaises(AttributeError):
            i.__nb_objects

    def test_saving_json(self):
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as f:
            with patch('sys.stdout', i=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_saving_json2(self):
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as f:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
