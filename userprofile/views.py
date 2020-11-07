from django.shortcuts import reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from userprofile.forms import  CustomUserSignupForm

class UserLoginView(LoginView):
	template_name = "login.html"
	redirect_authenticated_user = False	
	authentication_form = AuthenticationForm

	def get_success_url(self):
		return reverse("home:todo_list")

def UserLogoutView(request):
	logout(request)
	return redirect(reverse('home:todo_list'))

		

class UserSignupView(CreateView):
	model = User
	form_class = CustomUserSignupForm
	template_name = "signup.html"

	def form_valid(self, form):
		super().form_valid(form)
		user = authenticate(
			username = form.cleaned_data.get("username"), 
			password = form.cleaned_data.get("password1"),
		)
		login(self.request, user)
		return redirect(reverse("home:todo_list"))

	def get_success_url(self):
		return reverse("user:login")

