import unittest
from test_2 import sum_kor


class TestSumKor(unittest.TestCase):

    def test_task_ok(self):
        args = ['십삼억오천칠백육십사만삼천이백팔십구', '천삼백육']

        expect = '십삼억오천칠백육십사만사천오백구십오'
        result = sum_kor.sum(args)

        self.assertEqual(expect, result)

    def test_convert_to_int(self):
        result = sum_kor._convert_to_int('십삼억오천칠백육십사만삼천이백팔십구')
        expect = 1357643289
        self.assertEqual(expect, result)

        result = sum_kor._convert_to_int('천삼백육')
        expect = 1306
        self.assertEqual(expect, result)

        result = sum_kor._convert_to_int('십만천팔')
        expect = 101008
        self.assertEqual(expect, result)

    def test_convert_to_kor(self):
        result = sum_kor._convert_to_kor(1357643289)
        expect = '십삼억오천칠백육십사만삼천이백팔십구'
        self.assertEqual(expect, result)

        result = sum_kor._convert_to_kor(1306)
        expect = '천삼백육'
        self.assertEqual(expect, result)

        result = sum_kor._convert_to_kor(101008)
        expect = '십만천팔'
        self.assertEqual(expect, result)

    def test_invalid_arg_type(self):
        args = ['453', '이십오']

        with self.assertRaises(ValueError) as e:
            sum_kor.sum(args)

    def test_invalid_number_arg(self):
        args = ['천삼백육', '십만천팔', '이십오']

        with self.assertRaises(ValueError) as e:
            sum_kor.sum(args)
