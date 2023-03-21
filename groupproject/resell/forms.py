from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import CustomUser
from .models import CustomUser, Product
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name' , 'phone_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            # if 'profile_picture' in self.cleaned_data:
            #     user.profile_picture = self.cleaned_data['profile_picture']
            #     user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    
    
class ListingCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'brand', 'category' , 'condition', 'price', 'description')

    def save(self, user_id, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save(user_id)
        return product