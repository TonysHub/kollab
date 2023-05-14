from django.db import models
from django.contrib.postgres.fields import ArrayField
from core.apps.creator.models import KollabCreator


class KollabBusiness(models.Model):
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'kollab_business'
        verbose_name = 'Kollab Business'
        verbose_name_plural = 'Kollab Businesses'



    # name = models.CharField(max_length=100)
    # campaign_id = models.ForeignKey('KollabCampaign', on_delete=models.CASCADE)
    # tier_id = models.ForeignKey('KollabTier', on_delete=models.CASCADE)
    # logo = models.ImageField(upload_to='business/logos')
    # cover = models.ImageField(upload_to='business/covers')


# class KollabCampaign(models.Model):
#     class Meta:
#         db_table = 'kollab_campaign'
#         verbose_name = 'Kollab Campaign'
#         verbose_name_plural = 'Kollab Campaigns'


#     id = models.AutoField(primary_key=True)
#     created = models.DateTimeField(auto_now_add=True)
#     deleted = models.DateTimeField(auto_now=True)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     bid = models.DecimalField(max_digits=10, decimal_places=2)
#     is_active = models.BooleanField(default=True)
#     category = models.CharField(max_length=100)
#     # logo = models.ImageField(upload_to='business/logos/campaign')
#     # cover = models.ImageField(upload_to='business/covers/campaign')
#     business_id = models.ForeignKey('KollabBusiness', on_delete=models.CASCADE)

#     creator_id = models.ForeignKey(KollabCreator, on_delete=models.CASCADE)
#     currency_id = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# # free or paid tier, etc.
# class KollabTier(models.Model):
#     class Meta:
#         db_table = 'kollab_tier'
#         verbose_name = 'Kollab Tier'
#         verbose_name_plural = 'Kollab Tiers'


    # tier = models.CharField(max_length=100, default='free')

    # def __str__(self):
    #     return self.name
