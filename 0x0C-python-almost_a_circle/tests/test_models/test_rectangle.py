import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_therect(self):
        r = Rectangle(2, 4, 5, 6)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_wrong_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle('Hello', 4, 5, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 5, 6)

    def test_wrong_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 'Hello', 5, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 0, 5, 6)

    def test_wrong_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle('Hello', 4, 'no', 6)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, -8, 6)

    def test_wrong_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 5, 'yes')

        with self.assertRaises(ValueError):
            r = Rectangle(8, 4, 5, -2)

if __name__ == "__main__":
    unittest.main()
