"""
    App Public API
    Staff Management
"""

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from risocrm.users.serializers import UserDepthSerializer

User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    """
        User API for Admin manage
    """
    queryset = User.objects.all()
    serializer_class = UserDepthSerializer
    permission_classes = (IsAuthenticated,)
