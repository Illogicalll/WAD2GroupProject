from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'resell/index.html')

def about(request):
    return render(request, 'resell/about.html')


@login_required
def sell(request):
    return render(request, 'resell/sell.html')

def buy(request):
    return render(request, 'resell/listings.html')

def login(request):
    return render(request, 'resell/login.html')

def signup(request):
    return render(request,'resell/signup.html')

def item(request):
    return render(request, 'resell/item.html')
    
def profile(request):
    return render(request, 'resell/profile.html')

@login_required
def editprofile(request):
    return render(request,'resell/editprofile.html')

@login_required
def checkout(request):
    return render(request,'resell/checkout.html')






