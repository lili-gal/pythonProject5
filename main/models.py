from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(upload_to='uploads/', **NULLABLE, verbose_name='Изображение')
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена за покупку')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='Дата создания')
    last_modified_date = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description}'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    created_at = models.DateField(**NULLABLE, verbose_name='Изменения')

    def __str__(self):
        return f'{self.name} {self.description}'
