import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    def test_subtract(self):
        # COMPLETE HERE
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-3, 3), 0)
        self.assertEqual(subtract(-4, -4), -8)
    def test_divide(self):
        # COMPLETE HERE
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(-3, -1), 3)
if __name__ == '__main__':
    unittest.main()
