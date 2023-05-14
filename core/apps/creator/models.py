from django.db import models


class KollabCreator(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = "kollab_creator"
        verbose_name = "Kollab Creator"
        verbose_name_plural = "Kollab Creators"
