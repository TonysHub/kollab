from core.apps.campaign.models import KollabCampaign
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class CampaignCreateForm(forms.ModelForm):
    class Meta:
        model = KollabCampaign
        fields = ("name", "description", "start_date", "end_date", "bid", "category")

    def __init__(self, *args, **kwargs):
        super(CampaignCreateForm,self).__init__(*args, **kwargs)