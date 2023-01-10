"""
Creating serializers for core apps
"""

from rest_framework import serializers

from core.models import (
    Category,
    Channel,
    Content,
    Comment,
)

from action.serializers import (
    SubscriptionSerilaizer,
    LikeSerializer,
    DislikeSerializer
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



class ContentSerializer(serializers.ModelSerializer):
    channel = ChannelSerailizer(read_only=True)
    class Meta:
        model = Content
        fields = "__all__"
        read_only_fields = ['channel']

    def create(self, validated_data):
        channel_id = self.context['channel_id']
        return Content.objects.create(channel_id=channel_id, **validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","rating","body","created","edited"]
        read_only_fields = ["created", "edited"]
    
    def create(self, validated_data):
        content_id = self.context['content_id']
        profile_id = self.context['profile_id']

        return Comment.objects.create(content_id=content_id, profile_id=profile_id, **validated_data)