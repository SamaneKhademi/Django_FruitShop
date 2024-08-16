from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Customer, Product, Order, Profile, BlogPost
from django.contrib.auth.models import User

admin.site.unregister(Group)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'password')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'quantity', 'address', 'phone', 'date', 'status')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_modified', 'phone', 'state', 'city', 'address', 'zipcode', 'old_cart')


# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]


# Unregister the old way
admin.site.unregister(User)

# Re_register the new way
admin.site.register(User, UserAdmin)


@admin.register(BlogPost)
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')