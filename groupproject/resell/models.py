from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.utils.translation import gettext_lazy as _

# Create your models here.
	
class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, user_id, phone_number, password=None):
        if not username:
            raise ValueError(_('Users must have a username'))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_id=user_id,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, user_id, phone_number, password=None):
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            user_id=user_id,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
	username = models.CharField(_('username'), unique=True, max_length=30)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	user_id = models.PositiveIntegerField(_('user id'), unique=True)
	phone_number = models.CharField(_('phone number'), max_length=15, blank=True)
	joined_on = models.DateField(auto_now=True)
	is_active = models.BooleanField(_('active'), default=True)
	is_admin = models.BooleanField(_('admin'), default=False)
	# profile_picture = models.ImageField(null=True, blank=True, upload_to='static/pfps')
	objects = CustomUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'user_id', 'phone_number']

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

	# @property
	# def pfp(self):
	# 	if self.profile_picture and hasattr(self.profile_picture, 'url'):
	# 		return self.profile_picture.url
	# 	else:
	# 		return "/media/profile_pictures/user.png"

	def save(self, *args, **kwargs):
		if not self.pk:
			last_user = CustomUser.objects.all().order_by('-user_id').first()
			if last_user:
				self.user_id = last_user.user_id + 1
			else:
				self.user_id = 1
			super().save(*args, **kwargs)


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
		CustomUser, on_delete=models.SET_NULL,null=True, blank=True)
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
		CustomUser, on_delete=models.SET_NULL,null=True, blank=True)
	shippingAddr = models.CharField(max_length=200)
	subtotal = models.PositiveIntegerField()
	disacount = models.PositiveIntegerField()
	total = models.PositiveIntegerField()
	orederStatus = models.CharField(max_length=50, choices = ORDER_STATUS)
	createdAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Order: " + str(self.id)
	
