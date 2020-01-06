"""
    App Urls
    Filters Router
"""
from django.urls import include, path

from risocrm.choices.apis import choice_childs, choice_list
from risocrm.choices.views import create, delete, edit, index, view

app_name = 'choices'


fake_api = [
    path('choice_list', choice_list, name="choice_list"),
    path('choice_childs/<str:pk>', choice_childs, name="choice_childs"),
]

urlpatterns = [
    path('api/', include(fake_api)),
    path('', index, name="list"),
    path('create', create, name="create"),
    path('delete', delete, name="delete"),
    path("view/<str:pk>/", view, name="view"),
    path('<str:pk>', edit, name="edit"),
]
