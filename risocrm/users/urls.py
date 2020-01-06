"""
    App Router
    Staff Management
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from risocrm.users.views import (create, delete, detail, index,
                                 user_redirect_view, view)
from risocrm.users.apis import UserViewSet
app_name = "users"

router = SimpleRouter(trailing_slash=False)
router.register(r"", UserViewSet)

fake_api = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("~redirect/", user_redirect_view, name="redirect"),
    path('', index, name="list"),
    path('create', create, name="create"),
    path('delete', delete, name="delete"),
    path('api/', include(fake_api)),
    path("view/<str:username>/", view, name="view"),
    path("<str:username>/", detail, name="detail"),
]
