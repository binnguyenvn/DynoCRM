"""
    App serializer
    Activity serializer
"""
from risocrm.bases.serializers import BaseSerializer

from risocrm.activities.models import Activity


class ActivitySerializer(BaseSerializer):
    """
        Activity with full field
    """

    class Meta:
        model = Activity
        fields = "__all__"


class ActivityDepthSerializer(BaseSerializer):
    """
        Activity with full field
    """

    class Meta:
        model = Activity
        fields = "__all__"
        depth = 1
