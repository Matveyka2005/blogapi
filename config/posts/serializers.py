from .models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at", "author")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", )
