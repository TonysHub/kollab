from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import CustomLoginView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]