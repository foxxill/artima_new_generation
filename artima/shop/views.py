from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *


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
    template = 'products.html'

    categories = Category.objects.order_by('id')
    category = Category.objects.get(slug = pk)
    products = Product.objects.filter(category = category)

    context = {
        'products' : products,
        'categories' : categories,
        'category' : category,

    }
    return render(request, template, context)


def search(request):
    template = 'products.html'

    if request.method == 'POST':
        products = Product.objects.filter()

    context = {
        'products' : products,
        'category' : category,

    }
    return render(request, template, context)


def profile(request):
    return render(request, 'customer_profile.html', context={})

def testing(request):
    template = 'testing_back.html'

    
    # product = Product.objects.get(id = 0)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('shop:t')
    else:
        products = Product.objects.all()
        form = ProductForm()

        context = {
        # 'product' : product,
        'products' : products,
        'sucsess' : False,
        'form' : form
        }

        return render(request, template, context)



def category_test(request):
    return render(request, 'category.html', context={})