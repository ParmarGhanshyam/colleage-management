from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.Serializer):
    class Meta:
        model = Subject
        fields = ('subject_name','sem_name')
