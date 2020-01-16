"""
    App Models
    Notification system
"""
from django.contrib.auth import get_user_model
from django.db.models import (CASCADE, BooleanField, CharField, DateTimeField,
                              ForeignKey, Model)
from django.utils import timezone

from risocrm.bases.models import BaseModel
from webpush import send_user_notification

User = get_user_model()

NOTICE_CHOICES = (
    ('flaticon2-gear', 'System'),
    ('flaticon2-user', 'Customer'),
    ('flaticon2-send', 'Email'),
    ('flaticon2-calendar-1', 'Event'),
    ('flaticon2-indent-dots', 'Task'),

)


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
        payload = {"head": "Notification from CRM", "body": self.content,
                   "icon": "https://riso-media.s3.amazonaws.com/static/images/logo.svg", "url": self.url}
        send_user_notification(user=self.to_user, payload=payload, ttl=1000)
