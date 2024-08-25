from django.contrib import admin
from .models import ShippingAddress


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shipping_full_name', 'shipping_email', 'shipping_state', 'shipping_city', 'shipping_address',  'shipping_zipcode')


