from django.urls import path
from . import views

app_name = "campaign"
urlpatterns = [
    path("", views.CampaignHome.as_view(), name="campaign-home"),
    path("create/", views.CampaignCreate.as_view(), name="campaign-create"),
]
