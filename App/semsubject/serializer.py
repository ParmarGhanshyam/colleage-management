from rest_framework import serializers
from .models import Semstudent
from django.contrib.auth.models import User, auth
from ..systemuser.serializer import UserSerializer,SystermUserSerializer
from ..sem.serializer import SemesterSerializer


class SemstudentSerializer(serializers.ModelSerializer):
    sem = SemesterSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Semstudent
        fields = ('sem','user')
