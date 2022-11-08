from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.


def product_list (request):
    product_list = Product.objects.get_queryset().order_by('id')

    paginator = Paginator(product_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    context = {'product_list' : product_list}
    return render(request , 'product/product_list.html' , context)
    

def product_details (request , slug):
    
    product_details = Product.objects.get(PRDSlug=slug)
    context = {'product_details' : product_details}
    return render(request , 'product/product_details.html' , context)