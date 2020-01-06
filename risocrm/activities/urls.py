"""
    App Router
    Activity Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from risocrm.activities.apis import ActivityViewSet
# from risocrm.notes.views import index, create, edit, delete, view

app_name = 'activities'

router = SimpleRouter(trailing_slash=False)
router.register(r"", ActivityViewSet)

urlpatterns = [
    # path('', index, name="list"),
    # path('create', create, name="create"),
    
    # path('view/<int:pk>', view, name="view"),
    # path('delete', delete, name="delete"),
    path('api', include(router.urls)),
    # path('<int:pk>', edit, name="edit"),
]