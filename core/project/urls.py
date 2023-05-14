from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.apps.home.urls")),
    path("creator/", include("core.apps.creator.urls")),
    path("business/", include("core.apps.business.urls")),
]
