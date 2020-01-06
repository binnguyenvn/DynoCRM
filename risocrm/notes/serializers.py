"""
    App serializer
    Note Management
"""
from risocrm.bases.serializers import BaseSerializer

from risocrm.notes.models import Note


class NoteSerializer(BaseSerializer):
    """
        Note with full field
    """

    class Meta:
        model = Note
        fields = "__all__"


class NoteDepthSerializer(BaseSerializer):
    """
        Note with full field
    """

    class Meta:
        model = Note
        fields = "__all__"
        depth = 1