from jobs.models import Job, ServicePoints
from rest_framework import viewsets, permissions
from jobs.serializers import jobSerializer, servicePointsSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = jobSerializer


class ServicePointViewSet(viewsets.ModelViewSet):
    queryset = ServicePoints.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = servicePointsSerializer
