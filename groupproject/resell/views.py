from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from resell.forms import UserCreationForm, LoginForm, ListingCreationForm
from resell.models import Product,CustomUser
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def index(request):
    thisUser = request.user
    return render(request, 'resell/index.html', {'user':thisUser})

def about(request):
    return render(request, 'resell/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            auth_login(request, new_user)
            return redirect('../signupsuccess/')
    else:
        form = UserCreationForm()
    return render(request, 'resell/signup.html', {'form': form})

def signupsuccess(request):
    return render(request, 'resell/signupsuccess.html')

def loginsuccess(request):
    return render(request, 'resell/loginsuccess.html')

def buy(request):
    products = Product.objects.all()[:5]

    return render(request, 'resell/listings.html', {'products':products})

def login(request):
    return render(request, 'resell/login.html')

def item(request,product_id):
    try:
        item = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        item = None

    return render(request, 'resell/item.html', {'item':item})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('../loginsuccess/')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'resell/login.html', {'form': form})
    
def profile(request,profile_id):
    try:
        thisUser = CustomUser.objects.get(user_id=profile_id)
    except CustomUser.DoesNotExist:
        thisUser= None
    
    return render(request, 'resell/profile.html',{'user':thisUser})

def myprofile(request):
    try:
        thisUser = CustomUser.objects.get(user_id=request.user.user_id)
    except CustomUser.DoesNotExist:
        thisUser= None
    
    return render(request, 'resell/profile.html',{'user':thisUser})

def logout(request):
    auth_logout(request)
    return render(request, 'resell/logoutsuccess.html')

@login_required(login_url='../login/')
def editprofile(request):
    return render(request,'resell/editprofile.html')

@login_required(login_url='../login/')
def checkout(request):
    return render(request,'resell/checkout.html')

@login_required(login_url='../login/')
def newlisting(request):
    if request.method == 'POST':
        form = ListingCreationForm(request.POST)
        if form.is_valid():
            form.save(user_id=request.user.user_id)
            return redirect('../listingsuccess/')
    else:
        form = ListingCreationForm()
    return render(request, 'resell/newlisting.html', {'form': form})

def listingsuccess(request):
    return render(request,'resell/listingsuccess.html')