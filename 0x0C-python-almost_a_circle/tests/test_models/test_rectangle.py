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


class TestWidth(unittest.TestCase):
    """this class tests all instances of width"""
    def test_withNone(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    # a string
    def test_withstr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 4)

    def test_withfloat(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_withcomplex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_withdict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 7, "b": 4}, 2)

    def test_withbool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 5)

    def test_withlist(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 8)

    def test_withaset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 7)

    def test_withatuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 5, 6), 2)

    def test_withafrozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({4, 2, 3, 5}), 6)

    def test_withrange(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(6), 2)

    def test_withbytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'java', 1)

    def test_withbytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'ijklmno'), 9)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_floatnan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 4)

    def test_negativevalue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 2)

    def test_with0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)


class Testheight(unittest.TestCase):
    """this class tests all instances of height"""
    def test_withNone(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None)

    # a string
    def test_withstr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "hello")

    def test_withfloat(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_withcomplex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_withdict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 7, "b": 4})

    def test_withbool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, False)

    def test_withlist(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, [1, 2, 3])

    def test_withaset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, {1, 2, 3})

    def test_withatuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (4, 5, 6))

    def test_withafrozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(frozenset(6, {4, 2, 3, 5}))

    def test_withrange(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(6))

    def test_withbytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'java')

    def test_withbytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(b'abcdefg'))

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, memoryview(b'ijklmno'))

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_floatnan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('nan'))

    def test_negativevalue(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -9)

    def test_with0(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0)
