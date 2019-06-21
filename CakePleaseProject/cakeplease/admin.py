from django.contrib import admin

from .models import Item
from .models import Order
from .models import User


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'minimal_order')
    search_fields = ('name', 'description')

    class Meta:
        verbose_name_plural = 'Items'
        verbose_name = 'Item'
        ordering = '-name'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'delivery', 'count', 'status', 'payment_method')
    search_fields = ('user', 'date', 'delivery', 'status')

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'
        ordering = 'status'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email')
    search_fields = ('user', 'date', 'delivery', 'status')

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = '-name'


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
