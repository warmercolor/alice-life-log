from django.urls import path
from .views import (
    EducationView,
    CourseView,
    JobView,
    TechnologyView,
    ProfessionalSummaryView,
)

urlpatterns = [
    path("education/", EducationView.as_view(), name="education-list-create"),
    path("courses/", CourseView.as_view(), name="course-list-create"),
    path("jobs/", JobView.as_view(), name="job-list-create"),
    path("technologies/", TechnologyView.as_view(), name="technology-list"),
    path(
        "professional-summary/",
        ProfessionalSummaryView.as_view(),
        name="professional-summary",
    ),
]
