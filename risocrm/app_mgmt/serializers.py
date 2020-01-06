"""
    App serializer
    App Management
"""
from risocrm.bases.serializers import BaseSerializer

from risocrm.app_mgmt.models import Dynafield


class DynafieldSerializer(BaseSerializer):
    """
        Dynafield with full field
    """

    class Meta:
        model = Dynafield
        fields = "__all__"