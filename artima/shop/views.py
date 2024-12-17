from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home(request):
    """главная"""
    template = 'home.html'

    categories = Category.objects.order_by('id')

    context = {
        'categories' : categories,
        }
    return render(request, template, context)

def category(request, pk):
    """вывод категорий на странице"""
    template = 'category.html'

    categories = Category.objects.order_by('id')
    category = Category.objects.get(slug = pk)
    products = Product.objects.filter(category = category)

    context = {
        'products' : products,
        'categories' : categories,

    }
    return render(request, template, context)

def profile(request):
    return render(request, 'customer_profile.html', context={})

def testing(request):
    return render(request, 'testing_back.html', context={})

def category_test(request):
    return render(request, 'category.html', context={})