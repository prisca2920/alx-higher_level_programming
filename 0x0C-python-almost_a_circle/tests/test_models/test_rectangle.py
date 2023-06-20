#!/usr/bin/python3
"""unnittest for class square"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangles_base(self):
        self.assertIsInstance(Rectangle(5, 3), Base)

    def test_therect(self):
        r = Rectangle(2, 4, 5, 6, 4)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        self.assertEqual(r.id, 4)

    # testing with different no of args

    def test_noargs(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_lessargs(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_twoargs(self):
        r1 = Rectangle(5, 3)
        r2 = Rectangle(5, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_threeargs(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_fourargs(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_fiveargs(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_fiveplusargs(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 5, 6, 7, 8)

    # accessing private attributes

    def test_privatewidth(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 2).__width)

    def test_privateheight(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 2).__height)

    def test_privateX(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 2).__x)

    def test_privateY(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 2).__y)

    # testing with getters and setters

    def test_widthgetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_widthsetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_heightgetter(self):
        r = Rectangle(4, 7, 7, 5, 2)
        self.assertEqual(7, r.height)

    def test_heightsetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_Xgetter(self):
        r = Rectangle(4, 7, 7, 5, 2)
        self.assertEqual(7, r.x)

    def test_Xsetter(self):
        r = Rectangle(4, 7, 7, 5, 2)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_Ygetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_Ysetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)
