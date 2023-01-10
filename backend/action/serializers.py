"""
Serializers for user actions
"""

from rest_framework import serializers

from action.models import (
    Subscription,
    Like,
    Dislike,
    View,
)

class SubscriptionSerilaizer(serializers.ModelSerializer):
    channel = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = Subscription
        fields = "__all__"

class SubscriptionCreateEditSerilaizer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()
    class Meta:
        model = Subscription
        fields = "__all__"
    
    def validate(self, attrs):
        channel = attrs.get("channel")
        profile_id = self.context['profile_id']
        subscription = Subscription.objects.filter(channel=channel, profile_id=profile_id)
        if subscription:
            raise serializers.ValidationError({"error":"alredy exist"})
        return attrs

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Subscription.objects.create(profile_id=profile_id, **validated_data)


class LikeSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = Like
        fields = '__all__'


class LikeCreateEditSerilaizer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = "__all__"
    
    def validate(self, attrs):
        content = attrs.get("content")
        profile_id = self.context['profile_id']
        like = Like.objects.filter(content=content, profile_id=profile_id)
        if like:
            raise serializers.ValidationError({"error":"alredy exist"})
        return attrs

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Like.objects.create(profile_id=profile_id, **validated_data)


class DislikeSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = Dislike
        fields = '__all__'


class DislikeCreateEditSerilaizer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Dislike
        fields = "__all__"
    
    def validate(self, attrs):
        content = attrs.get("content")
        profile_id = self.context['profile_id']
        dislike = Dislike.objects.filter(content=content, profile_id=profile_id)
        if dislike:
            raise serializers.ValidationError({"error":"alredy exist"})
        return attrs

    def create(self, validated_data):
        profile_id = self.context['profile_id']
        return Dislike.objects.create(profile_id=profile_id, **validated_data)


class ViewSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = View
        fields = "__all__"

class ViewCreateEditSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = View
        fields = "__all__"
    
    def validate(self, attrs):
        ip = attrs.get('ip')
        content = attrs.get('content')
        view = View.objects.filter(ip=ip, content=content)
        if view:
            raise serializers.ValidationError({
                "error":"Already viewed"
            })
        return attrs