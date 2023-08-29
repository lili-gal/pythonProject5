from django.shortcuts import render
from main.models import Product, Category


def contacts(request):
    return render(request, 'main/contacts.html')


def product(request):
    product = Product.objects.get(id=int(request.GET.get('id')))
    return render(request, 'main/product.html', context={"model": product})


def products(request):
    product = Product.objects.all()
    return render(request, 'main/products.html', context={"model": product})
