from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if (obj.user == request.user or
                request.method in SAFE_METHODS):
            return True
        return False