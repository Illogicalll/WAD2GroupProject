from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from resell.forms import SignUpForm

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