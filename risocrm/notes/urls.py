"""
    App Router
    Note Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from risocrm.notes.apis import NoteViewSet
# from risocrm.notes.views import index, create, edit, delete, view

app_name = 'notes'

router = SimpleRouter(trailing_slash=False)
router.register(r"", NoteViewSet)

urlpatterns = [
    # path('', index, name="list"),
    # path('create', create, name="create"),
    
    # path('view/<int:pk>', view, name="view"),
    # path('delete', delete, name="delete"),
    path('api', include(router.urls)),
    # path('<int:pk>', edit, name="edit"),
]