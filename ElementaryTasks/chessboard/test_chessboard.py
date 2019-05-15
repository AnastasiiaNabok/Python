import unittest

from chessboard import ChessBoard


class TestChessBoard(unittest.TestCase):

    def test_create_board(self):
        chessboard1 = ChessBoard(5, 3)
        self.assertEqual(chessboard1.create_board(), "* * *\n * * \n* * *\n")
        self.assertNotEqual(chessboard1.create_board(), "* * * *")


if __name__ == '__main__':
    unittest.main()
