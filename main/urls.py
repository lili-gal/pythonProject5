from django.conf.urls.static import static
from django.urls import path

from config import settings
from main.views import contacts, products, product

urlpatterns = [
    path('', products),
    path('contacts/', contacts),
    path('product/', product)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
