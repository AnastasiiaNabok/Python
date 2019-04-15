import sqlite3

conn = sqlite3.connect('order_DB.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class Customer:
    def __init__(self, name, phone_umber, address):
        self.name = name
        self.phoneNumber = phone_umber
        self.address = address

    def create(self):
        new_customer = [(self.name, self.phoneNumber, self.address)]
        rows_count = cursor.execute('SELECT count(phoneNumber) FROM customers where phoneNumber = ?',
                                    (self.phoneNumber,)).fetchone()[0]
        if rows_count > 0:
            print('This  user already exist')
        else:
            cursor.executemany('INSERT INTO  customers(name, phoneNumber, address) VALUES (?,?,?)', new_customer)
            conn.commit()

    @staticmethod
    def find_by_name(name):
        if cursor.execute('SELECT * FROM customers where name = ?', (name,)).fetchone():
            for customer in cursor.execute('SELECT * FROM customers where name = ?', (name,)):
                print(tuple(customer))
        else:
            print("User doesn't exist")

    @staticmethod
    def delete_by_name_and_phone(name, phoneNumber):
        if cursor.execute('SELECT * FROM customers where name = ? AND phoneNumber=?', (name, phoneNumber)).fetchone():
            for customer in cursor.execute('SELECT * FROM customers where name = ? AND phoneNumber=?',
                                           (name, phoneNumber)):
                cursor.execute('Delete FROM customers where name = ? AND phoneNumber=?', (name, phoneNumber))
                cursor.fetchall()
                conn.commit()
                print(f'User {name},{phoneNumber} was deleted')
        else:
            print("User doesn't exist")

    def update(self):
        pass

    def find_all(self):
        pass
