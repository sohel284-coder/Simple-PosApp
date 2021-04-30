from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField(min_length=6, max_length=32)
    repeat_password = forms.CharField(min_length=6, max_length=32)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("This email is already in use")
        except User.DoesNotExist:
            return email

    def clean(self):
        super(RegistrationForm, self).clean()
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('repeat_password')
        if not password == re_password:
            raise forms.ValidationError('Passwords must match')

    def create(self, validated_data):
        # create a auth user
        user = User.objects.create_user(
            username=validated_data['email'], email=validated_data['email'], password=validated_data['password']
        )
        return user

class CustomRegisterForm(forms.Form):
    username = forms.CharField(max_length=55, )
    email = forms.EmailField()
    password = forms.CharField(min_length=2, max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(min_length=2, max_length=30, widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=11, )


class ProductSaleForm(forms.Form):
    name = forms.CharField(max_length=55, )
    number_of_carton = forms.IntegerField()
    number_of_piece = forms.IntegerField()
    carton_price_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    piece_price_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    return_carton = forms.IntegerField()
    return_piece = forms.IntegerField()
    total_product_sale = forms.CharField(max_length=255)
    amount_of_sale = forms.DecimalField(max_digits=8, decimal_places=4, )

   
