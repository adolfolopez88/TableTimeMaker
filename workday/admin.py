from django.contrib import admin
from .models import Workday, WorkdayClient
# Register your models here.
#admin.site.register(WorkDay)

@admin.register(Workday)
class AdminWorkday(admin.ModelAdmin):
	list_display = ('suburb', 'date_start')

@admin.register(WorkdayClient)
class AdminWorkdayClient(admin.ModelAdmin):
	list_display = ('client', 'workday', )