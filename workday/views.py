from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Workday
from .forms import WorkdayForm
from .mixins import LoginRequiredMixin

def hello_world(request):
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


@login_required()
def new_workday(request):
	if request.method == 'POST':
		form = WorkdayForm(request.POST, request.FILES)
		if form.is_valid():
			work_day = form.save(commit=False)
			work_day.save()
			return HttpResponseRedirect('/')
	else:
		form = WorkdayForm()

	template = loader.get_template('new_worday.html')
	context = {
		'form': form
	}
	
	return HttpResponse(template.render(context, request))

class WorkdayList(ListView):
	model = Workday

class WorkdayDetail(LoginRequiredMixin, DetailView):
	model = Workday

