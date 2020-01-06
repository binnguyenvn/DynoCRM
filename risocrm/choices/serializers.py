"""
    Choice serializer
"""
from risocrm.bases.serializers import BaseSerializer

from risocrm.choices.models import Choice, ChoiceDetail


class ChoiceSerializer(BaseSerializer):
    """
        Choice with full field
    """

    class Meta:
        model = Choice
        fields = "__all__"


class ChoiceDepthSerializer(BaseSerializer):
    """
        Choice with full field
    """

    class Meta:
        model = Choice
        fields = "__all__"
        depth = 1


class ChoiceDetailSerializer(BaseSerializer):
    """
        Detail with full field
    """

    class Meta:
        model = ChoiceDetail
        fields = "__all__"


class ChoiceDetailDepthSerializer(BaseSerializer):
    """
        Detail with full field
    """

    class Meta:
        model = ChoiceDetail
        fields = "__all__"
        depth = 1