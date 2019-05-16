class FibonacciNumber:
    def __init__(self, start, end):
        if start < end:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
        self.fibonacci_list = []
        self.generate_fibonacci_list()

    def __str__(self):
        return 'Fibonacci numbers between {} and {} is {}'.format(self.start,
                                                                  self.end,
                                                                  self.fibonacci_list,)

    def generate_fibonacci_list(self):
        f1 = 0
        f2 = 1
        while f1 <= self.end:
            if f1 >= self.start:
                self.fibonacci_list.append(f1)
            f1, f2 = f2, f1 + f2
        return self.fibonacci_list


def validate_input(input_value):
    try:
        val = int(input_value)
        if val >= 0:
            return val
        else:
            raise ValueError
    except ValueError:
        print("That's not a number!")
        new_val = validate_input(input('Please enter positive number:'))
        return int(new_val)


def main():
    start = validate_input(input('Please enter start of range: '))
    end = validate_input(input('Please enter end of range: '))

    fn = FibonacciNumber(start, end)
    print(fn)


if __name__ == '__main__':
    main()
