import sqlite3
conn = sqlite3.connect('order_DB.db')
cursor = conn.cursor()

cursor.execute("create table if not exists customers (customer_id integer primary key, name, phoneNumber, address)")
cursor.execute("create table if not exists items (item_id integer primary key, name, countable, pricePerItem)")
cursor.execute("create table if not exists orders (order_id integer primary key, customerID, itemID, date, completed)")


customers = [('Ivan', '0501234358', 'Dnipro, Myra str., 14 app 56'),
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

cursor.executemany('INSERT INTO  items(name, countable, pricePerItem) VALUES (?,?,?)', items)

conn.commit()

conn.close()