from core.apps.campaign.models import KollabCampaign
from core.apps.user.models import KollabUser
from django import forms
from django.contrib import auth



class CampaignCreateForm(forms.ModelForm):
    class Meta:
        model = KollabCampaign
        fields = ("name", "description", "start_date", "end_date", "bid", "category")

    def __init__(self, *args, **kwargs):
        super(CampaignCreateForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'field--l'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter campaign name'
        self.fields['name'].widget.attrs['required'] = 'true'

        self.fields['description'].widget.attrs['class'] = 'field--l'
        self.fields['description'].widget.attrs['placeholder'] = 'Explanation about the campaign'
        self.fields['description'].widget.attrs['required'] = 'true'

        self.fields['start_date'].widget.attrs['class'] = 'field--l'
        self.fields['start_date'].widget.attrs['placeholder'] = 'Select starting date'
        self.fields['start_date'].widget.attrs['required'] = 'true'

        self.fields['end_date'].widget.attrs['class'] = 'field--l'
        self.fields['end_date'].widget.attrs['placeholder'] = 'Select ending date'
        self.fields['end_date'].widget.attrs['required'] = 'true'

        self.fields['bid'].widget.attrs['class'] = 'field--l'
        self.fields['bid'].widget.attrs['placeholder'] = 'Enter bid amount'
        self.fields['bid'].widget.attrs['required'] = 'true'

        self.fields['category'].widget.attrs['class'] = 'field--l'
        self.fields['category'].widget.attrs['placeholder'] = 'Select category'
        self.fields['category'].widget.attrs['required'] = 'true'
