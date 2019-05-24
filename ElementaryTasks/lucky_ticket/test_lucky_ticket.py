import unittest

from lucky_ticket import LuckyTicket


class TestLuckyTicket(unittest.TestCase):

    def test_file_path_failure(self):
        file_path = 'test.txt'
        with self.assertRaises(FileExistsError):
            LuckyTicket(file_path)

    def test_moscow_ticket(self):
        file_path = 'test_moscow_tickets.txt'
        expected_count = 2
        actual_count = LuckyTicket(file_path).moscow()
        self.assertEqual(actual_count, expected_count)

    def test_piter_ticket(self):
        file_path = 'test_piter_tickets.txt'
        expected_count = 2
        actual_count = LuckyTicket(file_path).piter()
        self.assertEqual(actual_count, expected_count)

    def test_not_correct_mode(self):
        file_path = 'test_tickets.txt'
        with self.assertRaises(ValueError):
            LuckyTicket(file_path).verify_ticket()


if __name__ == '__main__':
    unittest.main()
