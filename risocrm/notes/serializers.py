"""
    App Serializer
    Staff Management
"""
from rest_framework.serializers import DateTimeField

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
    time_created = DateTimeField()
    time_modified = DateTimeField()

    class Meta:
        model = Note
        fields = "__all__"
        depth = 1
