import os


class LuckyTicket:
    def __init__(self, filename):
        self.filename = filename
        self.__validate_path()

    def __validate_path(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                self.mode = lines[0]
                self.tickets_list = [ticket for ticket in lines[1:] if ticket.isdigit()]
        else:
            raise FileExistsError("File doesn't exist. Please enter new filename")

    def moscow(self):
        count = 0
        for ticket in self.tickets_list:
            ticket_half_len = len(ticket) // 2
            first_part = sum(map(int, ticket[:ticket_half_len]))
            second_part = sum(map(int, ticket[ticket_half_len:]))
            if first_part == second_part:
                count += 1
        return count

    def piter(self):
        count = 0
        for ticket in self.tickets_list:
            first_part = sum(map(int, ticket[0::2]))
            second_part = sum(map(int, ticket[1::2]))
            if first_part == second_part:
                count += 1
        return count

    def verify_ticket(self):
        if self.mode.lower() == 'moscow':
            count = self.moscow()
        elif self.mode.lower() == 'piter':
            count = self.piter()
        else:
            raise ValueError(f'Value {self.mode} is not correct mode')
        return self.mode, count


def try_again():
    try_again = input('Press "y" or "yes" if you want to try again.  Press any key if you want to stop. ')
    if try_again.lower() == 'y' or try_again.lower == "yes":
        main()


def main():
    file_path = input('Enter filename: ')
    try:
        mode, count = LuckyTicket(file_path).verify_ticket()
        print(f'We have {count} "{mode}" lucky ticket(s) in the file {file_path}')
        try_again()
    except (ValueError, FileExistsError) as e :
        print(e)
        try_again()


if __name__ == '__main__':
    main()
