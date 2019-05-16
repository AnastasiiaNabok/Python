import unittest

from chessboard import ChessBoard


class TestChessBoard(unittest.TestCase):

    def test_create_board(self):
        width = '5'
        height = '3'
        chessboard1 = ChessBoard(width, height)
        self.assertEqual(chessboard1.create_board(), "* * *\n * * \n* * *\n")
        self.assertNotEqual(chessboard1.create_board(), "* * * *")

    def test_negative_validation(self):
        width = '-2'
        height = '10'
        with self.assertRaises(ValueError):
            ChessBoard(width, height)

    def test_text_validation(self):
        width = '10'
        height = "test"
        with self.assertRaises(ValueError):
            ChessBoard(width, height)

    def test_zero_validation(self):
        width = '0'
        height = '10'
        with self.assertRaises(ValueError):
            ChessBoard(width, height)


if __name__ == '__main__':
    unittest.main()
