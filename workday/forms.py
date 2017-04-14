from django import forms
from .models import Workday

class WordayForm(forms.ModelForm):
	class Meta:
		model = Workday
		fields = '__all__' 
		