from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress


def payment_success(request):
    return render(request, 'payment/payment_success.html', locals())


def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    shipped_cost = 20000
    totals = cart.cart_total() + shipped_cost

    if request.user.is_authenticated:
        # Checkout as logged in user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, 'payment/checkout.html',locals())
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html',locals())