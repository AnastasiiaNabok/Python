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


if __name__ == '__main__':
    unittest.main()
