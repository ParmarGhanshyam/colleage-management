from rest_framework import serializers
from .models import SystermUser

class SystermUserSerializer(serializers.ModelSerializer):
    # users = serializers.RelatedField(source='user', read_only=True)

    class Meta:
        model = SystermUser
        fields = ('user','mobile','status','user_type')
