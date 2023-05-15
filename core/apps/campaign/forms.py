from core.apps.campaign.models import KollabCampaign
from core.apps.user.models import KollabUser
from django import forms
from django.contrib import auth



class CampaignCreateForm(forms.ModelForm):
    class Meta:
        model = KollabCampaign
        fields = ("name", "description", "start_date", "end_date", "bid", "category")