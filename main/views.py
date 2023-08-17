from django.shortcuts import render


def contacts(request):
    return render(request, 'main/contacts.html')


def product(request):
    return render(request, 'main/product.html')


def products(request):
    return render(request, 'main/products.html', context={"range": range(100), "desc": "ОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписаниеОписание", "img": "kot.png"})
