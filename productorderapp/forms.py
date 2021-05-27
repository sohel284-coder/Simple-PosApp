from django import forms
from django.forms import widgets

PRODUCT_CHOICE = (
    ('1', 'juice'),
    ('2', 'water'),
    ('3', 'tea'),
)
class ProductForm(forms.Form):
    product_choice = forms.ChoiceField(
        choices=PRODUCT_CHOICE,
        label='Please Choose Your product',
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-control bg-white mt-2',
                'style': 'border-radius:6px; border:solid 2px blue',
                'id': 'choice',
                '@change': 'onChange', 
            }
        ),

    )
    
    
