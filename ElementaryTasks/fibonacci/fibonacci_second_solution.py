class Fib:
    """Solution with generator"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate(self):
        f1, f2 = 0, 1
        while f1 <= self.end:
            if f1 >= self.start:
                yield f1
            f1, f2 = f2, f1 + f2


def validate_input(input_value):
    try:
        val = int(input_value)
        if val >= 0:
            return val
        else:
            new_val = validate_input(input('Please enter positive number :'))
            return int(new_val)
    except ValueError:
        print("That's not a number!")
        new_val = validate_input(input('Please enter positive number:'))
        return int(new_val)


def main():
    start = validate_input(input('Please enter start of range: '))
    end = validate_input(input('Please enter end of range: '))

    f = Fib(start, end)
    for n in f.generate():
        print(n, end=", ")


if __name__ == '__main__':
    main()
