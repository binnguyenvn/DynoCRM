"""
    App Model
    Dashboard
"""
from django.db.models import (CASCADE, BooleanField, CharField, DateTimeField,
                              ForeignKey, ImageField, Model, SmallIntegerField,
                              TextField, UUIDField)
from django.utils import timezone

from risocrm.bases.models import BaseModel

WIDTH_CHOICES = (
    ('6', 'Half'),
    ('12', 'Full'),

)
CHART_CHOICES = (
    ('column', 'Column Chart'),
    ('line', 'Line Chart'),
    ('column-line', 'Column Line Chart'),
    ('pie', 'Pie Chart'),
    ('radar', 'Radar Chart'),
    ('table', 'Table'),
)


class Tile(BaseModel):
    """
        Dashboard Tile model
    """
    name = CharField(max_length=200, null=False, blank=False, unique=True)
    position = SmallIntegerField(default=1)
    width = SmallIntegerField(choices=WIDTH_CHOICES, default='12')
    module = CharField(max_length=200, null=False, blank=False)
    field = CharField(max_length=200, null=False, blank=False)
    dashboard = CharField(max_length=200, null=True, blank=True, unique=True)
    type = CharField(choices=CHART_CHOICES, max_length=200, null=False, blank=False)

    def __str__(self):
        return F'Model {self.name}'


class TileDetail(Model):
    """
        Detail of tile
    """
    tile = ForeignKey(Tile, related_name="tile_details", on_delete=CASCADE, null=False, blank=False)
    field = CharField(max_length=200, null=False, blank=False)
    formula = CharField(max_length=200, null=False, blank=False)
    type = CharField(max_length=200, null=False, blank=False)
