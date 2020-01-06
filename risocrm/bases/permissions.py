"""
    Custom Permission
"""
from django.http import HttpResponseForbidden
from rest_framework.permissions import BasePermission, IsAuthenticated


class IsSuperUserOnly(BasePermission):
    """
        Only allow SuperUser
    """

    def has_permission(self, request, view):
        """
            Per Module Permission
        """
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """
            Per Object Permission
        """
        return request.user.is_superuser


class IsNotAuthenticated(IsAuthenticated):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return False
        else:
            return True


class IsStaffOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff


class IsSuperOrOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        is_owner = True if obj.creator == request.user else False
        return any(request.user.is_superuser, is_owner)


# USER PASS TEST DECORATOR
def isSelfOrSuperOrDenie(f):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return f(request, *args, **kwargs)
        if request.user.groups.filter(name='Administrator').exists():
            return f(request, *args, **kwargs)
        if int(kwargs.get('pk')) == request.user.id:
            return f(request, *args, **kwargs)
        return HttpResponseForbidden()
    return wrap


def roleAdministrator(user):
    return user.groups.filter(name='Administrator').exists()
