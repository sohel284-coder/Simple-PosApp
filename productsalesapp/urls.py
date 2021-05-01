from django.urls import path
from .views import *


urlpatterns = [
    path('', add_product_sale, name="add_product_sale"),
    path('register', register_page, name="register_page"),
    path('login', login_page, name='login_page'),
    path('logout', logout_user, name='logout_user'),
    path('details/<str:date>/', product_sale_report_details, name='product_sale_report_details'),
  
]