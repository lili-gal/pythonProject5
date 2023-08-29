from django.urls import path
from main.views import contacts, products, product

urlpatterns = [
    path('', products),
    path('contacts/', contacts),
    path('product/', product)
]
