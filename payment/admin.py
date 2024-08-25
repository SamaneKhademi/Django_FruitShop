from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shipping_full_name', 'shipping_email', 'shipping_state', 'shipping_city', 'shipping_address',  'shipping_zipcode')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'email', 'shipping_address', 'amount_paid', 'date_ordered')


@admin.register(OrderItem)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'user', 'quantity', 'price')