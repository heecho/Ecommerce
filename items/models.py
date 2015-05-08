from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	#user = models.ForeignKey(User)
	#order_id = models.ForeignKey(Order)
	def __str__(self):
		return self.name 

class Order(models.Model):
	status = models.IntegerField()
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Item)
	


