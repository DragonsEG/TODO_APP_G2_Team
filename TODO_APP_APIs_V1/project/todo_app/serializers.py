from rest_framework import serializers
from .models import CustomUser,ListItem

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name','email','department','Permission_user']


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['pk','item','status']