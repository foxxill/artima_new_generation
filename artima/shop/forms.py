from .models import *
from django import forms


class ProductForm(forms.Form):
    fields = '__all__'
    