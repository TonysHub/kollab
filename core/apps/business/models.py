from django.db import models

class KollabBusiness(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = "kollab_business"
        verbose_name = "Kollab Business"
        verbose_name_plural = "Kollab Businesses"

