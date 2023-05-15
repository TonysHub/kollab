from django.db import models
from core.apps.business.models import KollabBusiness


class KollabCampaign(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    business = models.ForeignKey(KollabBusiness, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "kollab_campaign"
        verbose_name = "Kollab Campaign"
        verbose_name_plural = "Kollab Campaigns"