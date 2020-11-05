from django import forms
from home.models import Todo
from django.db.models import fields

#class TodoForm(forms.Form):
#	title = forms.CharField()
#	description = forms.CharField()
#	date = forms.DateField()

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ("title", "description", "date", "todo_image", "is_greater_priority", "profile",)