# -*- coding: utf-8 -*-

""" Unit tests for main.py """

import unittest
from main import print_numbers, is_multiple_of_x


class TestMainModule(unittest.TestCase):

    def test_is_multiple_of_x(self):
        self.assertTrue(is_multiple_of_x(5, 5))
        self.assertTrue(is_multiple_of_x(15, 5))
        self.assertTrue(is_multiple_of_x(15, 3))
        self.assertFalse(is_multiple_of_x(15, 7))
        self.assertTrue(is_multiple_of_x(9, 3))

    def test_print_numbers_until_10(self):
        res = list(print_numbers(10))
        self.assertIn('1', res)
        self.assertIn('2', res)
        self.assertIn('Three', res)
        self.assertIn('Five', res)

        n = len(filter(lambda x: x == 'Three', res))
        self.assertEqual(3, n)

        n = len(filter(lambda x: x == 'Five', res))
        self.assertEqual(2, n)

    def test_print_numbers_until_20(self):
        res = list(print_numbers(20))
        self.assertIn('Three', res)
        self.assertIn('Five', res)
        self.assertIn('ThreeFive', res)

        n = len(filter(lambda x: x == 'Three', res))
        self.assertEqual(5, n)

        n = len(filter(lambda x: x == 'Five', res))
        self.assertEqual(3, n)

        n = len(filter(lambda x: x == 'ThreeFive', res))
        self.assertEqual(1, n)

    def test_print_numbers_until_50(self):
        res = list(print_numbers(50))
        self.assertIn('Three', res)
        self.assertIn('Five', res)
        self.assertIn('ThreeFive', res)
        self.assertIn('49', res)

        n = len(filter(lambda x: x == 'Three', res))
        self.assertEqual(13, n)

        n = len(filter(lambda x: x == 'Five', res))
        self.assertEqual(7, n)

        n = len(filter(lambda x: x == 'ThreeFive', res))
        self.assertEqual(3, n)

    def test_print_numbers_until_100(self):
        res = list(print_numbers(100))
        self.assertIn('Three', res)
        self.assertIn('Five', res)
        self.assertIn('ThreeFive', res)
        self.assertIn('49', res)
        self.assertIn('98', res)

        n = len(filter(lambda x: x == 'Three', res))
        self.assertEqual(27, n)

        n = len(filter(lambda x: x == 'Five', res))
        self.assertEqual(14, n)

        n = len(filter(lambda x: x == 'ThreeFive', res))
        self.assertEqual(6, n)

if __name__ == "__main__":
    unittest.main()
