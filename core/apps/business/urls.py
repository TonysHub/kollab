from django.urls import path
from . import views

app_name = "business"
urlpatterns = [
    path("dashboard/", views.BusinessHome.as_view(), name="business-dashboard"),
]
