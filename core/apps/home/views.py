from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


class HomeView(generic.TemplateView):
    template_name = "home/home.html"

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")