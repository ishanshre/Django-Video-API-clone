from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.permissions import IsAdmnOrReadOnly, IsOwnerOrReadOnly
from core.serializers import (
    CategorySerializer,
    ChannelSerailizer,
    ChannelCreateSerailizer,
    ChannelEditSerializer,
)
from core.models import (
    Category,
    Channel,
)
# Create your views here.


class CategoryApiModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdmnOrReadOnly]
    queryset = Category.objects.all()




class ChannelApiModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options', 'head']
    edit_methods = ['POST','PUT','PATCH','DELETE']
    def get_permissions(self):
        if self.request.method in self.edit_methods:
            return [IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()]
        return []

    def get_queryset(self):
        if self.request.method in self.edit_methods:
            return Channel.objects.filter(profile=self.request.user.profile)
        return Channel.objects.all()

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