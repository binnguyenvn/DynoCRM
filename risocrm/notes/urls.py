"""
    App Router
    Note Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from risocrm.notes.apis import NoteViewSet, create

app_name = 'notes'

router = SimpleRouter(trailing_slash=False)
router.register(r"", NoteViewSet)

fake_api = [
    path('create', create, name="create"),
    path('', include(router.urls)),
    
]

urlpatterns = [
    path("api/", include(fake_api)),
]
