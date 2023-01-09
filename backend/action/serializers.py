"""
Serializers for user actions
"""

from rest_framework import serializers

from action.models import (
    Subscription,
    Like,
    Dislike,
)

class SubscriptionSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'
