#!/usr/bin/python3
"""tests the class rectangle"""
import unittest
from models.rectangle import Rectangle
import io
import sys
from models.base import Base


class test_rectangle(unittest.TestCase):
    """testing the class rect"""
    def setUp(self):
        """setting class rect"""
        self.r = Rectangle(3, 6)

    def tearDown(self):
        """deleting value of rect"""
        del self.r

    def test_height(self):
        """validating height"""
        self.assertEqual(6, self.r.height)

    def test_width(self):
        """validating width"""
        self.assertEqual(3, self.r.width)

    def test_x(self):
        """testing x"""
        self.r.x = 44
        self.assertEqual(44, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        """testing y"""
        self.r.y = 34
        self.assertEqual(34, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_rect_id(self):
        """testing rect id"""
        rect = Rectangle(4, 5, 0, 0, 170)
        self.assertEqual(170, rect.id)

    def test_height_str(self):
        """height as a str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, "hello")

    def test_height_bool(self):
        """height as bool"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, False)

    def test_height_list(self):
        """height as a list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, [1, 5])

    def test_height_neg(self):
        """negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, -5)

    def test_height_zero(self):
        """height as zero"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 0)

    def test_height_float(self):
        """height as a float"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 1.3)

    def test_noarg_height(self):
        """no arg"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_width_str(self):
        """width as a str"""
        with self.assertRaises(TypeError):
            rect = Rectangle("hello", 3)

    def test_width_bool(self):
        """width as bool"""
        with self.assertRaises(TypeError):
            rect = Rectangle(False, 6)

    def test_width_list(self):
        """width as a list"""
        with self.assertRaises(TypeError):
            rect = Rectangle([1, 5], 6)

    def test_width_neg(self):
        """negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 6)

    def test_width_zero(self):
        """width as zero"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 6)

    def test_width_float(self):
        """width as a float"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1.3, 6)

    def test_noarg_width(self):
        """no arg"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_x_str(self):
        """x as a str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, "hello")

    def test_x_bool(self):
        """x as bool"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, False)

    def test_x_list(self):
        """x as a list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, [1, 5])

    def test_x_neg(self):
        """negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 6, -5)

    def test_x_zero(self):
        """x as zero"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 6, 0)

    def test_x_float(self):
        """x as a float"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, 1.3)

    def test_y_str(self):
        """y as a str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, 5, "hello")

    def test_y_bool(self):
        """y as bool"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, 5, False)

    def test_y_list(self):
        """y as a list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, 5, [1, 5])

    def test_y_neg(self):
        """negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 6, 5, -5)

    def test_y_zero(self):
        """y as zero"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 6, 5, 0)

    def test_y_float(self):
        """y as a float"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 6, 5, 1.3)

    def test_area(self):
        """area of a rect"""
        self.assertEqual(self.r.area(), 3 * 6)
        rect = Rectangle(4, 5, 8, 8, 2)
        self.assertEqual(rect.area(), 4 * 5)

    def test_updating_id(self):
        """updating id"""
        self.r.update(72)
        self.assertEqual(72, self.r.id)

    def test_updating_width(self):
        """update width"""
        self.r.update(72, 10)
        self.assertEqual(10, self.r.width)

    def test_updating_height(self):
        """updating height"""
        self.r.update(72, 10, 20)
        self.assertEqual(20, self.r.height)

    def test_updating_x(self):
        """updating x"""
        self.r.update(72, 10, 20, 6)
        self.assertEqual(6, self.r.x)

    def test_updating_y(self):
        """updating y"""
        self.r.update(72, 10, 20, 6, 2)
        self.assertEqual(2, self.r.y)

    def test_str_overload(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")
