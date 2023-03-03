from django.db import models

# Create your models here.

class Category(models.Model):
	cateID = models.IntegerField(default = 20, unique = True)
	cateName = modles.CharField(max_length = 128)

	def __str__(self):
		return self.cateID



class product(modles.Modle):
	prodID = modles.IntegerField(default = 20, unique = True)
	prodName = modles.CharField(max_length = 100)
	Brand = modles.CharField(max_length = 100)
	Condition = modles.CharField(max_length = 100)
	Price = modles.IntegerField()
	Description = modles.CharField(max_length = 10000)


	def __str__(self):
		retrun self.prodID


