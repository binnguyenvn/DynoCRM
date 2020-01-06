"""
    App Urls
    Filters Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from risocrm.filters.apis import FilterViewSet
from risocrm.filters.views import create, delete, edit, index

app_name = 'filters'

router = SimpleRouter(trailing_slash=False)
router.register(r"", FilterViewSet)

urlpatterns = [
    path('', index, name="list"),
    path('create', create, name="create"),
    path('delete', delete, name="delete"),
    path('api', include(router.urls)),
    path('<str:pk>', edit, name="edit"),
]
