"""
Creating serializers for core apps
"""

from rest_framework import serializers

from core.models import (
    Category,
    Channel,
    Comment,
)

from accounts.serializers import SimpleProfileSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class ChannelSerailizer(serializers.ModelSerializer):
    profile = SimpleProfileSerializer(read_only=True)
    class Meta:
        model = Channel
        fields = ['id', 'profile', 'name', 'channel_type', 'thumbnail', 'banner', 'about']

class ChannelCreateSerailizer(serializers.ModelSerializer):
    profile = SimpleProfileSerializer(read_only=True)
    class Meta:
        model = Channel
        fields = ['id', 'profile', 'name', 'channel_type', 'thumbnail', 'banner', 'about']
    
    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Channel.objects.create(
            profile_id=profile_id,
            **validated_data
        )


class ChannelEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'channel_type', 'thumbnail', 'banner', 'about']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","rating","body","created","edited"]
        read_only_fields = ["created", "edited"]
    
    def create(self, validated_data):
        pass