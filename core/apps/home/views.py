from django.views import generic
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = "home/home.html"

