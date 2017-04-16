from __future__ import unicode_literals

from django.db import models
from clients.models import Client

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
		ordering = ['id' ]

class WorkdayClient(models.Model):
	client = models.ForeignKey(Client)
	workday = models.ForeignKey(Workday)
	
	#class Meta:
	#	verbose_name = ''

	def __str__(self):
		return '%s %s' % (self.client.name,  self.workday.suburb)


