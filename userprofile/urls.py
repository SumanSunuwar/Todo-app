from django.urls import path
from userprofile.views import UserLoginView, UserSignupView, UserLogoutView

app_name = "user"

urlpatterns = [
	path("login/", UserLoginView.as_view(), name="login"),
	path("register/", UserSignupView.as_view(), name="register"),
	path("logout/", UserLogoutView, name="logout"),

]