from itertools import product

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from homeapp.models import Product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#create cart_id using session
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request):
    if request.method == 'POST':
        # gives list of id of inputs
        list_of_products_id = request.POST.getlist('products')
        for x in list_of_products_id:
            #y = Product.objects.get(id=x)
            try:
                product = Product.objects.get(id=x)
                cart=Cart.objects.get(cart_id = _cart_id(request))

            except Cart.DoesNotExist:
                cart=Cart.objects.create(
                cart_id=_cart_id(request))
            cart.save()
            try:
                cart_item=CartItem.objects.get(product=product,cart=cart)
                if cart_item.quantity < cart_item.product.stock:
                    cart_item.quantity += 1
                cart_item.save()
            except CartItem.DoesNotExist:
                cart_item = CartItem.objects.create(
                product=product,
                quantity= 1,
                cart=cart
                )
                cart_item.save()
    return redirect('cartapp:cart_detail')

# cart_details

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        #puser=puser
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

#add item


def add_item(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id = _cart_id(request))

    except Cart.DoesNotExist:
        cart=Cart.objects.create(
        cart_id=_cart_id(request))
    cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity= 1,
            cart=cart
        )
        cart_item.save()
    return redirect('cartapp:cart_detail')


#delete cart item
def remove_item(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def delete_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cartapp:cart_detail')
