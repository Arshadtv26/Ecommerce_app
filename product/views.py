from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {'featured_products': featured_products,
               'latest_products': latest_products
               }
    return render(request, 'index.html', context)


def products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_list = Product.objects.order_by('priority')
    product_paginator = Paginator(product_list, 4)
    product_paginator_list = product_paginator.get_page(page)
    context = {'products': product_paginator_list}
    return render(request, 'products.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)
