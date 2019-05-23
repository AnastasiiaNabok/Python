class Envelope():
    def __init__(self, width, height):
        if height < width:
            self.width = self.validate_input(width)
            self.height = self.validate_input(height)
        else:
            self.width, self.height = self.validate_input(height), self.validate_input(width)

    @staticmethod
    def validate_input(input_value):
        if input_value.isdigit() and int(input_value) >= 0:
            val = int(input_value)
            return val
        else:
            raise ValueError('Value "{}" is not correct. Should be positive number'.format(input_value, ))

    def contains(self, other_envelope):
        if self.width - other_envelope.width > 0 and self.height - other_envelope.height > 0:
            return True
        else:
            return False


def try_again():
    try_again = input('Press "y" or "yes" if you want to try again.  Press any key if you want to stop. ')
    if try_again.lower() == 'y' or try_again.lower == "yes":
        main()


def main():
    first_envelope_width = input('Please enter first envelope width: ')
    first_envelope_height = input('Please enter first envelope height: ')
    try:
        envelope1 = Envelope(first_envelope_width, first_envelope_height)
    except ValueError as e:
        print(e)
        try_again()

    second_envelope_width = input('Please enter second envelope width: ')
    second_envelope_height = input('Please enter second envelope height: ')
    try:
        envelope2 = Envelope(second_envelope_width, second_envelope_height)
    except ValueError as e:
        print(e)
        try_again()

    if envelope1.contains(envelope2):
        print('The envelope 2 may be inserted in envelope 1')
    elif envelope2.contains(envelope1):
        print('The envelope 1 may be inserted in envelope 2')
    else:
        print('Envelopes could not be inserted to each other')
    try_again()


if __name__ == '__main__':
    while True:
        main()
        want_continue = input('Press y or yes if you want to continue ')
        if want_continue.lower() != "y" and want_continue.lower() != 'yes':
            break
