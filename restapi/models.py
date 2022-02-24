from django.db import models

# Create your models here.
class Fish(models.Model):
	name = models.CharField(max_length=100)
	species = models.CharField(max_length=200)
	# weight = models.DecimalField()
	# length = models.DecimalField()
	# latitude = models.DecimalField()
	# longitude = models.DecimalField()
	timestamp = models.DateTimeField(auto_now_add=True)
	#fish, species, weight, length, latitude, longitude and a timestamp