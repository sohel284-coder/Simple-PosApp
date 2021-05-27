from productorderapp.forms import PRODUCT_CHOICE
from django.db import models

# Create your models here.

class Product(models.Model):
    PRODUCT_CHOICE = (
        ('1', 'Juice'),
        ('2', 'Water',),
        ('3', 'Tea', ),
    )
    product_name = models.CharField(choices=PRODUCT_CHOICE, max_length=25, )
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, )
    