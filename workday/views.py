from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
#from django.shortcuts import render

from .models import Workday
from .forms import WordayForm

# Create your views here.

def hello_world(request):
	#return render(request, 'index.html')
	work_day = Workday.objects.order_by('id')
	template = loader.get_template('index.html')
	context = { 
		'work_day': work_day 
	}
	return HttpResponse(template.render(context, request))

def workday_detail(request, pk):
	work_day = get_object_or_404(Workday, pk=pk)
	template = loader.get_template('workday_detail.html')
	context = {
		'work_day': work_day
	}

	return HttpResponse(template.render(context, request))

def new_workday(request):
	template = loader.get_template('new_worday.html')
	form = WordayForm()
	context = {
		'form': form
	}

	return HttpResponse(template.render(context, request))