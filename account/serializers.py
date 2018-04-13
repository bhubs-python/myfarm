from rest_framework import serializers
from . import models
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('password', 'last_login', 'join_date', 'is_active', 'is_staff', 'groups', 'user_permissions',)
        #fields = '__all__'
