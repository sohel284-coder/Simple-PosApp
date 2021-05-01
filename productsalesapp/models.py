from django.db import models
from django.contrib.auth.models import User

class ProductSale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=55, help_text='name of the product')
    number_of_carton = models.PositiveIntegerField(null=True)
    number_of_piece = models.PositiveIntegerField(null=True)
    carton_price_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    piece_price_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, )
    return_carton = models.PositiveIntegerField(null=True)
    return_piece = models.PositiveIntegerField(null=True, )
    total_product_sale = models.CharField(max_length=255, null=True, )
    amount_of_sale = models.DecimalField(max_digits=8, decimal_places=2, null=True, )
    created_at = models.DateField(auto_now_add=True, )

    def __str__(self):
        return self.name

class CustomUser(models.Model):
    name = models.CharField(max_length=25, )
    email = models.EmailField(null=True, )
    password = models.CharField(max_length=30,null=True, )
    conform_password = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=11, null=True)


    def __str__(self):
        return self.name

