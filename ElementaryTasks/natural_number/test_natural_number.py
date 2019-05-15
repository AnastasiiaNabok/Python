import unittest

from natural_number import Number


class TestNaturalNubmer(unittest.TestCase):

    def test_create_list(self):
        given_number = 25
        expected_result = [1, 2, 3, 4]
        actual_result = Number(given_number).result
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
