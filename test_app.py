import unittest
from app import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 5), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertRaises(ValueError, divide, 10, 0)
    
if __name__ == '__main__':
    unittest.main()
# This code is a unit test for the math functions defined in app.py.