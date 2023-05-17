from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreatorHome.as_view(), name="creator-home"),
]
