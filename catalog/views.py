from django.shortcuts import render
from catalog.models import Product


def base(request):
    return render(request, 'base.html')


def index(request):
    context = {
        'title': 'Main'
    }
    return render(request, 'catalog/index.html', context)


def page_with_products(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Catalog'
    }
    return render(request, 'catalog/page_with_products/page_with_products.html', context)


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    return render(request, 'catalog/contacts/contacts.html', context)
