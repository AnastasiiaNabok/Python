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
    def __init__(self, customerId, itemId, date):
        self.customerId = customerId
        self.itemId = itemId
        self.date = date
        self.completed = False
