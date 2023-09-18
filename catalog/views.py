from django.shortcuts import render


def index(request):
    return render(request, 'catalog/home.html')


def index_2(request):
    return render(request, 'catalog/contacts/contacts.html')
