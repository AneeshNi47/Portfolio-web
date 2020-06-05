from jobs.models import Job
from rest_framework import viewsets, permissions
from jobs.serializers import jobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = jobSerializer
