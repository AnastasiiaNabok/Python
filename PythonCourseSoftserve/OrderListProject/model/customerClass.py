import sqlite3

conn = sqlite3.connect('order_DB.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class Customer:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def create(self):
        new_customer = [(self.name, self.phone_number, self.address)]
        rows_count = cursor.execute('SELECT count(phoneNumber) FROM customers where phoneNumber = ?',
                                    (self.phone_number,)).fetchone()[0]
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
    def delete_by_name_and_phone(name, phone_number):
        if cursor.execute('SELECT * FROM customers where name = ? AND phoneNumber=?', (name, phone_number)).fetchone():
            for customer in cursor.execute('SELECT * FROM customers where name = ? AND phoneNumber=?',
                                           (name, phone_number)):
                cursor.execute('Delete FROM customers where name = ? AND phoneNumber=?', (name, phone_number))
                cursor.fetchall()
                conn.commit()
                print(f'User {name},{phone_number} was deleted')
        else:
            print("User doesn't exist")

    def update(self, new_name=None, new_phone_number=None, new_address=None):
        if new_name and new_name != self.name:
            for customer in cursor.execute('SELECT * FROM customers where name = ?', (self.name,)):
                print(f'Name {self.name} updated to {new_name}')
                cursor.execute('UPDATE customers SET name = ? WHERE name= ?', (new_name, self.name))
        if new_phone_number and new_phone_number != self.phone_number:
            for customer in cursor.execute('SELECT * FROM customers where phoneNumber = ?', (self.phone_number,)):
               print(f'Phone Number {self.phone_number} updated to {new_phone_number}')
               cursor.execute('UPDATE customers SET phoneNumber = ? WHERE phoneNumber= ?', (new_phone_number,self.phone_number))
        if new_address and new_address != self.address:
            for customer in cursor.execute('SELECT * FROM customers where address = ?', (self.address,)):
               cursor.execute('UPDATE customers SET address = ? WHERE address= ?', (new_address, self.address))
        cursor.fetchall()
        conn.commit()

    @staticmethod
    def show_all():
        for customer in cursor.execute('SELECT * FROM customers'):
            print(tuple(customer))
