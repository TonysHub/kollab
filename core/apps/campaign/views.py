from core.apps.user.models import KollabUser
from core.apps.campaign.models import KollabCampaign
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CampaignCreateForm
from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


class CampaignHome(TemplateView):
    template_name = "campaign/campaign_home.html"
    def get(self, request):
        campaigns = KollabCampaign.objects.all()
        return render(request, self.template_name, {'campaigns': campaigns})


class CampaignCreate(LoginRequiredMixin, CreateView):
    form_class = CampaignCreateForm
    template_name = "campaign/campaign_create.html"
    success_url = reverse_lazy("campaign:campaign-home")

    def form_valid(self, form):
        user = auth.get_user(self.request)
        if not user.is_authenticated:
            return redirect("login")

        user_id = user.pk
        business_id = KollabUser.objects.get(pk=user_id).business_id
        form.instance.business_id = business_id
        return super().form_valid(form)


class CampaignDetails(LoginRequiredMixin, TemplateView):
    template_name = "campaign/campaign_details.html"
    def get(self, request, pk):
        campaign = KollabCampaign.objects.get(pk=pk)
        return render(request, self.template_name, {'campaign': campaign})