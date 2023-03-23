
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'groupproject.settings')

import django
django.setup()

from resell.models import CustomUser, Authentication_System, Category, Product, Wishlist, Order
from datetime import datetime, timedelta
from django.contrib.auth.models import CustomUser
from django.utils.text import slugify

def populate():
    categories = [
    {"name": "Electronics", "slug": "electronics"},
    {"name": "Fashion", "slug": "Fashion"},
    {"name": "Books", "slug": "books"},
    {"name": "Home & Garden", "slug": "home-and-garden"},
    {"name": "Toys & Games", "slug": "toys-and-games"},
    {"name": "Health & Beauty","slug":"healyh-and-beauty"},
    {"name": "Music & Movies","slug":"music-and-movies"}
    ]

    products = [
    {"name": "iPhone X", "category": "Electronics", "brand": "Apple", "condition": "Brand New", "price": 1000},
    {"name": "Macbook Pro", "category": "Electronics", "brand": "Apple", "condition": "Used", "price": 1500},
    {"name": "Dress", "category": "Fashion", "brand": "Zara", "condition": "Brand New", "price": 50},
    {"name": "T-Shirt", "category": "Fashion", "brand": "Nike", "condition": "Open Not Used", "price": 30},
    {"name": "Harry Potter", "category": "Books", "brand": "Scholastic", "condition": "Used", "price": 15},
    {"name": "Lord of the Rings", "category": "Books", "brand": "Houghton Mifflin", "condition": "Brand New", "price": 20},
    {"name": "Sofa", "category": "Home & Garden", "brand": "Ikea", "condition": "Used", "price": 400},
    {"name": "Bed", "category": "Home & Garden", "brand": "Pottery Barn", "condition": "Brand New", "price": 800},
    {"name": "Legos", "category": "Toys & Games", "brand": "Lego", "condition": "Brand New", "price": 50},
    {"name": "Board Game", "category": "Toys & Games", "brand": "Hasbro", "condition": "Open Not Used", "price": 30},
    {"name": "Patulin", "category": "Health & Beauty", "brand": "GlaxoSmithKline","condition": "Brand New", "price": 12},
    {"name": "Music CD", "category": "Music & Movies", "brand": "Unkonwn","condition": "Used", "price": 20}
]

    for category in categories:
        Category.objects.create(
            cateName=category["name"],
            slug=category["slug"],
            cateID=random.randint(1,1000)
        )

    for product in products:
        category = Category.objects.get(cateName=product["category"])
        Product.objects.create(
        prodName=product["name"],
        slug=slugify(product["name"]),
        Category=category,
        Brand=product["brand"],
        Condition=product["condition"],
        Price=product["price"],
        Description=" A test product",
        image="products/default.png",
        prodID=random.randint(1, 1000)
    )
        

users = []
for i in range(1,11):
     username = f"user{i}"
     if not CustomUser.objects.filter(username=username).exists():
         user = CustomUser.objects.create_user(
             username=f"user{i}",
             email=f"951975031@qq.com",
             password="123456789"
    )
         users.append(user)


for user in users:
    for product in Product.objects.all()[:5]:
        wishlist=Wishlist(
            user=user,
            Product=product
        )
        wishlist.save()

for user in users:
    wishlist = Wishlist.objects.filter(user=user).first()

if __name__ == '__main__':
    populate()
