import sqlite3

conn = sqlite3.connect('order_DB.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class Order:
    def __init__(self, customer, item, date):
        self.customer = customer
        self.item = item
        self.date = date
        self.completed = False

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def get(self):
        pass
