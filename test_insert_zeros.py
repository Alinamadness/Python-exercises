import unittest
from vec_insert_zero import insert_zeros

class VectorInsZerosTestCase(unittest.TestCase):
    """
    Tests for the insert_zeros function. Check the type, length of input, appearance of zeros in input, some of examples with 1 - 3 and 10 elements.
    """
    def test_1elem(self):
        res = insert_zeros([1])
        self.assertEqual(res, [1])

    def test_2elem(self):
        res = insert_zeros([-2, 15])
        self.assertEqual(res, [-2, 0, 15])
    #
    def test_3elem(self):
        res = insert_zeros([300, -276, -9])
        self.assertEqual(res, [300, 0, -276, 0, -9])
    #
    def test_10elem(self):
        res = insert_zeros([1, 45, -8, -10, 56, 21, 1, 1, -789001, 89])
        self.assertEqual(res, [1, 0, 45, 0, -8, 0, -10, 0, 56, 0, 21, 0, 1, 0, 1, 0, -789001, 0, 89])

    def test_not_empty(self):
        with self.assertRaises(ValueError) as e:
            insert_zeros([])

    def test_no_zeros(self):
        with self.assertRaises(ValueError) as e:
            insert_zeros([1, 2, 0])

    def test_is_list(self):
        with self.assertRaises(ValueError) as e:
            insert_zeros('a')

if __name__ == '__main__':
    unittest.main()
