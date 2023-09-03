from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("personal/", include('personal_info.urls')),
    path("professional/", include('professional_info.urls')),
]