from core.apps.campaign.models import KollabCampaign
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class CampaignCreateForm(forms.ModelForm):
    class Meta:
        model = KollabCampaign
        exclude = [
            "business_id",
            "is_active",
            "created_at",
            "updated_at",
            "thumbnail_url",
        ]
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
        }
