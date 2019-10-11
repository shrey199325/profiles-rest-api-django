from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow to make authentication before change"""
    def has_object_permission(self, request, view, obj):
        """Check to change only user's own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Users will only create and update their status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
