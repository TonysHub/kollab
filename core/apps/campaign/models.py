from django.db import models
from core.apps.business.models import KollabBusiness
from django.conf import settings


class KollabCampaign(models.Model):
    class Meta:
        db_table = "kollab_campaign"
        verbose_name = "Kollab Campaign"
        verbose_name_plural = "Kollab Campaigns"

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(
        upload_to="campaign/thumbnails",
        blank=True,
        null=True,
        default="campaign/thumbnails/default.png",
    )
    thumbnail_url = models.CharField(
        max_length=255, default="campaign/thumbnails/default.png"
    )
    category = models.CharField(max_length=100)

    # Exclude in CampaignCreateForm
    business_id = models.ForeignKey(
        KollabBusiness, on_delete=models.CASCADE, db_column="business_id"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.thumbnail_url = self.thumbnail.url
        super().save(*args, **kwargs)

