import unittest
from test_1 import sum_int


class TestSumInt(unittest.TestCase):

    def test_task_ok(self):
        args = ['200', '45']

        expect = 245
        result = sum_int.sum_str(args)

        self.assertEqual(expect, result)

    def test_invalid_arg_type(self):
        args = ['abc', '45']

        with self.assertRaises(ValueError) as e:
            sum_int.sum_str(args)

    def test_invalid_number_arg(self):
        args = ['123', '45', '433']

        with self.assertRaises(ValueError) as e:
            sum_int.sum_str(args)
