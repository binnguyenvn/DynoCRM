"""
    App Models
    Filter Models
"""
from django.db.models import (BooleanField, CharField, ForeignKey, Model,
                              TextField, CASCADE)

from risocrm.bases.global_variables import OPERATOR_CHOICES
from risocrm.bases.models import BaseModel


class Filter(BaseModel):
    """
        Filter model
    """
    name = CharField(max_length=200, null=False, blank=False, unique=True)
    field_list = TextField(null=True, blank=True)
    order_by = CharField(max_length=100, null=True, blank=True)
    module = CharField(max_length=200, null=False, blank=False)
    private = BooleanField(default=False)

    def __str__(self):
        return F'Model {self.name}'
        


class FilterDetail(Model):
    """
        Detail of filter
        it's a row
        if field name is Null it's mean operator for 2 other detail
    """
    filter = ForeignKey(Filter, related_name="filter_details", on_delete=CASCADE, null=False, blank=False)
    field_name = CharField(max_length=200, null=True, blank=True)
    operator = CharField(max_length=20, choices=OPERATOR_CHOICES, null=False, blank=False)
    value = CharField(max_length=500, null=True, blank=True)
