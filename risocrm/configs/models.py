"""
    App Models
    Personal Configs on system
"""
from django.db.models import (CASCADE, BooleanField, CharField, F, ForeignKey,
                              Model, SmallIntegerField, TextField)

from risocrm.bases.models import BaseModel


class SystemConfig(BaseModel):
    """
        System
    """

    def __str__(self):
        return F"System {self.creator.fist_name}"


class ContactConfig(BaseModel):
    """
        Contact
    """

    def __str__(self):
        return F"Contact {self.creator.fist_name}"


class FilterConfig(BaseModel):
    """
        Filter
    """
    module = CharField(max_length=200, null=False, blank=False)
    filter = ForeignKey("filters.Filter", verbose_name="defaul_filter", on_delete=CASCADE)

    def __str__(self):
        return F"Filter {self.creator.fist_name}"
