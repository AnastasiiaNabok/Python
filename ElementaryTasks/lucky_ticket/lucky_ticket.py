import os


def get_tickets_from_file():
    file_path = input('Enter filename: ')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            mode = lines[0]
            tickets_list = lines[1:]

            return mode, tickets_list
    else:
        print("File doesn't exist. Please enter new filename")
        get_tickets_from_file()


def verify_ticket():
    mode, tickets_list = get_tickets_from_file()
    ticket_length = len(tickets_list)
    if mode.lower() == 'moscow':
        for ticket in tickets_list:
            pass
    elif mode.lower == 'piter':
        pass
    else:
        raise ValueError


def main():
    verify_ticket()


if __name__ == '__main__':
    main()
