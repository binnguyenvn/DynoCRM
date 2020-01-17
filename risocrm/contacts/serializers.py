"""
    App serializer
    Contact serializer
"""
from rest_framework.serializers import DateField, ModelSerializer, SlugRelatedField

from risocrm.bases.serializers import BaseSerializer
from risocrm.contacts.models import Contact


class internalContactSerializer(ModelSerializer):
    """
        Contact with full field
    """

    class Meta:
        model = Contact
        fields = "__all__"


class ContactSerializer(BaseSerializer):
    """
        Contact with full field
    """

    class Meta:
        model = Contact
        fields = "__all__"


class ContactDepthSerializer(BaseSerializer):
    """
        Contact with full field
    """
    dob = DateField(format="%d-%m-%Y")
    creator = SlugRelatedField(slug_field='first_name', read_only=True)
    last_modified_by = SlugRelatedField(slug_field='first_name', read_only=True)
    city = SlugRelatedField(slug_field='value', read_only=True)
    rate = SlugRelatedField(slug_field='value', read_only=True)
    job = SlugRelatedField(slug_field='value', read_only=True)
    source = SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = Contact
        fields = "__all__"
        depth = 1
