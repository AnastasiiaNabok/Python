from OrderListProject.model.DB_create import get_all_items, create_item, delete_item_by_name, update_item, \
    get_item_by_name, get_customer_by_name, delete_customer_by_name_and_phone, update_customer, get_all_customers, \
    create_customer, create_order
from OrderListProject.model.models import Customer, Item, Order

customer = Customer('Aliona', '087421868291', 'KIev blalbla')

new_item = Item('carrot cupcake', 350, True)

# create_customer(customer)
# get_customer_by_name('Anna')
# delete_customer_by_name_and_phone('Anna', '34')
# update_customer(customer, 'Anna', '34', 'eorrfdsk')
#get_all_customers()

# create_item(new_item)
# get_item_by_name('carrot cupcake')
# delete_item_by_name('cupcake')
# update_item(customer, 'Anna', '34', 'eorrfdsk')
#get_all_items()


order = Order(2, 4, '2019, 12, 5')


create_order(order)

