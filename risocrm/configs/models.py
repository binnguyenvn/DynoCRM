"""
    App Models
    Configs Management
"""
from django.db.models import CASCADE, BooleanField, CharField, F, ForeignKey, Model, SmallIntegerField, TextField

from risocrm.bases.models import BaseModel
from risocrm.app_mgmt.helpers import get_field_object

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
    icon = CharField(max_length=50, null=False, blank=False)
    external = CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return F"External config for {self.module}: {self.external}"


class ReportConfig(BaseModel):
    """
        Report config
    """
    RP_TYPE = (
        ('count', 'Count'),
        ('percent', 'Percent'),
    )

    module = CharField(max_length=200, null=False, blank=False)
    name = CharField(max_length=200, null=False, blank=False)
    desc = CharField(max_length=200, null=False, blank=False)
    field = CharField(max_length=200, null=False, blank=False)
    type = CharField(choices=RP_TYPE, max_length=200, null=False, blank=False)

    def __str__(self):
        return F"Report config for {self.module}: {self.name}"

    def value(self):
        return 0


class FieldConfig(BaseModel):
    """
        Field config
    """
    module = CharField(max_length=200, null=False, blank=False)
    field = CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return F"Field config for {self.module}: {self.field}"

    def object(self):
        return get_field_object(self.module, self.field)


class FilterConfig(BaseModel):
    """
        Filter
    """
    module = CharField(max_length=200, null=False, blank=False)
    filter = ForeignKey("filters.Filter", verbose_name="defaul_filter", on_delete=CASCADE)

    def __str__(self):
        return F"Filter {self.creator.fist_name}"
