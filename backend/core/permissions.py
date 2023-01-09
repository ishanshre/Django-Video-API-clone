from rest_framework.permissions import BasePermission



SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdmnOrReadOnly(BasePermission):
    """
    The request is authenticated as admin or is read only
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and 
            request.user.is_staff
        )


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to check if user is the owner of the object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.profile == request.user.profile