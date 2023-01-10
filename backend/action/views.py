from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from action.models import Subscription, Like, Dislike
from action.serializers import SubscriptionSerilaizer, LikeSerializer, DislikeSerializer
# Create your views here.
class SubscriptionModelViewSet(ModelViewSet):
    serializer_class = SubscriptionSerilaizer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        channel_id = self.kwargs['channel_pk']
        return Subscription.objects.filter(channel_id=channel_id)

class LikeModelViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        content_id = self.kwargs['content_pk']
        return Like.objects.filter(content_id=content_id)

class DislikeModelViewSet(ModelViewSet):
    serializer_class = DislikeSerializer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        content_id = self.kwargs['content_pk']
        return Dislike.objects.filter(content_id=content_id)