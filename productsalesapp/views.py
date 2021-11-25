 import datetime
from django.db.models import Sum, F
from django.shortcuts import render, HttpResponse, redirect
from .models import ProductSale, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import CustomRegisterForm, ProductSaleForm, CreateUserForm


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been Created for ' + user)
            return redirect('login_page')
    return render(request, 'register_page.html', {'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_product_sale')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login_page.html',   )
def logout_user(request):
    logout(request)
    return redirect('login_page')

def register_request(request):
    if request.method == 'POST':
        reg_form = CustomRegisterForm(request.POST)
        login_form = AuthenticationForm(request, data=request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            confirm_password = reg_form.cleaned_data['confirm_password']
            phone_number = reg_form.cleaned_data['phone_number']
            user = User.objects.create(username=username, email=email, password=password)
            login(request, user)
            return redirect ('add_product_sale')
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('add_product_sale')
            else:
                messages.error(request,"Invalid username or password.")
    else:
        login_form = AuthenticationForm()
        reg_form = CustomRegisterForm()
    return render(request, 'login.html', {'reg_form': reg_form, 'login_form': login_form})

@login_required(login_url='login_page')

def add_product_sale(request):
    user = request.user
    if request.method == 'POST':
        form = ProductSaleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number_of_carton = form.cleaned_data['number_of_carton']
            number_of_piece = form.cleaned_data['number_of_piece']
            carton_price_rate = form.cleaned_data['carton_price_rate']
            piece_price_rate = form.cleaned_data['piece_price_rate']
            return_carton = form.cleaned_data['return_carton']
            return_piece = form.cleaned_data['return_piece']
            total_product_sale = form.cleaned_data['total_product_sale']
            amount_of_sale = form.cleaned_data['amount_of_sale']
            ProductSale.objects.create(
                user=user,
                name=name,
                number_of_carton=number_of_carton,
                number_of_piece=number_of_piece,
                carton_price_rate=carton_price_rate,
                piece_price_rate=piece_price_rate,
                return_carton=return_carton,
                return_piece=return_piece,
                total_product_sale=total_product_sale,
                amount_of_sale=amount_of_sale,
            )
            return render(request, 'add_product_sale.html', {'msg': 'Information is successfully saved'})
    else:
        form = ProductSaleForm()
    products = ProductSale.objects.filter(user=request.user).values('created_at').order_by('-created_at').annotate(sum=Sum('amount_of_sale'))
    return render(request, 'add_product_sale.html', {'form': form, 'products': products })

@login_required(login_url='login_page')
def product_sale_report_details(request, date):
    products = ProductSale.objects.filter(created_at=date, user=request.user)
    return render(request, 'product_sale_report_details.html', {'products': products, 'date': date, })
