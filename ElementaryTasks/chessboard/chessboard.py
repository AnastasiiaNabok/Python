class ChessBoard:
    def __init__(self, width, height):
        self.width = self.validate_input(width)
        self.height = self.validate_input(height)

    def __str__(self):
        return self.create_board()

    @staticmethod
    def validate_input(input_value):
        if input_value.isdigit() and int(input_value) > 0:
            val = int(input_value)
            return val
        else:
            raise ValueError('Value "{}" is not correct. Should be positive number'.format(input_value, ))

    def create_board(self):
        board = str()
        for j in range(self.height):
            for i in range(self.width):
                if (i + j) % 2 == 0:
                    board = board + '*'
                else:
                    board = board + ' '
            board = board + '\n'
        return board


def try_again():
    try_again = input('Press "y" or "yes" if you want to try again.  Press any key if you want to stop. ')
    if try_again.lower() == 'y' or try_again.lower == "yes":
        main()


def main():
    width = input('Please enter board with: ')
    height = input('Please enter board height: ')

    try:
        board = ChessBoard(width, height)
        print(board)
        try_again()
    except ValueError as e:
        print(e)
        try_again()


if __name__ == '__main__':
    main()
