from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from resell.forms import UserCreationForm, UserChangeForm, LoginForm, ListingCreationForm, ProductFilterForm
from resell.models import Product,CustomUser,Wishlist
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView
from django.db.models import Q
from django.forms.models import model_to_dict

# Create your views here.

def index(request):
    thisUser = request.user
    return render(request, 'resell/index.html', {'user':thisUser})

def about(request):
    return render(request, 'resell/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
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


@login_required(login_url='../login/')
def editprofile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('../editprofilesuccess/')
    else:
        form = UserChangeForm()
    return render(request, 'resell/editprofile.html', {'form': form})

def editprofilesuccess(request):
    return render(request, 'resell/editprofilesuccess.html', {'user':request.user})

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
    seller = None
    sellerisviewer = None
    isinwishlist = False
    loggedin = False

    try:
        item = Product.objects.get(product_id=product_id)
        seller = CustomUser.objects.get(user_id=item.user_id)
        if request.user.is_authenticated:
            request.session['product_id'] = product_id
            sellerisviewer = request.user.user_id == seller.user_id
            loggedin = True
    except Product.DoesNotExist:
        item = None
    try:
        if Wishlist.objects.filter(user=request.user, Product=item).exists():
            isinwishlist = True
    except:
        pass

    return render(request, 'resell/item.html', {'item':item,'seller':seller,'ownitem':sellerisviewer,'loggedin':loggedin,'inwishlist':isinwishlist})

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
    valid = False
    try:
        thisUser = CustomUser.objects.get(user_id=profile_id)
        exists = True
        valid = profile_id == request.user.user_id
    except CustomUser.DoesNotExist:
        thisUser = None
    if exists:
        listings = Product.objects.filter(user_id=profile_id)
    else:
        listings = None
    return render(request, 'resell/profile.html', {'user':thisUser, 'listings':listings, 'valid':not valid})

@login_required(login_url='../login/')
def myprofile(request):
    try:
        thisUser = CustomUser.objects.get(user_id=request.user.user_id)
    except CustomUser.DoesNotExist:
        thisUser= None
    return render(request, 'resell/profile.html',{'user':thisUser, 'valid':True})

def logout(request):
    auth_logout(request)
    return render(request, 'resell/logoutsuccess.html')


@login_required(login_url='../login/')
def checkout(request):
    return render(request,'resell/checkout.html')

@login_required(login_url='../login/')
def newlisting(request):
    if request.method == 'POST':
        form = ListingCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(user_id=request.user.user_id)
            return redirect('../listingsuccess/')
    else:
        form = ListingCreationForm()
    return render(request, 'resell/newlisting.html', {'form': form})

def listingsuccess(request):
    return render(request,'resell/listingsuccess.html')

@login_required(login_url='../login/')
def wishlist(request):
    exists = False
    user = request.user
    try:
        thisUser = CustomUser.objects.get(user_id=user.user_id)
        exists = True
    except CustomUser.DoesNotExist:
        thisUser = None
    if exists:
        wishlistItem = Wishlist.objects.filter(user=user)
        products = []
        for item in wishlistItem:
                product = model_to_dict(item.Product)
                products.append(product)
    else:
        products = None

    return render(request, 'resell/wishlist.html', {'products':products,'user':thisUser})

@login_required
def purchasesuccess(request):
    if 'product_id' in request.session:
        product_id = request.session['product_id']

    Product.objects.filter(product_id=product_id).delete()

    return render(request,'resell/purchasesuccess.html')

def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        wishlist_item = Wishlist(user=request.user, Product=Product.objects.get(product_id=product_id))
        wishlist_item.save()
        return redirect((f'../item/{product_id}'))
    else:
        return redirect((f'../item/{product_id}'))
    
def itemaddtowishlistsuccess(request):
    return render(request,'resell/itemaddsuccess.html')

def removefromwishlist(request):

    if 'product_id' in request.session:
        product_id = request.session['product_id']

    Wishlist.objects.filter(Product=Product.objects.get(product_id=product_id)).delete()

    return render(request,'resell/wishlist.html')