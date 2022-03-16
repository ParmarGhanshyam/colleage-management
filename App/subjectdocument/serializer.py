from rest_framework import serializers
from .models import SubjectDocument

class SubjectDocumentSerializer(serializers.Serializer):
    class Meta:
        model = SubjectDocument
        fields = ('subject','user','filefield','filename')
