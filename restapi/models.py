from django.db import models

# Create your models here.
class Fish(models.Model):
	name = models.CharField(max_length=100)
	species = models.CharField(max_length=200)
	weight = models.DecimalField(max_digits=8,decimal_places=3)
	length = models.DecimalField(max_digits=8,decimal_places=3)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	timestamp = models.DateTimeField(auto_now_add=True)
	picture = models.ImageField(upload_to ='media/', blank=True, null=True)
	#fish, species, weight, length, latitude, longitude and a timestamp