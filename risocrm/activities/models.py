"""
    App Models
    Activity Management
"""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              Model, SmallIntegerField, TextField)

from risocrm.bases.models import BaseModel

TYPE_CHOICES = (
    ('flaticon2-safe', 'System'),
    ('flaticon-facebook-letter-logo', 'Facebook'),
    ('flaticon-facebook-logo-button', 'Paid Facebook'),
    ('flaticon-letter-g', 'Google'),
    ('flaticon-mail-1', 'Email'),
    ('flaticon2-phone', 'Phone'),
    ('flaticon2-website', 'Website'),
    ('flaticon2-sheet', 'Form'),
)


class Activity(BaseModel):
    """
        Activity
    """
    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    object_id = CharField(max_length=100)
    content_object = GenericForeignKey('content_type', 'object_id')
    type = CharField(max_length=50, choices=TYPE_CHOICES, default='flaticon2-safe')
    note = TextField(null=False, blank=False)

    def __str__(self):
        return F'Activity {self.content_object}'
