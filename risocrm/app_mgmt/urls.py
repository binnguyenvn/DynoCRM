"""
    App Urls
    App Management
"""
from django.urls import include, path

from risocrm.app_mgmt.apis import get_field, get_field_type, get_foreign_data, get_module, make_migrations, migrate
from risocrm.app_mgmt.views import index, view, create, edit, delete

app_name = 'app_mgmt'

fake_api = [
    path('make_migrations', make_migrations, name="make_migrations"),
    path('migrate', migrate, name="migrate"),
    path('get_module', get_module, name="get_module"),
    path('get_field', get_field, name="get_field"),
    path('get_field_type', get_field_type, name="get_field_type"),
    path('get_foreign_data', get_foreign_data, name="get_foreign_data"),
]

urlpatterns = [
    path("", index, name="index"),
    path("view", view, name="view"),
    path("create", create, name="create"),
    path('delete', delete, name="delete"),
    path("api/", include(fake_api)),
    path('<str:pk>', edit, name="edit"),
]
