from django.urls import path
from .views import HomeView, SignUpView, LoginView, SuccessView
from django.contrib.auth.decorators import login_required


app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("success/", login_required(SuccessView.as_view()), name="success"),
]
