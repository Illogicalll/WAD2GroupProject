from django.contrib import admin
from .models import CustomUser, Authentication_System, Category, Product, Wishlist, Order

# Register your models here.
admin.site.register([CustomUser, Authentication_System, Category, Product, Wishlist, Order])