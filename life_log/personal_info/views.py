from rest_framework import generics
from rest_framework.response import Response
from .models import Personal
from .serializers import PersonalSerializer

class PersonalInfoView(generics.RetrieveUpdateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

    def get_object(self):
        return Personal.objects.first()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
