from rest_framework import serializers
from .models import Semstudent

class SemstudentSerializer(serializers.Serializer):
    class Meta:
        model = Semstudent
        fields = ('sem','user')
