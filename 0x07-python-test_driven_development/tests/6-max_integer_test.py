#!/usr/bin/python3
"""Max integer - Unittest"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """Max integer - Unittest"""
    def test_empty_list(self):
        """testing empty list"""
        lst = []
        self.assertIsNone(max_integer(lst))

    def test_positive_ints(self):
        """Test arranged positive ints"""
        lst = [1, 2, 3, 4]
        self.assertEqual(max_integer(lst), 4)

    def test_mixed_ints(self):
        """Test unarranged positive ints"""
        lst = [2, 1, 4, 3]
        self.assertEqual(max_integer(lst), 4)

    def test_negative_ints(self):
        """Test negative ints"""
        lst = [-1, -2, -3, -4]
        self.assertEqual(max_integer(lst), -1)

    def test_pos_neg_ints(self):
        """Test mixed ints"""
        lst = [1, -2, -3, 4]
        self.assertEqual(max_integer(lst), 4)

    def test_floats(self):
        """Test a list with floats"""
        lst = [1.2, 2.3, 3.2, 4.1]
        self.assertEqual(max_integer(lst), 4.1)

    def test_negative_floats(self):
        """Test negative floats"""
        lst = [-1.3, -2.1, -3.4, -4.5]
        self.assertEqual(max_integer(lst), -1.3)

    def test_mixed_floats(self):
        """Test positie and negative floats"""
        lst = [1.5, -2.2, -3.4, 4.5]
        self.assertEqual(max_integer(lst), 4.5)

    def test_floats_and_ints(self):
        """Test floats and ints"""
        lst = [1.1, 2, 3, 4.5]
        self.assertEqual(max_integer(lst), 4.5)

    def test_one_item(self):
        """one item in list"""
        lst = [4]
        self.assertEqual(max_integer(lst), 4)

    def test_string(self):
        """test a str"""
        lst = 'zebra'
        self.assertEqual(max_integer(lst), 'z')

    def test_list_of_str(self):
        """Test a list of str"""
        lst = ['zebra', 'ann']
        self.assertEqual(max_integer(lst), 'zebra')

    def test_empty_string(self):
        """Test an empty str"""
        lst = ''
        self.assertEqual(max_integer(lst), None)

    def test_dict_as_list(self):
        """empty dict"""
        lst = {}
        self.assertEqual(max_integer(lst), None)


if __name__ == '__main__':
    unittest.main()
