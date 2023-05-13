from django.db import models
from django.contrib.auth.models import AbstractUser
from core.apps.creator.models import KollabCreator
from core.apps.business.models import KollabBusiness


class KollabUser(AbstractUser):
    class Meta:
        db_table = 'kollab_user'
        verbose_name = 'Kollab User'
        verbose_name_plural = 'Kollab Users'

    class Role(models.TextChoices):
        CREATOR = "CREATOR", 'creator'
        BUSINESS = "BUSINESS", 'business'
    
    id = models.AutoField(primary_key=True)
    base_role = Role.CREATOR
    role = models.CharField(max_length=50, choices=Role.choices)
    creator_id = models.ForeignKey(KollabCreator, on_delete=models.CASCADE, null=True, blank=True)
    business_id = models.ForeignKey(KollabBusiness, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.role:
            self.role = self.base_role
        super().save(*args, **kwargs)

class KollabBusiness(KollabUser):
    class Meta:
        proxy = True

    base_role = KollabUser.Role.BUSINESS
    

