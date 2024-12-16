from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', context={})

def profile(request):
    return render(request, 'customer_profile.html', context={})

def testing(request):
    return render(request, 'testing_back.html', context={})

def category_test(request):
    return render(request, 'category.html', context={})