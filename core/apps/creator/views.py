from django.shortcuts import render
from django.views.generic import TemplateView


class CreatorHome(TemplateView):
    template_name = "creator/creator_home.html"
