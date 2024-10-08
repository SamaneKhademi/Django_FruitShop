from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    pre_totals = cart.cart_total()
    shipped_cost = 20000
    totals = cart.cart_total() + shipped_cost
    return render(request, 'cart_summary.html', locals())

def cart_add(request):
    #  Get the cart
    cart = Cart(request)
    # Test for post
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get cart quantity
        cart_quantity = cart.__len__()

        # Return response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, 'محصول موردنظر به سبد خرید شما اضافه شد.')
        return response

def cart_update(request):
    pass
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        messages.success(request, 'سبد خرید شما بروزرسانی شد.')
        return response
        #return redirect('cart_summary')

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete function in cart
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        messages.success(request, 'محصول موردنظر از سبد خرید شما حذف شد.')
        # return redirect('cart_summary')
        return response

