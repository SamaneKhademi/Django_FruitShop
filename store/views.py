from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages


def index(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'index.html', locals())


def category(request, foo):
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', locals())
    except:
        messages.success(request, 'این دسته بندی وجود ندارد')
        return redirect('home')


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', locals())


def sale_products(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'sale_products.html', locals())
