class Number:
    def __init__(self, given_number):
        self.given_number = given_number
        self.result = []
        self.create_list()

    def __str__(self):
        return 'Natural numbers where square less than given number {}'.format(self.result,)

    def create_list(self):
        n = 1
        while n * n < self.given_number:
            self.result.append(n)
            n += 1
        return self.result


def validate_input(input_value):
    try:
        val = float(input_value)
        return val
    except ValueError:
        print("That's not a number!")
        new_val = validate_input(input('Please enter positive number: '))
        return float(new_val)


def main():
    given_number = validate_input(input('Please enter positive number: '))

    result = Number(given_number)
    print(result)


if __name__ == '__main__':
    while True:
        main()
        want_continue = input('Press y or yes if you want to continue ')
        if want_continue.lower() != "y" and want_continue.lower() != 'yes':
            break
