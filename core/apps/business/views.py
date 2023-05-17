from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BusinessHome(LoginRequiredMixin, TemplateView):
    template_name = "business/business_dashboard.html"
