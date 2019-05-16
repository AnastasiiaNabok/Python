import unittest


from fibonacci import FibonacciNumber


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_list_range(self):
        start = 2
        end = 10
        fn = FibonacciNumber(start, end)
        expected_list = [2, 3, 5, 8]
        actual_list = fn.fibonacci_list
        self.assertEqual(actual_list, expected_list)

    def test_Negative_validation(self):
        start = -2
        end = 10
        with self.assertRaises(ValueError):
            FibonacciNumber(start, end)

    def test_text_validation(self):
        start = 0
        end = "test"
        with self.assertRaises(ValueError):
            FibonacciNumber(start, end)

    def test_input_order_validation(self):
        start = 45
        end = 10
        with self.assertRaises(ValueError):
            FibonacciNumber(start, end)


if __name__ == '__main__':
    unittest.main()
