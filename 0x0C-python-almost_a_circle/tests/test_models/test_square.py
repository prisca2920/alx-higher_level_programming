#!/usr/bin/python3
# test_square.py
"""tests class sq"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """tests class sq"""

    def test_isbase(self):
        self.assertIsInstance(Square(9), Base)

    def test_isrectangle(self):
        self.assertIsInstance(Square(9), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(9)
        s2 = Square(10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(9, 2)
        s2 = Square(2, 9)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(9, 2, 2)
        s2 = Square(2, 2, 9)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(9, Square(10, 2, 2, 9).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(9, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(9, Square(9, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 4
        self.assertEqual(4, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 4
        self.assertEqual(4, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(9).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(9).y)


class TestSquare_size(unittest.TestCase):
    """for testing size"""

    def test_Nonesize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_strsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("hello")

    def test_floatsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.5)

    def test_complexsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(6))

    def test_dictsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_boolsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([4, 5, 6])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({4, 5, 6}, 2)

    def test_tuplesize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 6, 7)

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({5, 6, 7, 8}))

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(8))

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'java')

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-8, 2)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

if __name__ == "__main__":
    unittest.main()
