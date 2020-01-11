"""
    App Router
    Contacts Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from risocrm.contacts.apis import ContactViewSet
from risocrm.contacts.views import index, create, edit, delete, view

app_name = 'contacts'

router = SimpleRouter(trailing_slash=False)
router.register(r"", ContactViewSet, basename="contacts")

urlpatterns = [
    path('', index, name="list"),
    path('create', create, name="create"),
    path('<str:pk>', edit, name="edit"),
    path('view/<str:pk>', view, name="view"),
    path('delete', delete, name="delete"),
    path('api/', include(router.urls)),
]