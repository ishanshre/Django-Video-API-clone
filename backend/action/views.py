from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from action.models import (
    Subscription, 
    Like, 
    Dislike, 
    View
)
from action.serializers import (
    SubscriptionSerilaizer, 
    SubscriptionCreateEditSerilaizer,
    LikeSerializer, 
    LikeCreateEditSerilaizer,
    DislikeSerializer,
    DislikeCreateEditSerilaizer,
    ViewSerializer
)
# Create your views here.
class SubscriptionModelViewSet(ModelViewSet):
    serializer_class = SubscriptionSerilaizer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        channel_id = self.kwargs['channel_pk']
        return Subscription.objects.filter(channel_id=channel_id)

class SubscriptionCreateEdtModelViewSet(ModelViewSet):
    serializer_class = SubscriptionCreateEditSerilaizer
    http_method_names = ['get','post','put','patch','options','head']
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Subscription.objects.filter(profile=self.request.user.profile)
    
    def get_serializer_context(self):
        return {"profile_id":self.request.user.profile.id}
    

class LikeModelViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        content_id = self.kwargs['content_pk']
        return Like.objects.filter(content_id=content_id)

class LikeCreateEdtModelViewSet(ModelViewSet):
    serializer_class = LikeCreateEditSerilaizer
    http_method_names = ['get','post','put','patch','options','head']
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Like.objects.filter(profile=self.request.user.profile)
    
    def get_serializer_context(self):
        return {"profile_id":self.request.user.profile.id}

class DislikeModelViewSet(ModelViewSet):
    serializer_class = DislikeSerializer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        content_id = self.kwargs['content_pk']
        return Dislike.objects.filter(content_id=content_id)

class DislikeCreateEdtModelViewSet(ModelViewSet):
    serializer_class = DislikeCreateEditSerilaizer
    http_method_names = ['get','post','put','patch','options','head']
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Dislike.objects.filter(profile=self.request.user.profile)
    
    def get_serializer_context(self):
        return {"profile_id":self.request.user.profile.id}

class ViewModelViewSet(ModelViewSet):
    serializer_class = DislikeSerializer
    http_method_names = ['get','options','head']
    def get_queryset(self):
        content_id = self.kwargs['content_pk']
        return View.objects.filter(content_id=content_id)