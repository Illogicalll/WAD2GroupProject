from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from resell.forms import SignUpForm
from resell.models import Product

# Create your views here.

def index(request):
    return render(request, 'resell/index.html')

def about(request):
    return render(request, 'resell/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            f_name = form.cleaned_data.get('f_name')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../success/')
    else:
        form = SignUpForm()
    return render(request, 'resell/signup.html', {'form': form})

def signupsuccess(request):
    return render(request, 'resell/signupsuccess.html')

@login_required
def sell(request):
    return render(request, 'resell/sell.html')

def buy(request):
    return render(request, 'resell/listings.html')

def login(request):
    return render(request, 'resell/login.html')

def item(request,product_id):

    try:
        item = Product.objects.get(prodID=product_id)
    except Product.DoesNotExist:
        item = None

    return render(request, 'resell/item.html', {'item':item})
    
def profile(request):
    return render(request, 'resell/profile.html')

@login_required
def editprofile(request):
    return render(request,'resell/editprofile.html')

@login_required
def checkout(request):
    return render(request,'resell/checkout.html')