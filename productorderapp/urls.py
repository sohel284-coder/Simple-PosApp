from django.urls import path
from productorderapp.views import *


urlpatterns = [
    path('product-add', product_add, name='product_add'),
       
]

