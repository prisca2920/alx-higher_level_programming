#!/usr/bin/python3
"""unittests of class base"""
import unittest
from models.base import Base
from models.square import Square
import json
import inspect


class test_base(unittest.TestCase):
    """testing class base"""
    def test_no_arg(self):
        """with no arg"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_positive_int(self):
        """positive int"""
        b = Base(4)
        self.assertEqual(4, b.id)

    def test_zero_id(self):
        """with 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_neg_value(self):
        """negative value"""
        b = Base(-5)
        self.assertEqual(-5, b.id)

    def test_str_id(self):
        """with a str"""
        b = Base("hello")
        self.assertEqual("hello", b.id)

    def test_list_id(self):
        """with a list"""
        b = Base([4, 5, 6])
        self.assertEqual([4, 5, 6], b.id)

    def test_dict_id(self):
        """with a dict"""
        b = Base({"id": 10})
        self.assertEqual({"id": 10}, b.id)

    def test_tuple_id(self):
        """testing with a tuple"""
        b = Base((2,))
        self.assertEqual((2,), b.id)


if __name__ == "__main__":
    unittest.main()
