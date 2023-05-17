from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm


class HomeView(generic.TemplateView):
    template_name = "home/home.html"


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
