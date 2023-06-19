import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_therect(self):
        r = Rectangle(2, 4, 5, 6, 4)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        self.assertEqual(r.id, 4)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_lessargs(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_wrong_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle('Hello', 4, 5, 6, 3)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 5, 6, 3)

    def test_wrong_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 'Hello', 5, 6, 3)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 0, 5, 6, 3)

    def test_wrong_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle('Hello', 4, 'no', 6, 3)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, -8, 6, 3)

    def test_wrong_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 5, 'yes', 3)

        with self.assertRaises(ValueError):
            r = Rectangle(8, 4, 5, -2, 3)

if __name__ == "__main__":
    unittest.main()
