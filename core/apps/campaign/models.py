from django.db import models
from core.apps.business.models import KollabBusiness


class KollabCampaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    campaign_thumbnail = models.ImageField(
        upload_to="campaign/thumbnails", blank=True, null=True
    )
    campaign_thumbnail_url = models.CharField(
        max_length=255, default="https://via.placeholder.com/150"
    )
    category = models.CharField(max_length=100)

    # exclude in CampaignCreateForm
    business = models.ForeignKey(KollabBusiness, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.campaign_thumbnail and not self.campaign_thumbnail_url:
            self.campaign_thumbnail_url = "https://via.placeholder.com/150"  # Default value if no thumbnail is set
        else:
            self.campaign_thumbnail_url = self.campaign_thumbnail.url
        super().save(*args, **kwargs)

    class Meta:
        db_table = "kollab_campaign"
        verbose_name = "Kollab Campaign"
        verbose_name_plural = "Kollab Campaigns"
