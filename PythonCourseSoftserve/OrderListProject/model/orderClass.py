import sqlite3

conn = sqlite3.connect('order_DB.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class Order:
    def __init__(self, customerId, itemId, date):
        self.customerId = customerId
        self.itemId = itemId
        self.date = date
        self.completed = False
        self.create()

    def create(self):
        cursor.executemany('INSERT INTO  customers(customerID, itemID, date, completed) VALUES (?,?,?)', (self.customerId,
                                                                                                 self.itemID, self.date,
                                                                                                 self.completed))
        conn.commit()

    def delete(self):
        pass

    def update(self):
        pass

    def get(self):
        pass
