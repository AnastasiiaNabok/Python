import sqlite3

conn = sqlite3.connect('order_DB.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

class Item:
    def __init__(self, name, price, countable=True):
        self.name = name
        self.countable = countable
        self.price = price

    def create(self):
        new_item = [(self.name, self.price, self.countable)]
        rows_count = cursor.execute('SELECT count(name) FROM items where name = ?',
                                    (self.name,)).fetchone()[0]
        if rows_count > 0:
            print('This  item already exist')
        else:
            cursor.executemany('INSERT INTO  items(name, pricePerItem, countable) VALUES (?,?,?)', new_item)
            conn.commit()

    def delete(self):
        pass

    def update(self):
        pass

    def get(self):
        pass

