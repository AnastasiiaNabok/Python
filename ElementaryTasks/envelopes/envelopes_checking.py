class Envelope():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if height > width:
            self.width, self.height = height, width

    def contains(self, other_envelope):
        if self.width - other_envelope.width > 0 and self.height - other_envelope.height > 0:
            return True
        else:
            return False


def validate_input(input_value):
    try:
        val = float(input_value)
        if val > 0:
            return val
        else:
            raise ValueError
    except ValueError:
        print("That's not a number!")
        new_val = validate_input(input('Please enter positive number: '))
        return float(new_val)


def main():
    first_envelope_width = validate_input(input('Please enter first envelope width: '))
    first_envelope_height = validate_input(input('Please enter first envelope height: '))
    envelope1 = Envelope(first_envelope_width, first_envelope_height)

    second_envelope_width = validate_input(input('Please enter first envelope width: '))
    second_envelope_height = validate_input(input('Please enter first envelope height: '))
    envelope2 = Envelope(second_envelope_width, second_envelope_height)

    if envelope1.contains(envelope2):
        print('The envelope 2 may be inserted in envelope 1')
    elif envelope2.contains(envelope1):
        print('The envelope 1 may be inserted in envelope 2')
    else:
        print('Envelopes could not be inserted to each other')


if __name__ == '__main__':
    while True:
        main()
        want_continue = input('Press y or yes if you want to continue ')
        if want_continue.lower() != "y" and want_continue.lower() != 'yes':
            break
