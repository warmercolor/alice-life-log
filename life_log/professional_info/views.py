from rest_framework import generics
from rest_framework.response import Response
from .models import Education, Job, Technology, Course
from .serializers import (
    EducationSerializer,
    JobSerializer,
    TechnologySerializer,
    CourseSerializer,
)


class EducationView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class JobView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class TechnologyView(generics.ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class ProfessionalSummaryView(generics.GenericAPIView):
    def get(self, request):
        education = EducationSerializer(Education.objects.all(), many=True).data
        courses = CourseSerializer(Course.objects.all(), many=True).data
        jobs = JobSerializer(Job.objects.all(), many=True).data
        technologies = TechnologySerializer(Technology.objects.all(), many=True).data

        data = {
            "education": education,
            "courses": courses,
            "jobs": jobs,
            "technologies": technologies,
        }

        return Response(data)
