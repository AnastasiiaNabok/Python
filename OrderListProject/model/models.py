class Customer:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address


class Item:
    def __init__(self, name, price, countable=True):
        self.name = name
        self.countable = countable
        self.price = price


class Order:
    def __init__(self, customer_id, item_id, date):
        self.customer_id = customer_id
        self.item_id = item_id
        self.date = date
        self.completed = 0
