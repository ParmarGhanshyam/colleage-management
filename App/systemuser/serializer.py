from django.db import transaction
from rest_framework import serializers
from .models import SystermUser
from django.contrib.auth.models import User, auth

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SystermUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SystermUser
        fields = ('user','mobile', 'status', 'user_type')

    def create(self, validated_data):
        with transaction.atomic():
            user_instance = User.objects.create_user(username=self.context.get('username'),
                                                     password=self.context.get('password'))
            systemuser_instance = SystermUser.objects.create(user=user_instance, mobile=validated_data.get('mobile'),
                                                             status=validated_data.get('status'),
                                                             user_type=validated_data.get('user_type'))

            return systemuser_instance
