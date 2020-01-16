"""
    App Models
    Filter Models
"""
from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              Model, TextField)

from risocrm.bases.models import BaseModel

OPERATOR_CHOICES = [
    ('exact', 'Exact'),
    ('iexact', 'Exact case-insensitive'),
    ('contains', 'Contains'),
    ('icontains', 'Contains case-insensitive'),
    ('in', 'In'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than equal'),
    ('lt', 'Less than'),
    ('lte', 'Less than equal'),
    ('startswith', 'Start with'),
    ('istartswith', 'Start with case-insensitive'),
    ('endswith', 'End with'),
    ('iendswith', 'End with case-insensitive'),
    ('isnull', 'Is Null')
]


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
