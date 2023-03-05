from django.contrib import admin
from .models import User, Authentication_System, Category, Product, Wishlist, Order

# Register your models here.
admin.site.register([User, Authentication_System, Category, Product, Wishlist, Order])