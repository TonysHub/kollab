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

    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25, verbose_name="password")
    role = models.CharField(max_length=50, choices=Role.choices)
    creator_id = models.OneToOneField(
        KollabCreator,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="creator_id",
    )
    business_id = models.OneToOneField(
        KollabBusiness,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="business_id",
    )
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    profile_image = models.ImageField(
        upload_to="user/profile",
        blank=True,
        null=True,
        default="user/profile/default.png",
    )
    profile_image_url = models.CharField(
        max_length=255, default="user/profile/default.png"
    )
    is_saved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.is_saved:
            if self.role == self.Role.CREATOR:
                creator = KollabCreator.objects.create()
                self.creator_id = creator
                creator.save()
            elif self.role == self.Role.BUSINESS:
                business = KollabBusiness.objects.create()
                self.business_id = business
                business.save()
            self.is_saved = True

        self.profile_image_url = self.profile_image.url
        super().save(*args, **kwargs)
