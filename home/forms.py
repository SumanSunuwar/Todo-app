from django import forms
from home.models import Todo
from django.db.models import fields
from django.contrib.auth.models import User



#class TodoForm(forms.Form):
#	title = forms.CharField()
#	description = forms.CharField()
#	date = forms.DateField()

class TodoForm(forms.ModelForm):
	def __init__(self, *args):
		self.user = args.pop('username', None)
		super(TodoForm, self).__init__(*args)

	def save(self, commit=True):
		obj = super(TodoForm, self).save(commit=False)
		obj.user = self.user
		if commit:
            obj.save()
        return obj



	class Meta:
		model = Todo
		fields = ["title", "description", "date", "todo_image", "is_greater_priority", "user"]