from rest_framework import serializers
from jobs.models import Job


# jobs serializers
class jobSerializer(serializers.Serializer):
    class Meta:
        model = Job
        fields = '__all__'
