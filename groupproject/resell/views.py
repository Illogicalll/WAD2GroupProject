from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'resell/index.html')

def about(request):
    return render(request, 'resell/about.html')


def sell(request):
    return render(request, 'resell/sell.html')

def buy(request):
    return render(request, 'resell/buy.html')

def login(request):
    return render(request, 'resell/login.html')

def products(request):
    return render(request,'resell/products.html')


""" 
def product(request):
    return render(request, 'resell/{product_id}.html')
    
def user(request):
    return render(request, 'resell/{user_id}.html)
"""
