from django.db import models

# Create your models here.
class Workday(models.Model):
	suburb = models.CharField(max_length=255)
	date_start = models.DateTimeField(blank=True)
	date_finish = models.DateTimeField(blank=True)
	image = models.ImageField(blank=True)
	
	def __str__(self):
		return self.suburb

	#ayuda a los modelos
	class Meta:
		ordering = (id, )
