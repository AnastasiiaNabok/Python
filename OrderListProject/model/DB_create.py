import datetime
import sqlite3
conn = sqlite3.connect('order_DB.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customers (customer_id integer primary key, name, phoneNumber, address)")
cursor.execute("CREATE TABLE IF NOT EXISTS items (item_id integer primary key, name, countable, pricePerItem)")
cursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id integer primary key, customer_id, item_id, date, "
               "completed), FOREIGN KEY(customer_id) REFERENCES customers(customer_id),"
               " FOREIGN KEY(item_id) REFERENCES items(item_id))")


'''customers = [('Ivan', '0501234358', 'Dnipro, Myra str., 14 app 56'),
             ('Anna', '0501863935', 'Dnipro, Myra str., 14 app 56'),
             ('Igor', '0500583723', 'Dnipro, Myra str., 14 app 56'),
            ]
cursor.executemany('INSERT INTO  customers(name, phoneNumber, address) VALUES (?,?,?)', customers)

items = [('cupcake', 1, 45),
         ('chocolate cake', 0, 350),
         ('carrot cake', 0, 350),
         ('marshmallow', 1, 15),
         ('gingerbread', 1, 30),
         ('cheesecake', 0, 400),
        ]

cursor.executemany('INSERT INTO  items(name, countable, pricePerItem) VALUES (?,?,?)', items)'''

'''Customer functions'''

def create_customer(customer):
    new_customer = [(customer.name, customer.phone_number, customer.address)]
    rows_count = cursor.execute('SELECT count(phoneNumber) FROM customers where phoneNumber = ?',
                                (customer.phone_number,)).fetchone()[0]
    if rows_count > 0:
        print('This  user already exist')
    else:
        cursor.executemany('INSERT INTO  customers(name, phoneNumber, address) VALUES (?,?,?)', new_customer)
        conn.commit()


def get_customer_by_name(name):
    if cursor.execute('SELECT * FROM customers where name = ?', (name,)).fetchone():
        for customer in cursor.execute('SELECT * FROM customers where name = ?', (name,)):
            print(customer)
    else:
        print("User doesn't exist")


def delete_customer_by_name_and_phone(name, phone_number):
    if cursor.execute('SELECT * FROM customers where name = ? AND phoneNumber=?', (name, phone_number)).fetchone():
        for c in cursor.execute('SELECT * FROM customers where name = ? AND phoneNumber=?',
                                       (name, phone_number)):
            cursor.execute('Delete FROM customers where name = ? AND phoneNumber=?', (name, phone_number))
            cursor.fetchall()
            conn.commit()
            print(f'User {name},{phone_number} was deleted')
    else:
        print("User doesn't exist")


def update_customer(customer, new_name=None, new_phone_number=None, new_address=None):
    if new_name == customer.name and new_phone_number == customer.phone_number and new_address == customer.address:
        print('Customer is up to date')

    if new_name and new_name != customer.name:
        for c in cursor.execute('SELECT * FROM customers where name = ?', (customer.name,)):
            print(f'Name {customer.name} updated to {new_name}')
            cursor.execute('UPDATE customers SET name = ? WHERE name= ?', (new_name, customer.name))
            customer.name = new_name

    if new_phone_number and new_phone_number != customer.phone_number:
        for c in cursor.execute('SELECT * FROM customers where phoneNumber = ?', (customer.phone_number,)):
            print(f'Phone Number {customer.phone_number} updated to {new_phone_number}')
            cursor.execute('UPDATE customers SET phoneNumber = ? WHERE phoneNumber= ?',
                           (new_phone_number, customer.phone_number))
            customer.phone_number = new_phone_number

    if new_address and new_address != customer.address:
        for c in cursor.execute('SELECT * FROM customers where address = ?', (customer.address,)):
            cursor.execute('UPDATE customers SET address = ? WHERE address= ?', (new_address, customer.address))
            print(f'Address {customer.address} updated to {new_address}')
            customer.address = new_address


    cursor.fetchall()
    conn.commit()


def get_all_customers():
    for customer in cursor.execute('SELECT * FROM customers'):
        print(customer)

'''Item functions'''


def create_item(item):
    new_item = [(item.name, item.price, item.countable)]
    rows_count = cursor.execute('SELECT count(name) FROM items where name = ?',
                                (item.name,)).fetchone()[0]
    if rows_count > 0:
        print('This  item already exist')
    else:
        cursor.executemany('INSERT INTO  items(name, pricePerItem, countable) VALUES (?,?,?)', new_item)
        conn.commit()


def get_item_by_name(name):
    if cursor.execute('SELECT * FROM items where name = ?', (name,)).fetchone():
        for item in cursor.execute('SELECT * FROM items where name = ?', (name,)):
            print(item)
    else:
        print("User doesn't exist")


def delete_item_by_name(name):
    if cursor.execute('SELECT * FROM items where name = ?', (name,)).fetchone():
        for i in cursor.execute('SELECT * FROM items where name = ?', (name,)):
            cursor.execute('Delete FROM items where name = ?', (name,))
            cursor.fetchall()
            conn.commit()
            print(f'Item {name} was deleted')
    else:
        print("Item doesn't exist")


def update_item(item, new_name=None, new_price=None, new_countable=None):
    if new_name and new_name != item.name:
        for i in cursor.execute('SELECT * FROM items where name = ?', (item.name,)):
            print(f'Item {item.name} updated to {new_name}')
            cursor.execute('UPDATE items SET name = ? WHERE name= ?', (new_name, item.name))

    if new_price and new_price != item.price:
        for i in cursor.execute('SELECT * FROM items where pricePerItem = ?', (item.price,)):
            print(f'Price {item.price} updated to {new_price}')
            cursor.execute('UPDATE items SET pricePerItem = ? WHERE pricePerItem= ?',
                           (new_price, item.price))

    if new_countable and new_countable != item.countable:
        for i in cursor.execute('SELECT * FROM items where countable = ?', (item.countable,)):
            cursor.execute('UPDATE items SET countable = ? WHERE countable= ?', (new_countable, item.countable))

    cursor.fetchall()
    conn.commit()


def get_all_items():
    for item in cursor.execute('SELECT * FROM items'):
        print(item)


'''Order functions'''


def create_order(order):

    cursor.executemany('INSERT INTO  orders (customer_id, item_id, date, completed) VALUES (?,?,?,?)', (order.customer_id,
                                                                                                        order.item_id,
                                                                                                        order.date,
                                                                                                        order.completed))
    conn.commit()


def get_order(order_id):
    order = cursor.execute('SELECT * FROM orders where order_id = ?', (order_id,)).fetchone()
    print(order)
    #if order:

            # cursor.execute('Delete FROM items where name = ?', (name,))
            # cursor.fetchall()
            # conn.commit()
            # print(f'Item {name} was deleted')





def delete(self):
    pass


def update(self):
    pass


def get_all_orders():
    for order in cursor.execute('SELECT * FROM orders'):
        print(order)


conn.commit()
