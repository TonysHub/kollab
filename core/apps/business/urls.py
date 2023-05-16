from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.BusinessHome.as_view(), name="business-dashboard"),
]
