
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'groupproject.settings')

import django
django.setup()

from resell.models import CustomUser, Category, Product, Wishlist, Order
from datetime import datetime, timedelta
from django.utils.text import slugify

def populate():
    categories = [
    {"name": "Electronics", "slug": "electronics"},
    {"name": "Fashion", "slug": "fashion"},
    {"name": "Books", "slug": "books"},
    {"name": "Home & Garden", "slug": "home-and-garden"},
    {"name": "Toys & Games", "slug": "toys-and-games"},
    {"name": "Health & Beauty","slug":"healyh-and-beauty"},
    {"name": "Music & Movies","slug":"music-and-movies"}
    ]

    user1products = [
        {"name": "iPhone X", "category": "Electronics", "brand": "Apple", "condition": "Brand New and Sealed", "price": 1000, "description":"A really cool phone"},
        {"name": "Macbook Pro", "category": "Electronics", "brand": "Apple", "condition": "Signs of Usage", "price": 1500,"description": "The best laptop on the market"},
        {"name": "Dress", "category": "Fashion", "brand": "Zara", "condition": "Like New", "price": 50,"description": "Perfect for summer"},
    ]

    user2products = [
        {"name": "T-Shirt", "category": "Fashion", "brand": "Nike", "condition": "Brand New and Sealed", "price": 30,"description": "Dinosaur t shirt. Comes in small, medium or large"},
    ]

    user3products = [
        {"name": "Harry Potter", "category": "Books", "brand": "Scholastic", "condition": "Signs of Usage", "price": 15,"description": "Wizard book"},
        {"name": "Lord of the Rings", "category": "Books", "brand": "Houghton Mifflin", "condition": "Brand New and Sealed", "price": 20,"description": "wizard and dragon book"},        
    ]

    user4products = []

    user5products = [
        {"name": "Sofa", "category": "Home & Garden", "brand": "Ikea", "condition": "Broken/For Parts Only", "price": 400,"description": "really comfy"},
        {"name": "Bed", "category": "Home & Garden", "brand": "Pottery Barn", "condition": "Signs of Usage", "price": 800,"description": "super comfy"},
        {"name": "Legos", "category": "Toys & Games", "brand": "Lego", "condition": "Like New", "price": 50,"description": "build a building"},
        {"name": "Board Game", "category": "Toys & Games", "brand": "Hasbro", "condition": "Broken/For Parts Only", "price": 30,"description": "board game for 2 - 6 players"},
    ]

    user6products = [
        {"name": "Patulin", "category": "Health & Beauty", "brand": "GlaxoSmithKline","condition": "Like New", "price": 12,"description": "clears skin instantly"},
        {"name": "Music CD", "category": "Music & Movies", "brand": "Unkonwn","condition": "Brand New and Sealed", "price": 20,"description": "filled with #1's from the 60's to 2023"}
    ]

    user1wishlist = [
        "Harry Potter","Legos"
    ]

    user2wishlist = ["iPhone X","Macbook Pro"]

    user3wishlist = ["Music CD","Patulin"]

    user4wishlist = []
    user5wishlist=[]
    user6wishlist=[]

    users = {
        'User1' : {'products': user1products,'first_name': 'fnameuser1','last_name': 'lnameuser1', 'user_id' : 1, 'phone_number':'11111111111', 'password':'123456789', 'wishlist':user1wishlist},
        'User2' : {'products': user2products,'first_name': 'fnameuser2','last_name': 'lnameuser2', 'user_id' : 2, 'phone_number':'22222222222', 'password':'123456789', 'wishlist':user2wishlist},
        'User3' : {'products': user3products,'first_name': 'fnameuser3','last_name': 'lnameuser3', 'user_id' : 3, 'phone_number':'33333333333', 'password':'123456789', 'wishlist':user3wishlist},
        'User4' : {'products': user4products,'first_name': 'fnameuser4','last_name': 'lnameuser4', 'user_id' : 4, 'phone_number':'44444444444', 'password':'123456789', 'wishlist':user4wishlist},
        'User5' : {'products': user5products,'first_name': 'fnameuser5','last_name': 'lnameuser5', 'user_id' : 5, 'phone_number':'55555555555', 'password':'123456789', 'wishlist':user5wishlist},
        'User6' : {'products': user6products,'first_name': 'fnameuser6','last_name': 'lnameuser6', 'user_id' : 6, 'phone_number':'66666666666', 'password':'123456789', 'wishlist':user6wishlist},
    }

    for i,category in enumerate(categories):
        Category.objects.create(
            cateName=category["name"],
            slug=category["slug"],
            cateID=i
        )

    product_id = 1
    for user,user_data in users.items():
        u = add_user(user,user_data['first_name'],user_data['last_name'],user_data['user_id'],user_data['phone_number'],user_data['password'])
        for p in user_data['products']:
            p = add_product(p['name'],Category.objects.get(cateName=p['category']),user_data['user_id'],p['brand'],p['condition'],p['price'],p['description'],"products/placeholder-image.jpg", product_id)
            product_id += 1

    for user,user_data in users.items():
        for product in user_data["wishlist"]:
            p = add_wishlist(CustomUser.objects.get(user_id=user_data['user_id']),Product.objects.get(name=product))



def add_user(user, first_name, last_name, user_id, phone_number,password):
    u = CustomUser.objects.get_or_create(username=user, first_name=first_name, last_name=last_name,user_id=user_id,phone_number=phone_number,password=password)[0]
    u.save()
    return u

def add_product(name, category, user_id, brand, condition, price, description, image, product_id):
    p = Product.objects.get_or_create(name=name,category=category,brand=brand,user_id=user_id,condition=condition,price=price,description=description,image=image,product_id=product_id)
    return p

def add_wishlist(user,product):
    w = Wishlist.objects.get_or_create(user = user, Product = product)
    return w

if __name__ == '__main__':
    populate()
