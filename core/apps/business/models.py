from django.db import models


class KollabBusiness(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    thumbnail = models.ImageField(max_length=255, null=True, blank=True)
    

    class Meta:
        db_table = "kollab_business"
        verbose_name = "Kollab Business"
        verbose_name_plural = "Kollab Businesses"
