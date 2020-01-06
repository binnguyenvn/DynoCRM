"""
    App Router
    Contacts Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from risocrm.contacts.apis import ContactViewSet
from risocrm.contacts.views import index, create, edit, delete, view
from risocrm.contacts.configs import model_index

app_name = 'contacts'

router = SimpleRouter(trailing_slash=False)
router.register(r"", ContactViewSet, basename="contacts")

config_patterns = [
    path('', model_index, name="model_index"),
]

urlpatterns = [
    path('', index, name="list"),
    path('create', create, name="create"),
    path('<int:pk>', edit, name="edit"),
    path('view/<int:pk>', view, name="view"),
    path('delete', delete, name="delete"),
    path('api/', include(router.urls)),
    path('configs/', include(config_patterns)),
]