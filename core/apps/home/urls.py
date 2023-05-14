from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("success/", views.SuccessView.as_view(), name="success"),
]
