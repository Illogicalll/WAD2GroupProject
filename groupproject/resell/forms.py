from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import CustomUser
from .models import CustomUser
from django.contrib.auth import get_user_model

# class SignUpForm(UserCreationForm):
#     f_name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'f_name', 'email', 'password1', 'password2', )




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
        fields = ('username', 'first_name', 'last_name' ,'date_of_birth', 'phone_number')

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
        return user
    
    # def save(self, *args, **kwargs):
    #     user = super().save(commit=False)
    #     last_user = CustomUser.objects.all().order_by('-user_id').first()
    #     if last_user:
    #         self.user_id = last_user.user_id + 1
    #     else:
    #         self.user_id = 1
    #     super().save(*args, **kwargs)
    #     return user
