class Fib:
    """Solution with generator"""
    def __init__(self, start, end):
        if start < 0 :
            raise ValueError('Value "{}" is not correct. Should be positive number'.format(start,))
        if end < 0 :
            raise ValueError('Value "{}" is not correct. Should be positive number'.format(end,))
        if start > end:
            raise ValueError('Start should be larger than end')

        self.start = start
        self.end = end

    def generate(self):
        f1, f2 = 0, 1
        while f1 <= self.end:
            if f1 >= self.start:
                yield f1
            f1, f2 = f2, f1 + f2

def main():
    try:
        start = int(input('Please enter start of range: '))
        end = int(input('Please enter end of range: '))
        f = Fib(start, end)
        for n in f.generate():
            print(n, end=", ")
    except ValueError as e:
        print(e)
        try_again = input('Press "y" or "yes" if you want to try again. Press any key if you want to stop.')
        if try_again.lower() == 'y' or try_again.lower == "yes":
            main()


if __name__ == '__main__':
    main()
