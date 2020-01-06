"""
    App Helper DRY
    Filter Management
"""
from risocrm.dashboard.models import Tile

def get_group_distinct_tuple():
    return [(m, m) for m in Tile.objects.all().values_list('dashboard', flat=True).distinct()]
