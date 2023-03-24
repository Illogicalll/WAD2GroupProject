from django.contrib import admin
from .models import CustomUser, Category, Product, Wishlist, Order

# Register your models here.
admin.site.register([CustomUser, Category, Product, Wishlist, Order])