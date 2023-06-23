#!/usr/bin/python3
""" test for class square"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """testing the square class"""

    def test_is_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Square)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            Square()

    def test_onearg(self):
        s1 = Square(5)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_twoargs(self):
        s1 = Square(5, 2)
        s2 = Square(2, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_threeargs(self):
        s1 = Square(5, 2, 2)
        s2 = Square(2, 2, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_fourargs(self):
        self.assertEqual(7, Square(5, 2, 2, 7).id)

    def test_morethanfourargs(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_sizeprivate(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 2, 3, 4).__size)

    def test_sizegetter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_sizesetter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_widthgetter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_heightgetter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_xgetter(self):
        self.assertEqual(0, Square(5).x)

    def test_ygetter(self):
        self.assertEqual(0, Square(5).y)


