"""
    Choice serializer
"""
from risocrm.bases.serializers import BaseSerializer, ModelSerializer

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


## NESTED SERIALIZER
####################
class ChoiceDepthNestedSerializer(ModelSerializer):
    """
        Choice with full field
    """

    class Meta:
        model = Choice
        fields = "__all__"
        depth = 1


class ChoiceDetailNestedSerializer(ModelSerializer):
    """
        Detail with full field
    """

    class Meta:
        model = ChoiceDetail
        fields = ['value']


class ChoiceNestedSerializer(ModelSerializer):
    """
        Choice with nested save
    """
    details = ChoiceDetailNestedSerializer(many=True)

    class Meta:
        model = Choice
        fields = "__all__"
        extra_fields = ['details']

    def create(self, validated_data):
        tracks_data = validated_data.pop('details')
        choice = Choice.objects.create(**validated_data)
        for track_data in tracks_data:
            ChoiceDetail.objects.create(choice=choice, **track_data)
        return choice
