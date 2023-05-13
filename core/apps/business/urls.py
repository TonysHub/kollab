from django.urls import path
from . import views

urlpatterns = [
    path('', views.BusinessHome, name='business-home'),
]
