from core.apps.user.models import KollabUser
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CampaignCreateForm
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CampaignHome(TemplateView):
    template_name = "campaign/campaign_home.html"


class CampaignCreate(LoginRequiredMixin, CreateView):
    form_class = CampaignCreateForm
    template_name = "campaign/campaign_create.html"
    success_url = reverse_lazy("campaign-home")

    def form_valid(self, form):
        user = auth.get_user(self.request)
        if not user.is_authenticated:
            return redirect("login")
        
        user_id = user.pk
        business_id = KollabUser.objects.get(pk=user_id).business_id
        form.instance.business_id = business_id
        return super().form_valid(form)
