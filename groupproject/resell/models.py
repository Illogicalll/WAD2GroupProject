from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	BirthOfDate = models.DateTimeField()
	Address = models.CharField(max_length=1000,blank=True)
	UserID = models.PositiveIntegerField(unique=True)
	phoneNum = models.CharField(max_length=50,blank=True)
	creditRating = models.IntegerField()
	Email = models.CharField(max_length=100)
	joinedOn = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.FirstName
	

class Authentication_System(models.Model):
	Email = models.CharField(max_length=100)
	passWord = models.CharField(max_length=50)

	def __str__(self):
		return "AuthenSys: " + str(self)




class Category(models.Model):
	cateID = models.PositiveIntegerField(unique = True)
	cateName = models.CharField(max_length = 128)
	slug = models.SlugField(unique = True)

	def __str__(self):
		return self.cateName

PRODUCT_CONDITION = (
	("Brand New", "Brand New"),
	("Used", "Used"),
	("Open Not Used", "Open Not Used"),
)

class Product(models.Model):
	prodID = models.PositiveIntegerField(unique = True)
	prodName = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True)
	Category = models.ForeignKey(Category, on_delete=models.CASCADE)
	Brand = models.CharField(max_length = 100)
	Condition = models.CharField(max_length=50, choices = PRODUCT_CONDITION)
	Price = models.PositiveIntegerField()
	Description = models.TextField()
	image = models.ImageField(upload_to = "products")
	view_count = models.PositiveIntegerField(default=0)


	def __str__(self):
		return self.prodName
	
	
	

class Wishlist(models.Model):
	user = models.ForeignKey(
		User, on_delete=models.SET_NULL,null=True, blank=True)
	Product = models.ForeignKey(Product, on_delete=models.CASCADE)
	addAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Wishlist" + str(self.id)
	 

ORDER_STATUS = (
	("Order Resived", "Order Resived"),
	("Order processing", "Order processing"),
	("Order on the way", "Order on the way"),
	("Order Completed", "Order Completed"),
	("Order Canceled", "Order Canceled"),
)

class Order(models.Model):
	wishlist = models.OneToOneField(Wishlist, on_delete=models.CASCADE,blank=True)
	orderdBy = models.ForeignKey(
		User, on_delete=models.SET_NULL,null=True, blank=True)
	shippingAddr = models.CharField(max_length=200)
	subtotal = models.PositiveIntegerField()
	disacount = models.PositiveIntegerField()
	total = models.PositiveIntegerField()
	orederStatus = models.CharField(max_length=50, choices = ORDER_STATUS)
	createdAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Order: " + str(self.id)
	
