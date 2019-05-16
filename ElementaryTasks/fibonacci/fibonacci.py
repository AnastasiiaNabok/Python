class FibonacciNumber:
    def __init__(self, start, end):
        self.start = self.validate_input(start)
        self.end = self.validate_input(end)
        if self.start > self.end:
            raise ValueError('Start could not be bigger than end')

        self.fibonacci_list = []
        self.generate_fibonacci_list()

    def __str__(self):
        if not self.fibonacci_list:
            return 'No fibonacci numbers between {} and {}'.format(self.start,
                                                                      self.end, )
        else:
            return 'Fibonacci numbers between {} and {} is {}'.format(self.start,
                                                                  self.end,
                                                                  self.fibonacci_list,)

    @staticmethod
    def validate_input(input_value):
        if input_value.isdigit() and int(input_value) >= 0:
            val = int(input_value)
            return val
        else:
            raise ValueError('Value "{}" is not correct. Should be positive number'.format(input_value,))

    def generate_fibonacci_list(self):
        f1 = 0
        f2 = 1
        while f1 <= self.end:
            if f1 >= self.start:
                self.fibonacci_list.append(f1)
            f1, f2 = f2, f1 + f2
        return self.fibonacci_list


def main():
        start = input('Please enter start of range: ')
        end = input('Please enter end of range: ')

        try:
            fn = FibonacciNumber(start, end)
            print(fn)
        except ValueError as e:
            print(e)
            try_again = input('Press "y" or "yes" if you want to try again. Press any key if you want to stop.')
            if try_again.lower() == 'y' or try_again.lower == "yes":
                main()


if __name__ == '__main__':
    main()
