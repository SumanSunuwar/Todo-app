from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.forms import User

class CutomAuthenticationForm(AuthenticationForm):
	pass

class CustomUserSignupForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = (
			"username", 
			"email", 
			"password1", 
			"password2"
		)