from django.urls import path
from .views import PersonalInfoView

urlpatterns = [path("personal/", PersonalInfoView.as_view(), name="personal-info")]
