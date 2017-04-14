from django.contrib import admin
from .models import Workday
# Register your models here.
#admin.site.register(WorkDay)

@admin.register(Workday)
class AdminWorkday(admin.ModelAdmin):
	list_display = ('suburb', )
