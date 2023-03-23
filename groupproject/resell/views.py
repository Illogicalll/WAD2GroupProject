from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from resell.forms import UserCreationForm, LoginForm, ListingCreationForm, ProductFilterForm
from resell.models import Product,CustomUser,Wishlist
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView
from django.db.models import Q

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

class buy(ListView):
    model = Product
    template_name = 'resell/listings.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        condition = self.request.GET.get('condition')
        sort = self.request.GET.get('sort')

        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))


        if category:
            queryset = queryset.filter(category=category)
        if condition:
            queryset = queryset.filter(condition=condition)
        if sort == 'Highest Price':
            queryset = queryset.order_by('-price')
        elif sort == 'Lowest Price':
            queryset = queryset.order_by('price')
        return queryset


    def get_context_data(self, **kwargs):
        context = super(buy, self).get_context_data(**kwargs)
        context['form'] = ProductFilterForm(self.request.GET or None)
        return context

    #return render(request, 'resell/listings.html', {'products':products})

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
    exists = False
    try:
        thisUser = CustomUser.objects.get(user_id=profile_id)
        exists = True
    except CustomUser.DoesNotExist:
        thisUser = None
    if exists:
        listings = Product.objects.filter(user_id=profile_id)
    else:
        listings = None
    
    return render(request, 'resell/profile.html', {'user':thisUser, 'listings':listings})

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

def purchasesuccess(request):
    return render(request,'resell/purchasesuccess.html')

def wishlist(request,profile_id):
    exists = False
    try:
        thisUser = CustomUser.objects.get(user_id=profile_id)
        exists = True
    except CustomUser.DoesNotExist:
        thisUser = None
    if exists:
        wishlist = Wishlist.objects.filter(user=profile_id)
    else:
        wishlist = None

    return render(request, 'resell/wishlist.html', {'wishlist':wishlist,'user':thisUser})

def purchase(request,product_id):
    try:
        item = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        item = None

    return render(request, 'resell/purchase', {'item':item})