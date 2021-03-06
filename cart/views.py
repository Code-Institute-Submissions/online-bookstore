from django.shortcuts import render, redirect, reverse
from django.contrib import messages



# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")
    
    
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[id] = 1
    request.session['cart'] = cart
    messages.add_message(request, messages.INFO, 'Hello world.')
    return redirect(request.META['HTTP_REFERER'])
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    cart[id] = 0
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))