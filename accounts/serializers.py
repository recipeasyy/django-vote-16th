from rest_framework import serializers
from django.contrib.auth import login

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'name', 'part', 'team']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'], username=validated_data['username'],
            name=validated_data['name'], part=validated_data['part'], team=validated_data['team'])
        user.set_password(validated_data['password'])
        user.save()
        login(self.context['request'], user)
        return user