from rest_framework import serializers
from .models import Semester

class SemesterSerializer(serializers.Serializer):
    class Meta:
        model = Semester
        fields = ('branch','sem_name')
