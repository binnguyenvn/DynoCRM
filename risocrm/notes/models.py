"""
    App Models
    Note Management
"""
from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              Model, SmallIntegerField, TextField)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from risocrm.bases.models import BaseModel

TYPE_CHOICES = (
    ('flaticon2-safe', 'System'),
    ('flaticon2-user', 'Human'),
)


class Note(BaseModel):
    """
        Note
    """
    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    object_id = CharField(max_length=100)
    content_object = GenericForeignKey('content_type', 'object_id')
    type = CharField(max_length=30, choices=TYPE_CHOICES, default='flaticon2-user')
    note = TextField(null=False, blank=False)

    def __str__(self):
        return F'Note {self.content_object}'
