from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, view, request, obj):
        return request.user == obj.created_by


class IsMe(BasePermission):
    def has_object_permission(self, view, request, user):
        return request.user == user
