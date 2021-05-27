from django.shortcuts import render
from productorderapp.forms import ProductForm

# Create your views here.

def product_add(request):
    form = ProductForm()
    return render(request, 'product_stock_management/product_add.html', {'form': form})
