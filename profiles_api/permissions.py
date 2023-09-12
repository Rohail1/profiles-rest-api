from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfilePermission(BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user permission trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id


class ProfileFeedItemPermission(BasePermission):
    """Allow user to edit their own profile"""


    # def has_permission(self, request, view):
    #     """Check where user is logged-in or not"""
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Check user permission trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True
        return obj.user.id == request.user.id
