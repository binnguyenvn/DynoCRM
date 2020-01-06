"""
    App serializer
    Filter serializer
"""
from risocrm.bases.serializers import BaseSerializer

from risocrm.filters.models import Filter, FilterDetail


class FilterSerializer(BaseSerializer):
    """
        Filter with full field
    """

    class Meta:
        model = Filter
        fields = "__all__"


class FilterDepthSerializer(BaseSerializer):
    """
        Filter with full field
    """

    class Meta:
        model = Filter
        fields = "__all__"
        depth = 1


class FilterDetailSerializer(BaseSerializer):
    """
        Detail with full field
    """

    class Meta:
        model = FilterDetail
        fields = "__all__"


class FilterDetailDepthSerializer(BaseSerializer):
    """
        Detail with full field
    """

    class Meta:
        model = FilterDetail
        fields = "__all__"
        depth = 1