"""
    App serializer
    Activity serializer
"""
from rest_framework.serializers import DateTimeField

from risocrm.activities.models import Activity
from risocrm.bases.serializers import BaseSerializer


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
    time_created = DateTimeField()
    time_modified = DateTimeField()

    class Meta:
        model = Activity
        fields = "__all__"
        depth = 1
