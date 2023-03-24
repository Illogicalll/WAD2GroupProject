from django.db import models
from django.conf import settings
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

    def create_superuser(self, username, first_name, last_name, user_id, phone_number, password=None, profilepicture=None):
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
	profilepicture = models.ImageField(_('profilepicture'), upload_to = "profiles", blank=True, null=True)
	objects = CustomUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'user_id', 'phone_number', 'profilepicture']

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

	@property
	def pfp(self):
		try:
			print(self.profilepicture.url)
			return True
		except:
			return False

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
	("Brand New and Sealed", "Brand New and Sealed"),
	("Like New", "Like New"),
	("Signs of Usage", "Signs of Usage"),
	("Broken/For Parts Only", "Broken/For Parts Only"),
)

PRODUCT_CATEGORY = (
	("Home and Furniture", "Home and Furniture"),
	("Technology", "Technology"),
	("Clothing", "Clothing"),
	("Other", "Other"),
)

class Product(models.Model):
	product_id = models.PositiveIntegerField(_('id'), unique = True, default=0)
	user_id = models.PositiveIntegerField(blank=True, default=0)
	name = models.CharField(_('name'), blank=True, max_length = 100)
	category = models.CharField(_('category'), blank=True, max_length=50, choices = PRODUCT_CATEGORY)
	brand = models.CharField(_('brand'), blank=True, max_length = 100)
	condition = models.CharField(_('condition'), max_length=50, blank=True, choices = PRODUCT_CONDITION)
	price = models.PositiveIntegerField(_('price'), blank=True, default=0)
	description = models.TextField(_('description'), blank=True, default="")
	image = models.ImageField(_('image'), upload_to = "products", blank=True, null=True)
	view_count = models.PositiveIntegerField(default=0)

	REQUIRED_FIELDS = ['name', 'brand','category', 'condition', 'price', 'description']

	def __str__(self):
		return self.name

	def save(self, user_id=None, *args, **kwargs):
		if not self.pk:
			last_product = Product.objects.all().order_by('-product_id').first()
			if last_product:
				self.product_id = last_product.product_id + 1
			else:
				self.product_id = 1
			if user_id:
				self.user_id = user_id
			super().save(*args, **kwargs)
	
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
	
