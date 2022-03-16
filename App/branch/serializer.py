from rest_framework import serializers
from .models import Branch


class BranchSerializer(serializers.Serializer):
    class Meta:
        model = Branch
        fields = ('name')
