from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "campaign"
urlpatterns = [
    path("", views.CampaignHome.as_view(), name="campaign-home"),
    path("create/", views.CampaignCreate.as_view(), name="campaign-create"),
    path("<int:pk>/", views.CampaignDetails.as_view(), name="campaign-details"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)