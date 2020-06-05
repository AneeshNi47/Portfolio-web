from rest_framework import serializers
from jobs.models import Job
from jobs.models import ServicePoints


# jobs serializers
class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

# servicePoints serializers


class servicePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePoints
        fields = '__all__'
