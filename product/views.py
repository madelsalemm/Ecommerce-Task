from django.shortcuts import redirect, render
from .models import Product 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

######################################
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
######################################
########## filter ###########
from .filters import ProductFilter
######### filter ###########
# Create your views here.


def product_list (request):
    product_list = Product.objects.get_queryset().order_by('-price')
    
    #Filter
    filter = ProductFilter(request.GET, queryset=product_list)
    product_list = filter.qs
    #Filter

    paginator = Paginator(product_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    context = {'product_list' : product_list , 'filter' : filter}
    return render(request , 'product/product_list.html' , context)
    

def product_details (request , id):
    
    product_details = Product.objects.get(id=id)
    context = {'product_details' : product_details}
    return render(request , 'product/product_details.html' , context)

#########################################
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)    
    return redirect("product:product_list")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("product:cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product:cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("product:cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("product:cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'product/cart_detail.html')


