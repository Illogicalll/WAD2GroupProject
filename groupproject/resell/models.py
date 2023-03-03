from django.db import models

# Create your models here.

class Category(models.Model):
	cateID = models.IntegerField(default = 20, unique = True)
	cateName = models.CharField(max_length = 128)

	def __str__(self):
		return self.cateID



class product(modles.Modle):
	prodID = models.IntegerField(default = 20, unique = True)
	prodName = models.CharField(max_length = 100)
	Brand = models.CharField(max_length = 100)
	Condition = models.CharField(max_length = 100)
	Price = models.IntegerField()
	Description = models.CharField(max_length = 10000)
	print("sadoifhsdofgisdhg")


	def __str__(self):
		return self.prodID


