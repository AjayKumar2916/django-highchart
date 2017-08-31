from django.db import models

# Create your models here.
class RainFall(models.Model):
	month = models.CharField(max_length=128)
	centimeter = models.IntegerField()

	def __str__(self):
		return self.month
