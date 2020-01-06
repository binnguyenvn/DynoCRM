"""
    App Serializer
    Staff Management
"""
from django.contrib.auth import get_user_model
from risocrm.bases.serializers import BaseSerializer

User = get_user_model()


class UserSerializer(BaseSerializer):
    """
        User with full field
    """

    class Meta:
        model = User
        fields = "__all__"


class UserDepthSerializer(BaseSerializer):
    """
        User with full field
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'is_active', 'avatar', 'groups')
        depth = 1
