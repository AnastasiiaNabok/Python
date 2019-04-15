from model.itemClass import Item
from model.customerClass import Customer
import sqlite3

conn = sqlite3.connect('order_DB.db')

cursor = conn.cursor()

new_customer = Customer('Anastasiia', '08742129390', 'dhhdhdhssllsdkn dfjdj')

new_customer.create()

# for customer in cursor.execute('SELECT * FROM customers'):
#   print(customer)

new_item = Item('carrot cupcake', 350, True)


# new_item.create()

# for item in cursor.execute('SELECT * FROM items'):
#    print(item)
def find_by_name1(name):
    if cursor.execute('SELECT * FROM customers where name = ?', (name,)).fetchone():
        for customer in cursor.execute('SELECT * FROM customers where name = ?', (name,)):
            print(customer)
    else:
        print("User doesn't exist")


# find_by_name1('Ivan')

# Customer.find_by_name('Ivan')


Customer.delete_by_name_and_phone('Anastasiia', '08742129390')

for customer in cursor.execute('SELECT * FROM customers'):
    print(customer)
