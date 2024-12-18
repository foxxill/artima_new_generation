from .models import *
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'author', 'image', 'description', 'color', 'theme', 'height', 'width', 'price']
