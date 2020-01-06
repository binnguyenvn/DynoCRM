"""
    App Urls
    Filters Router
"""
from django.urls import path

from risocrm.filters.views import create, delete, edit, index

app_name = 'filters'

urlpatterns = [
    path('', index, name="list"),
    path('create', create, name="create"),
    path('delete', delete, name="delete"),
    path('<str:pk>', edit, name="edit"),
]
