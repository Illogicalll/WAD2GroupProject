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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['brand'].required = True
        self.fields['category'].required = True
        self.fields['condition'].required = True
        self.fields['price'].required = True
        self.fields['description'].required = True
        self.fields['image'].required = True

    class Meta:
        model = Product
        fields = ('name', 'brand', 'category' , 'condition', 'price', 'description', 'image')

    def save(self, user_id, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save(user_id)
        return product


class ProductFilterForm(forms.Form):
    category_choices = Product.objects.values_list('category', 'category').distinct()
    condition_choices = Product.objects.values_list('condition', 'condition').distinct()
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search...'}),required = False)
    category = forms.ChoiceField(choices=[('', 'All')] + list(category_choices), required=False)
    condition = forms.ChoiceField(choices=[('', 'All')] + list(condition_choices), required=False)
    sort = forms.ChoiceField(choices=[('','--Please Choose a Sorting Method--'),
                                        ('Highest Price', 'Highest Price'),
                                        ('Lowest Price', 'Lowest Price')], required = False)