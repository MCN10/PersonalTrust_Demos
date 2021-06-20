from django.forms import ModelForm
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):
	creator = forms.CharField()

	class Meta:
		model = Task
		fields = '__all__'

		widgets = {
			'due_date': DateInput(),
		}
		readonly = ('creator',)
