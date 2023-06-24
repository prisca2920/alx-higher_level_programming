#!/usr/bin/python3
# test_rectangle.py
"""class rect unittest"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """class rect unittest"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(9, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_twoargs(self):
        r1 = Rectangle(7, 2)
        r2 = Rectangle(7, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 3, 4)
        r2 = Rectangle(4, 3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(6, Rectangle(8, 9, 0, 0, 6).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 1, 2, 3, 4, 5)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 2).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 3, 0, 0, 2).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 7).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 7).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(4, 7, 7, 4, 2)
        r.width = 9
        self.assertEqual(9, r.width)

    def test_height_getter(self):
        r = Rectangle(4, 7, 7, 4, 2)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(4, 7, 7, 4, 2)
        r.height = 9
        self.assertEqual(9, r.height)

    def test_xgetter(self):
        r = Rectangle(4, 7, 7, 4, 1)
        self.assertEqual(7, r.x)

    def test_xsetter(self):
        r = Rectangle(4, 7, 7, 4, 1)
        r.x = 9
        self.assertEqual(9, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(4, 6, 6, 5, 1)
        r.y = 4
        self.assertEqual(4, r.y)


if __name__ == "__main__":
    unittest.main()
