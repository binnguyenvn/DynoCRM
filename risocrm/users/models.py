"""
    App Models
    Staff Management
"""
import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db.models import CASCADE, CharField, ForeignKey, ImageField
from django.urls import reverse


class User(AbstractUser):
    avatar = ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def group_verbose(self):
        GROUP = {
            'Administrator': 'danger',
            'Manager': 'warning',
            'Leader': 'success',
            'Sale': 'info',
        }
        try:
            group = self.groups.first().name
            return F'<span style="width: 100px;"><span class="btn btn-bold btn-sm btn-font-sm btn-label-{GROUP[group]}">{group}</span></span>'
        except Exception:
            return F'<span style="width: 100px;"><span class="btn btn-bold btn-sm btn-font-sm btn-label-danger">Non Group</span></span>'

    def active_verbose(self):
        if self.is_active:
            return '<span style="width: 100px;"><span class="btn btn-bold btn-sm btn-font-sm  btn-label-success">Active</span></span>'
        return '<span style="width: 100px;"><span class="btn btn-bold btn-sm btn-font-sm  btn-label-danger">Not Active</span></span>'

    def last_seen(self):
        return cache.get('seen_%s' % self.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

    def online_verbose(self):
        if self.online:
            return '<span style="width: 100px;"><span class="btn btn-bold btn-sm btn-font-sm  btn-label-success">Online</span></span>'
        return '<span style="width: 100px;"><span class="btn btn-bold btn-sm btn-font-sm  btn-label-danger">Offline</span></span>'
