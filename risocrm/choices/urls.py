"""
    App Urls
    Filters Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from risocrm.choices.apis import ChoiceViewSet, choice_childs
from risocrm.choices.views import create, delete, edit, index, view

app_name = 'choices'

router = SimpleRouter(trailing_slash=False)
router.register(r"", ChoiceViewSet)

fake_api = [
    path("", include(router.urls)),
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
