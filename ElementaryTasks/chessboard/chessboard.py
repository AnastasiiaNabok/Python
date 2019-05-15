class ChessBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return self.create_board()

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


def validate_input(input_value):
    try:
        val = int(input_value)
        if val > 0:
            return val
        else:
            new_val = validate_input(input('Please enter positive number :'))
            return int(new_val)
    except ValueError:
        print("That's not a number!")
        new_val = validate_input(input('Please enter positive number:'))
        return int(new_val)


def main():
    width = validate_input(input('Please enter board with: '))
    height = validate_input(input('Please enter board height: '))

    board = ChessBoard(width, height)
    print(board)


if __name__ == '__main__':
    main()
