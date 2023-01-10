from django.shortcuts import render
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import IsAdmnOrReadOnly, IsOwnerOrReadOnly, IsChannelOwnerOrReadOnly
from core.serializers import (
    CategorySerializer,
    ChannelSerailizer,
    ChannelCreateSerailizer,
    ChannelEditSerializer,
    ContentSerializer,
    CommentSerializer,
)
from core.models import (
    Category,
    Channel,
    Content,
    Comment,
)
# Create your views here.


class CategoryApiModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdmnOrReadOnly]
    queryset = Category.objects.all()


class ChannelListApiView(ListAPIView):
    serializer_class = ChannelSerailizer
    queryset = Channel.objects.all()


class ChannelApiModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options', 'head']
    edit_methods = ['POST','PUT','PATCH','DELETE']
    def get_permissions(self):
        if self.request.method in self.edit_methods:
            return [IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()]
        return []

    def get_queryset(self):
        # if self.request.method in self.edit_methods:
        #     return Channel.objects.filter(profile=self.request.user.profile)
        # return Channel.objects.all()
        return Channel.objects.filter(profile=self.request.user.profile)

    def get_serializer_context(self):
        if self.request.user.is_authenticated:
            return {"profile_id":self.request.user.profile.id}
        return super().get_serializer_context()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ChannelCreateSerailizer
        elif self.request.method in ['PUT','PATCH','DELETE']:
            return ChannelEditSerializer
        return ChannelSerailizer



class ContentApiModelViewSet(ModelViewSet):
    http_method_names = ['get','post','put','patch','delete','options','head']
    edit_method = ['POST','PUT','PATCH','DELETE']
    def get_permissions(self):
        if self.request.method in self.edit_method:
            return [IsAuthenticatedOrReadOnly(), IsChannelOwnerOrReadOnly()]
        return []
    
    def get_queryset(self):
        if self.request.method in self.edit_method:
            return Content.objects.filter(Q(channel_id=self.kwargs['channel_pk'])& 
            Q(channel_profile=self.request.user.profile))
        return Content.objects.filter(channel_id=self.kwargs['channel_pk'])
    
    def get_serializer_context(self):
        return {"channel_id":self.kwargs['channel_pk']}

    def get_serializer_class(self):
        return ContentSerializer


class CommentApiModelViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(content_id=self.kwargs['content_pk'])
    
    def get_serializer_context(self):
        return {
            "content_id":self.kwargs['content_pk'],
            "profile_id":self.request.user.profile.id,
        }