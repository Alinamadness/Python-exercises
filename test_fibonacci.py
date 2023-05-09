import unittest
from fibonacci import fibonacci_loop

class FibonacciSeqTestCase(unittest.TestCase):
    """
    Tests for the fibonacci_loop function. Check the type of input and sign of input, some of examples - for 0th, 1th, 11th, 80th
    elements of Fibonacci sequence.
    """

    def test_0_loop(self):
        res = fibonacci_loop(0)
        self.assertEqual(res, 0)

    def test_1_loop(self):
        res = fibonacci_loop(1)
        self.assertEqual(res, 1)

    def test_11_loop(self):
        res = fibonacci_loop(11)
        self.assertEqual(res, 89)

    def test_80_loop(self):
        res = fibonacci_loop(80)
        self.assertEqual(res, 23416728348467685)

    def test_not_neg(self):
        with self.assertRaises(ValueError) as e:
            fibonacci_loop('-2')

    def test_is_int(self):
        with self.assertRaises(ValueError) as e:
            fibonacci_loop('2.5')

if __name__ == '__main__':
    unittest.main()
