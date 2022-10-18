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


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.DecimalField(verbose_name='Количество', max_digits=15, decimal_places=0)

    @property
    def name(self):
        return self.product.name

    @property
    def image(self):
        return self.product.image

    @property
    def cost(self):
        return self.product.cost

    def __str__(self):
        return f'{self.product} - {self.qty}'


class Order(models.Model):
    products = models.ManyToManyField('app.Product', related_name='orders', verbose_name='Заказ')
    name = models.CharField(verbose_name='Имя', max_length=100, null=False, blank=False)
    address = models.CharField(verbose_name='Адрес', max_length=100, null=False, blank=False)
    phone = models.DecimalField(verbose_name='Номер', max_digits=15, decimal_places=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')




