from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import CustomLoginView, SignUpView

app_name = "user"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
]

