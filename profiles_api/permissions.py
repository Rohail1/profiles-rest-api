from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfilePermission(BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user permission trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id
