#!/usr/bin/python3
"""testing class square"""
import unittest
import os
from models.square import Square
import io


class test_square(unittest.TestCase):
    """testing class square"""
    def setUp(self):
        """setting up instance sq"""
        self.sq = Square(4)

    def tearDown(self):
        """del the sq"""
        del self.sq

    def test_width(self):
        """testing the width"""
        self.assertEqual(4, self.sq.width)

    def test_height(self):
        """testing the height"""
        self.assertEqual(4, self.sq.height)

    def test_x(self):
        """testing x of sq"""
        self.sq.x = 33
        self.assertEqual(33, self.sq.x)
        self.assertEqual(0, self.sq.y)

    def test_y(self):
        """testing y of sq"""
        self.sq.y = 33
        self.assertEqual(33, self.sq.y)
        self.assertEqual(0, self.sq.x)

    def test_id_sq(self):
        """testing the id of sq"""
        sq = Square(3, 0, 0, 10)
        self.assertEqual(10, sq.id)

    def test_width_zero(self):
        """zero width"""
        with self.assertRaises(ValueError):
            sq = Square(0, 4)

    def test_width_float(self):
        """with a float"""
        with self.assertRaises(TypeError):
            sq = Square(1.3, 4)

    def test_width_string(self):
        """with a str"""
        with self.assertRaises(TypeError):
            sq = Square("hello")

    def test_width_bool(self):
        """with a bool"""
        with self.assertRaises(TypeError):
            sq = Square(False)

    def test_width_list(self):
        """as a list"""
        with self.assertRaises(TypeError):
            sq = Square([4, 5])

    def test_width_negative(self):
        """ a negative value"""
        with self.assertRaises(ValueError):
            sq = Square(-3)

    def test_x_float(self):
        """with a float"""
        with self.assertRaises(TypeError):
            sq = Square(4, 1.3)

    def test_x_string(self):
        """with a str"""
        with self.assertRaises(TypeError):
            sq = Square(4, "hello")

    def test_x_bool(self):
        """with a bool"""
        with self.assertRaises(TypeError):
            sq = Square(4, False)

    def test_x_list(self):
        """as a list"""
        with self.assertRaises(TypeError):
            sq = Square(4, [4, 5])

    def test_x_negative(self):
        """ a negative value"""
        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_float(self):
        """with a float"""
        with self.assertRaises(TypeError):
            sq = Square(4, 5, 1.3)

    def test_y_string(self):
        """with a str"""
        with self.assertRaises(TypeError):
            sq = Square(4, 5, "hello")

    def test_y_bool(self):
        """with a bool"""
        with self.assertRaises(TypeError):
            sq = Square(4, 5, False)

    def test_y_list(self):
        """as a list"""
        with self.assertRaises(TypeError):
            sq = Square(4, 5, [4, 5])

    def test_y_negative(self):
        """ a negative value"""
        with self.assertRaises(ValueError):
            sq = Square(4, 5, -3)

    def test_area(self):
        """area of a sq"""
        self.assertEqual(self.sq.area(), 4 * 4)
        sq = Square(8, 8, 8, 2)
        self.assertEqual(sq.area(), 8 * 8)

    def test_updating_id(self):
        """updating id"""
        self.sq.update(72)
        self.assertEqual(72, self.sq.id)

    def test_updating_width(self):
        """updating width"""
        self.sq.update(72, 20)
        self.assertEqual(4, self.sq.width)

    def test_update_height(self):
        """updating height"""
        self.sq.update(72, 10)
        self.assertEqual(4, self.sq.height)

    def test_update_x(self):
        """updating x"""
        self.sq.update(72, 30, 15)
        self.assertEqual(15, self.sq.x)

    def test_update_y(self):
        """updating y"""
        self.sq.update(72, 30, 15, 12)
        self.assertEqual(12, self.sq.y)
