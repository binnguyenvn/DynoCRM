"""
    App Models
    Notification system
"""
from django.contrib.auth import get_user_model
from django.db.models import (CASCADE, BooleanField, CharField, DateTimeField,
                              ForeignKey, Model)
from django.utils import timezone

from risocrm.bases.global_variables import NOTICE_CHOICES
from risocrm.bases.models import BaseModel

User = get_user_model()


class Notice(BaseModel):
    content = CharField(max_length=5000, null=True, blank=True)
    url = CharField(max_length=550, null=True, blank=True)
    to_user = ForeignKey(
        User,
        related_name='read_notifications',
        null=True,
        blank=True,
        on_delete=CASCADE
    )
    is_read = BooleanField(default=False)
    type = CharField(choices=NOTICE_CHOICES, max_length=50, null=True, blank=True)

    def __str__(self):
        return u"%s" % (self.content)
    
    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)