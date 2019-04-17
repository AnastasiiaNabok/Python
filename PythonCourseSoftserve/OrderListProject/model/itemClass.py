import sqlite3

conn = sqlite3.connect('order_DB.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

class Item:
    def __init__(self, name, price, countable=True):
        self.name = name
        self.countable = countable
        self.price = price
        self.create()

    def create(self):
        new_item = [(self.name, self.price, self.countable)]
        rows_count = cursor.execute('SELECT count(name) FROM items where name = ?',
                                    (self.name,)).fetchone()[0]
        if rows_count > 0:
            print('This  item already exist')
        else:
            cursor.executemany('INSERT INTO  items(name, pricePerItem, countable) VALUES (?,?,?)', new_item)
            conn.commit()

    @staticmethod
    def find_by_name(name):
        if cursor.execute('SELECT * FROM items where name = ?', (name,)).fetchone():
            for item in cursor.execute('SELECT * FROM items where name = ?', (name,)):
                print(tuple(item))
        else:
            print("User doesn't exist")

    @staticmethod
    def delete_by_name(name):
        if cursor.execute('SELECT * FROM items where name = ?', (name, )).fetchone():
            for item in cursor.execute('SELECT * FROM items where name = ?', (name,)):
                cursor.execute('Delete FROM items where name = ?', (name,))
                cursor.fetchall()
                conn.commit()
                print(f'Item {name} was deleted')
        else:
            print("Item doesn't exist")

    def update(self, new_name=None, new_price=None, new_countable=None):
        if new_name and new_name != self.name:
            for item in cursor.execute('SELECT * FROM items where name = ?', (self.name,)):
                print(f'Item {self.name} updated to {new_name}')
                cursor.execute('UPDATE items SET name = ? WHERE name= ?', (new_name, self.name))

        if new_price and new_price != self.price:
            for item in cursor.execute('SELECT * FROM items where pricePerItem = ?', (self.price,)):
                print(f'Price {self.price} updated to {new_price}')
                cursor.execute('UPDATE items SET pricePerItem = ? WHERE pricePerItem= ?',
                               (new_price, self.price))

        if new_countable and new_countable != self.countable:
            for item in cursor.execute('SELECT * FROM items where countable = ?', (self.countable,)):
                cursor.execute('UPDATE items SET countable = ? WHERE countable= ?', (new_countable, self.countable))

        cursor.fetchall()
        conn.commit()

    @staticmethod
    def show_all():
        for item in cursor.execute('SELECT * FROM items'):
            print(tuple(item))

