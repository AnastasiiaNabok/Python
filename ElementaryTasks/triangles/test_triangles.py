import unittest

from triangles import Triangle
from triangles import split_inputs
from triangles import validate_inputs


class TestTriangle(unittest.TestCase):

    def test_calculate_area(self):
        name = 'Test1'
        side1 = 12
        side2 = 13
        side3 = 14
        expected_area = 72.31
        actual_area = Triangle(name, side1, side2, side3).area
        self.assertEqual(actual_area, expected_area)


class TestSplit(unittest.TestCase):

    def test_split(self):
        raw_str = 'Test.34,   45,  tr , 12,'
        expected_result ={'name': 'Test.34' , 'sides': ['45', 'tr', '12', '']}
        actual_result = split_inputs(raw_str)
        self.assertEqual(actual_result, expected_result)


class TestValidation(unittest.TestCase):

    def test_success_validation(self):
        parsed_line = {'name': 'Test.34', 'sides': ['2', '2', '1']}
        expected_result = ('Test.34', 2.0, 2.0, 1.0)
        actual_result = validate_inputs(parsed_line)
        self.assertEqual(actual_result, expected_result)

    def test_if_not_enough_dimensions(self):
        parsed_line = {'name': 'Test.34', 'sides': ['45']}
        with self.assertRaises(ValueError):
            validate_inputs(parsed_line)

    def test_if_dimensions_more_than_expected(self):
        parsed_line = {'name': 'Test.34', 'sides': ['45', '15', '12', '21']}
        with self.assertRaises(ValueError):
            validate_inputs(parsed_line)

    def test_if_dimensions_is_not_digits(self):
        parsed_line = {'name': 'Test.34', 'sides': ['45', 'tr', '12']}
        with self.assertRaises(ValueError):
            validate_inputs(parsed_line)

    def test_if_triangle_doesnt_exists(self):
        parsed_line = {'name': 'Test.34', 'sides': ['45', '15', '12']}
        with self.assertRaises(ValueError):
            validate_inputs(parsed_line)


if __name__ == '__main__':
    unittest.main()
