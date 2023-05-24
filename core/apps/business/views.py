from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.apps.campaign.models import KollabCampaign
from django.shortcuts import render


class BusinessHome(LoginRequiredMixin, TemplateView):
    template_name = "business/business_dashboard.html"
    def get(self, request):
        campaigns = KollabCampaign.objects.filter(business_id = self.request.user.business_id)
        return render(request, self.template_name, {'campaigns': campaigns})