from django.urls import path
from . import views

urlpatterns = [
    path("", views.BusinessHome.as_view(), name="business-home"),
]
