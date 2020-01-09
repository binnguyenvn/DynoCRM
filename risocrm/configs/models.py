"""
    App Models
    Configs Management
"""
from django.db.models import CASCADE, BooleanField, CharField, F, ForeignKey, Model, SmallIntegerField, TextField

from risocrm.bases.models import BaseModel


class SystemConfig(BaseModel):
    """
        System
    """

    def __str__(self):
        return F"System {self.creator.fist_name}"


class ExternalConfig(BaseModel):
    """
        External config
    """
    module = CharField(max_length=200, null=False, blank=False)
    external = CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return F"External config for {self.module}: {self.external}"


class ReportConfig(BaseModel):
    """
        Report config
    """
    module = CharField(max_length=200, null=False, blank=False, unique=True)
    name = CharField(max_length=200, null=False, blank=False, unique=True)
    desc = CharField(max_length=200, null=False, blank=False, unique=True)
    field = CharField(max_length=200, null=False, blank=False, unique=True)
    type = CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return F"Report config for {self.module}: {self.name}"


class FieldConfig(BaseModel):
    """
        Field config
    """
    module = CharField(max_length=200, null=False, blank=False, unique=True)
    field = CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return F"Field config for {self.module}: {self.name}"


class FilterConfig(BaseModel):
    """
        Filter
    """
    module = CharField(max_length=200, null=False, blank=False)
    filter = ForeignKey("filters.Filter", verbose_name="defaul_filter", on_delete=CASCADE)

    def __str__(self):
        return F"Filter {self.creator.fist_name}"
