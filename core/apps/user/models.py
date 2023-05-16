from django.db import models
from django.contrib.auth.models import AbstractUser
from core.apps.creator.models import KollabCreator
from core.apps.business.models import KollabBusiness


class KollabUser(AbstractUser):
    class Meta:
        db_table = "kollab_user"
        verbose_name = "Kollab User"
        verbose_name_plural = "Kollab Users"

    class Role(models.TextChoices):
        CREATOR = "CREATOR", "creator"
        BUSINESS = "BUSINESS", "business"

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25, verbose_name="password")
    role = models.CharField(max_length=50, choices=Role.choices)
    creator = models.OneToOneField(
        KollabCreator, on_delete=models.CASCADE, null=True, blank=True
    )
    business = models.OneToOneField(
        KollabBusiness, on_delete=models.CASCADE, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    user_thumbnail = models.ImageField(
        upload_to="user/thumbnails", blank=True, null=True
    )
    user_thumbnail_url = models.CharField(
        max_length=255, default="https://via.placeholder.com/150"
    )

    def save(self, *args, **kwargs):
        # Create a creator or business object depending on the role
        if self.role == self.Role.CREATOR:
            self.creator = KollabCreator.objects.create()
        elif self.role == self.Role.BUSINESS:
            self.business = KollabBusiness.objects.create()

        if not self.user_thumbnail and not self.user_thumbnail_url:
            self.user_thumbnail_url = "https://via.placeholder.com/150"  # Default value if no thumbnail is set
        else:
            self.user_thumbnail_url = self.campaign_thumbnail.url
        super().save(*args, **kwargs)
