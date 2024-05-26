from django.db import models


class Articles(models.Model):
    title = models.CharField( 'Название', max_length=50)
    anons = models.CharField( 'Анонс', max_length=250)
    full_text = models.TextField( 'Статья')
    date = models.DateTimeField( 'Дата публикации' )

    def __str__(self):
        return self.title

# models.py


class Order(models.Model):
    order_number = models.CharField('Номер заказа', max_length=100)
    customer_name = models.CharField('Заказчик', max_length=100)
    product_name = models.CharField('Продукт', max_length=100)
    order_date = models.DateTimeField('Дата публикации')
    status = models.CharField('Статус', max_length=50)

    def __str__(self):
        return self.order_number
