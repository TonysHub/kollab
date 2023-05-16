from typing import Any, Dict
from core.apps.user.models import KollabUser
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CampaignCreateForm
from django.contrib import auth
from django.utils.functional import SimpleLazyObject
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


class CampaignHome(TemplateView):
    template_name = "campaign/campaign_home.html"

class CampaignCreate(LoginRequiredMixin, CreateView):
    form_class = CampaignCreateForm
    template_name = "campaign/campaign_create.html"
    success_url = reverse_lazy("campaign-home")

    def form_valid(self, form):
        business_id = KollabUser.objects.filter(id=auth.get_user(self.request).id).values()[0]["business_id"]
        form.instance.business_id = business_id
        return super().form_valid(form)

