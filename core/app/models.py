from django.db import models

CATEGORIES = (
    ('other', 'Разное'), ('products', 'Продукты'), ('technique', 'Техника'), ('sport', 'Спорт'), ('clothes', 'Одежда'))


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2000, null=True, blank=True)
    image = models.TextField(verbose_name='Фото', max_length=200, null=False, blank=False)
    category = models.TextField(verbose_name='Категория', choices=CATEGORIES, default='other', null=False, blank=False)
    qty = models.DecimalField(verbose_name='Остаток', max_digits=15, decimal_places=0)
    cost = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.category}'
