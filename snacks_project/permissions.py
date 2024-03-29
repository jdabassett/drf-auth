from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # return bool(
        #     request.method in permissions.SAFE_METHODS or
        #     request.user and
        #     request.user.is_authenticated
        # )
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner