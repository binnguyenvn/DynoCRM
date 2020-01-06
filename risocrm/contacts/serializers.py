"""
    App serializer
    Contact serializer
"""
from risocrm.bases.serializers import BaseSerializer

from risocrm.contacts.models import Contact


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

    class Meta:
        model = Contact
        fields = "__all__"
        depth = 1